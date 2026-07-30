"""
Serialización de mutaciones del banco en memoria.
Evita condiciones de carrera; el fsync corre fuera del lock de mutación (hilo).
Soporta transacciones anidadas (ContextVar) y serializa guardados concurrentes.
"""
from __future__ import annotations

import asyncio
import copy
import functools
from contextlib import asynccontextmanager
from contextvars import ContextVar

from discord import app_commands


class EstadoBanco:
    def __init__(self) -> None:
        self.cuentas: dict = {}
        self._lock = asyncio.Lock()
        self._persist_lock = asyncio.Lock()


estado = EstadoBanco()
_profundidad_transaccion_banco: ContextVar[int] = ContextVar(
    "profundidad_transaccion_banco",
    default=0,
)


def guardar_banco(cuentas: dict) -> None:
    """En producción: escritura atómica a JSON (ver 06_persistencia_json_atomica)."""
    pass


@asynccontextmanager
async def transaccion_banco(*, persistir: bool = True):
    profundidad = _profundidad_transaccion_banco.get()
    if profundidad:
        token = _profundidad_transaccion_banco.set(profundidad + 1)
        try:
            yield estado
        finally:
            _profundidad_transaccion_banco.reset(token)
        return

    async with estado._lock:
        token = _profundidad_transaccion_banco.set(1)
        snapshot = None
        try:
            yield estado
        finally:
            if persistir:
                snapshot = copy.deepcopy(estado.cuentas)
            _profundidad_transaccion_banco.reset(token)

    if snapshot is not None:
        async with estado._persist_lock:
            await asyncio.to_thread(guardar_banco, snapshot)


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
