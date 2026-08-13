from __future__ import annotations

import asyncio
import importlib.util
import pathlib
import sys
import types
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "ejemplos" / "05_lock_transacciones_banco.py"


def _instalar_discord_stub() -> None:
    if "discord" in sys.modules:
        return

    discord = types.ModuleType("discord")
    app_commands = types.ModuleType("discord.app_commands")

    class Command:
        pass

    class Group:
        commands = []

    class CommandTree:
        pass

    app_commands.Command = Command
    app_commands.Group = Group
    app_commands.CommandTree = CommandTree
    discord.app_commands = app_commands
    sys.modules["discord"] = discord
    sys.modules["discord.app_commands"] = app_commands


def _cargar_modulo():
    _instalar_discord_stub()
    spec = importlib.util.spec_from_file_location("lock_transacciones_banco", MODULE_PATH)
    assert spec is not None
    assert spec.loader is not None
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


class TransaccionBancoTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.mod = _cargar_modulo()
        self.mod.estado = self.mod.EstadoBanco()

    async def test_transacciones_anidadas_reusan_el_lock_y_persisten_una_vez(self):
        guardados: list[dict] = []

        def guardar(cuentas: dict) -> None:
            guardados.append(dict(cuentas))

        self.mod.guardar_banco = guardar

        async def operacion_anidada():
            async with self.mod.transaccion_banco():
                self.mod.estado.cuentas["usuario"] = {"balance": 100}
                async with self.mod.transaccion_banco():
                    self.mod.estado.cuentas["usuario"]["balance"] += 50

        await asyncio.wait_for(operacion_anidada(), timeout=1)

        self.assertEqual(self.mod.estado.cuentas["usuario"]["balance"], 150)
        self.assertEqual(guardados, [{"usuario": {"balance": 150}}])

    async def test_post_commit_se_ejecuta_tras_persistir(self):
        orden: list[str] = []

        def guardar(_cuentas: dict) -> None:
            orden.append("persist")

        self.mod.guardar_banco = guardar

        async def operacion():
            async with self.mod.transaccion_banco():
                self.mod.estado.cuentas["u"] = {"balance": 1}

                async def ack():
                    orden.append("ack")

                self.mod.al_confirmar_persistencia(ack)

        await operacion()
        self.assertEqual(orden, ["persist", "ack"])


if __name__ == "__main__":
    unittest.main()
