"""
Serialización de mutaciones del banco en memoria.
Evita condiciones de carrera; el fsync corre fuera del lock de mutación (hilo).
Soporta transacciones anidadas (ContextVar), serializa guardados concurrentes
y permite ACK de éxito solo tras confirmar persistencia.
Los callbacks de botones/menús persistentes deben usar transaccion_banco()
explícitamente, porque no pasan por el wrapper de slash commands.
"""
from __future__ import annotations

import asyncio
import copy
import functools
from collections.abc import Awaitable, Callable
from contextlib import asynccontextmanager
from contextvars import ContextVar

from discord import app_commands

PostCommit = Callable[[], Awaitable[None]]


class EstadoBanco:
    def __init__(self) -> None:
        self.cuentas: dict = {}
        self._lock = asyncio.Lock()
        self._persist_lock = asyncio.Lock()


class TransaccionBanco:
    def __init__(self, estado_banco: EstadoBanco) -> None:
        self.estado = estado_banco
        self._post_commit: list[PostCommit] = []

    @property
    def cuentas(self) -> dict:
        return self.estado.cuentas

    def despues_de_persistir(self, callback: PostCommit) -> None:
        self._post_commit.append(callback)


estado = EstadoBanco()
_profundidad_transaccion_banco: ContextVar[int] = ContextVar(
    "profundidad_transaccion_banco",
    default=0,
)
_transaccion_actual: ContextVar[TransaccionBanco | None] = ContextVar(
    "_transaccion_actual",
    default=None,
)
_tarea_transaccion_banco: ContextVar[asyncio.Task | None] = ContextVar(
    "_tarea_transaccion_banco",
    default=None,
)


def al_confirmar_persistencia(callback: PostCommit) -> None:
    """Registra una acción que solo debe ejecutarse tras guardar el snapshot."""
    tx = _transaccion_actual.get()
    if tx is None or _tarea_transaccion_banco.get() is not asyncio.current_task():
        raise RuntimeError("al_confirmar_persistencia requiere transaccion_banco activa")
    tx.despues_de_persistir(callback)


def guardar_banco(cuentas: dict) -> None:
    """En producción: escritura atómica a JSON (ver 06_persistencia_json_atomica)."""
    pass


@asynccontextmanager
async def transaccion_banco(*, persistir: bool = True):
    profundidad = _profundidad_transaccion_banco.get()
    tarea_actual = asyncio.current_task()
    if profundidad and _tarea_transaccion_banco.get() is tarea_actual:
        token = _profundidad_transaccion_banco.set(profundidad + 1)
        try:
            yield estado
        finally:
            _profundidad_transaccion_banco.reset(token)
        return
    if profundidad:
        # create_task() copia ContextVar: una tarea hija debe abrir su propia
        # transaccion para no saltarse el lock ni la persistencia.
        _profundidad_transaccion_banco.set(0)
        _transaccion_actual.set(None)
        _tarea_transaccion_banco.set(None)

    tx = TransaccionBanco(estado)
    async with estado._lock:
        depth_token = _profundidad_transaccion_banco.set(1)
        tx_token = _transaccion_actual.set(tx)
        task_token = _tarea_transaccion_banco.set(tarea_actual)
        snapshot = None
        try:
            yield estado
        finally:
            if persistir:
                snapshot = copy.deepcopy(estado.cuentas)
            _transaccion_actual.reset(tx_token)
            _tarea_transaccion_banco.reset(task_token)
            _profundidad_transaccion_banco.reset(depth_token)

    if snapshot is not None:
        async with estado._persist_lock:
            await asyncio.to_thread(guardar_banco, snapshot)
        for callback in tx._post_commit:
            await callback()


def envolver_arbol_comandos(tree: app_commands.CommandTree) -> None:
    """Envuelve cada slash command para ejecutarse dentro de transaccion_banco."""

    def _envolver(cmd: app_commands.Command | app_commands.Group) -> None:
        if isinstance(cmd, app_commands.Group):
            for sub in cmd.commands:
                _envolver(sub)
            return
        original = cmd._callback

        @functools.wraps(original)
        async def wrapper(interaction, *args, **kwargs):
            async with transaccion_banco():
                return await original(interaction, *args, **kwargs)

        cmd._callback = wrapper

    for cmd in tree.get_commands():
        _envolver(cmd)
