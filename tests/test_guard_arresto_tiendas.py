from __future__ import annotations

import importlib.util
import pathlib
import sys
import types
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "ejemplos" / "03_guard_arresto_tiendas.py"


def _instalar_discord_stub() -> None:
    if "discord" in sys.modules:
        discord = sys.modules["discord"]
        if not hasattr(discord, "HTTPException"):
            discord.HTTPException = Exception
        return

    discord = types.ModuleType("discord")
    app_commands = types.ModuleType("discord.app_commands")

    class HTTPException(Exception):
        pass

    class Command:
        pass

    class Group:
        commands = []

    class CommandTree:
        pass

    discord.HTTPException = HTTPException
    app_commands.Command = Command
    app_commands.Group = Group
    app_commands.CommandTree = CommandTree
    discord.app_commands = app_commands
    sys.modules["discord"] = discord
    sys.modules["discord.app_commands"] = app_commands


def _cargar_modulo():
    _instalar_discord_stub()
    spec = importlib.util.spec_from_file_location("guard_arresto_tiendas", MODULE_PATH)
    assert spec is not None
    assert spec.loader is not None
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


class _Usuario:
    bot = False
    id = 123


class _Respuesta:
    def __init__(self) -> None:
        self.enviados: list[tuple[str, bool]] = []

    def is_done(self) -> bool:
        return False

    async def send_message(self, mensaje: str, *, ephemeral: bool) -> None:
        self.enviados.append((mensaje, ephemeral))


class _Followup:
    def __init__(self) -> None:
        self.enviados: list[tuple[str, bool]] = []

    async def send(self, mensaje: str, *, ephemeral: bool) -> None:
        self.enviados.append((mensaje, ephemeral))


class _Interaction:
    def __init__(self) -> None:
        self.user = _Usuario()
        self.response = _Respuesta()
        self.followup = _Followup()


class GuardArrestoTiendasTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.mod = _cargar_modulo()

    def test_esta_arrestado_solo_bloquea_contadores_positivos(self) -> None:
        self.assertFalse(self.mod.esta_arrestado({}))
        self.assertFalse(self.mod.esta_arrestado({"arresto_trabajos_pendientes": None}))
        self.assertFalse(self.mod.esta_arrestado({"arresto_trabajos_pendientes": ""}))
        self.assertFalse(self.mod.esta_arrestado({"arresto_trabajos_pendientes": "pendiente"}))
        self.assertTrue(self.mod.esta_arrestado({"arresto_trabajos_pendientes": "2"}))

    async def test_bloquear_si_arrestado_no_crashea_con_contador_nulo(self) -> None:
        interaction = _Interaction()
        banco = {"123": {"arresto_trabajos_pendientes": None}}

        bloqueado = await self.mod.bloquear_si_arrestado(interaction, banco)

        self.assertFalse(bloqueado)
        self.assertEqual(interaction.response.enviados, [])
        self.assertEqual(interaction.followup.enviados, [])

    async def test_bloquear_si_arrestado_envia_mensaje_para_contador_positivo(self) -> None:
        interaction = _Interaction()
        banco = {"123": {"arresto_trabajos_pendientes": 1}}

        bloqueado = await self.mod.bloquear_si_arrestado(interaction, banco)

        self.assertTrue(bloqueado)
        self.assertEqual(
            interaction.response.enviados,
            [(self.mod.MENSAJE_BLOQUEO_ARRESTO, True)],
        )


if __name__ == "__main__":
    unittest.main()
