"""
Serialización de mutaciones del banco en memoria (v2.9.4).
Evita condiciones de carrera cuando varios comandos tocan saldos a la vez.
"""
from __future__ import annotations

import asyncio
import functools
from contextlib import asynccontextmanager

from discord import app_commands


class EstadoBanco:
    def __init__(self) -> None:
        self.cuentas: dict = {}
        self._lock = asyncio.Lock()


estado = EstadoBanco()


def guardar_banco(cuentas: dict) -> None:
    """En producción: escritura atómica a JSON (ver storage.guardar_json_atomico)."""
    pass


@asynccontextmanager
async def transaccion_banco(*, persistir: bool = True):
    async with estado._lock:
        yield estado
        if persistir:
            guardar_banco(estado.cuentas)


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
