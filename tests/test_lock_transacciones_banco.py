from __future__ import annotations

import copy
import importlib.util
import sys
import types
import unittest
from pathlib import Path


def cargar_modulo_banco():
    discord = types.ModuleType("discord")
    discord.app_commands = types.SimpleNamespace(
        Command=object,
        CommandTree=object,
        Group=object,
    )
    sys.modules["discord"] = discord

    ruta = Path(__file__).resolve().parents[1] / "ejemplos" / "05_lock_transacciones_banco.py"
    spec = importlib.util.spec_from_file_location("lock_transacciones_banco", ruta)
    modulo = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(modulo)
    return modulo


class TransaccionBancoTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.modulo = cargar_modulo_banco()
        self.guardados: list[dict] = []

        def guardar(cuentas: dict) -> None:
            self.guardados.append(copy.deepcopy(cuentas))

        self.modulo.guardar_banco = guardar

    async def test_persiste_al_salir_correctamente(self) -> None:
        async with self.modulo.transaccion_banco():
            self.modulo.estado.cuentas["42"] = {"balance": 1000}

        self.assertEqual(self.guardados, [{"42": {"balance": 1000}}])

    async def test_persiste_si_el_comando_falla_tras_mutar_saldo(self) -> None:
        with self.assertRaises(RuntimeError):
            async with self.modulo.transaccion_banco():
                self.modulo.estado.cuentas["42"] = {"balance": 750}
                raise RuntimeError("fallo al responder a Discord")

        self.assertEqual(self.guardados, [{"42": {"balance": 750}}])

    async def test_no_persiste_cuando_se_desactiva_expresamente(self) -> None:
        async with self.modulo.transaccion_banco(persistir=False):
            self.modulo.estado.cuentas["42"] = {"balance": 500}

        self.assertEqual(self.guardados, [])


if __name__ == "__main__":
    unittest.main()
