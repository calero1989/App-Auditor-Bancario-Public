"""
Serialización de mutaciones del banco en memoria.
Evita condiciones de carrera; el fsync corre fuera del lock (hilo).
Los callbacks de botones/menús persistentes deben usar transaccion_banco()
explícitamente, porque no pasan por el wrapper de slash commands.
"""
from __future__ import annotations

import asyncio
import copy
import functools
from contextlib import asynccontextmanager

from discord import app_commands


class EstadoBanco:
    def __init__(self) -> None:
        self.cuentas: dict = {}
        self._lock = asyncio.Lock()


estado = EstadoBanco()


def guardar_banco(cuentas: dict) -> None:
    """En producción: escritura atómica a JSON (ver 06_persistencia_json_atomica)."""
    pass


@asynccontextmanager
async def transaccion_banco(*, persistir: bool = True):
    async with estado._lock:
        yield estado
        snapshot = copy.deepcopy(estado.cuentas) if persistir else None
    if snapshot is not None:
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
