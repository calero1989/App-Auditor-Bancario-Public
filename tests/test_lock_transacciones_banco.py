import asyncio
import importlib
import sys
import types
import unittest


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


class TransaccionBancoTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        _instalar_discord_stub()
        self.mod = importlib.import_module("ejemplos.05_lock_transacciones_banco")
        self.mod.estado = self.mod.EstadoBanco()

    async def test_transacciones_anidadas_reusan_el_lock_y_persisten_una_vez(self):
        guardados = []
        self.mod.guardar_banco = lambda cuentas: guardados.append(dict(cuentas))

        async def operacion_anidada():
            async with self.mod.transaccion_banco():
                self.mod.estado.cuentas["usuario"] = {"balance": 100}
                async with self.mod.transaccion_banco():
                    self.mod.estado.cuentas["usuario"]["balance"] += 50

        await asyncio.wait_for(operacion_anidada(), timeout=1)

        self.assertEqual(self.mod.estado.cuentas["usuario"]["balance"], 150)
        self.assertEqual(guardados, [{"usuario": {"balance": 150}}])


if __name__ == "__main__":
    unittest.main()
