"""
Serialización de mutaciones del banco en memoria.
Evita condiciones de carrera; el fsync corre fuera del lock (hilo).
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


estado = EstadoBanco()
_transaccion_actual: ContextVar["TransaccionBanco | None"] = ContextVar(
    "_transaccion_actual",
    default=None,
)


class TransaccionBanco:
    def __init__(self, estado_banco: EstadoBanco) -> None:
        self.estado = estado_banco
        self._post_commit: list[PostCommit] = []

    @property
    def cuentas(self) -> dict:
        return self.estado.cuentas

    def despues_de_persistir(self, callback: PostCommit) -> None:
        self._post_commit.append(callback)


def al_confirmar_persistencia(callback: PostCommit) -> None:
    """Registra una acción que solo debe ejecutarse tras guardar el snapshot."""
    tx = _transaccion_actual.get()
    if tx is None:
        raise RuntimeError("al_confirmar_persistencia requiere transaccion_banco activa")
    tx.despues_de_persistir(callback)


def guardar_banco(cuentas: dict) -> None:
    """En producción: escritura atómica a JSON (ver 06_persistencia_json_atomica)."""
    pass


@asynccontextmanager
async def transaccion_banco(*, persistir: bool = True):
    tx = TransaccionBanco(estado)
    async with estado._lock:
        token = _transaccion_actual.set(tx)
        try:
            yield estado
            snapshot = copy.deepcopy(estado.cuentas) if persistir else None
        finally:
            _transaccion_actual.reset(token)
    if snapshot is not None:
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
