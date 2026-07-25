from __future__ import annotations

import asyncio
import importlib.util
import pathlib
import sys
import time
import types
import unittest


def _cargar_modulo_banco():
    discord = types.ModuleType("discord")

    class _Command:
        pass

    class _Group:
        commands = []

    class _CommandTree:
        def get_commands(self):
            return []

    app_commands = types.SimpleNamespace(
        Command=_Command,
        Group=_Group,
        CommandTree=_CommandTree,
    )
    discord.app_commands = app_commands

    sys.modules.setdefault("discord", discord)
    sys.modules.setdefault("discord.app_commands", app_commands)

    ruta = pathlib.Path(__file__).resolve().parents[1] / "ejemplos" / "05_lock_transacciones_banco.py"
    spec = importlib.util.spec_from_file_location("lock_transacciones_banco", ruta)
    modulo = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(modulo)
    return modulo


class TransaccionBancoTests(unittest.IsolatedAsyncioTestCase):
    async def test_guardados_concurrentes_respetan_orden_de_transaccion(self):
        modulo = _cargar_modulo_banco()
        modulo.estado = modulo.EstadoBanco()
        guardados: list[int] = []

        def guardar_lento(cuentas: dict) -> None:
            saldo = cuentas["saldo"]
            if saldo == 1:
                time.sleep(0.05)
            guardados.append(saldo)

        modulo.guardar_banco = guardar_lento

        async def mutar(saldo: int) -> None:
            async with modulo.transaccion_banco() as estado:
                estado.cuentas["saldo"] = saldo
                await asyncio.sleep(0)

        await asyncio.gather(mutar(1), mutar(2))

        self.assertEqual([1, 2], guardados)


if __name__ == "__main__":
    unittest.main()
