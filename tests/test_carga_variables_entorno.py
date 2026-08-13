from __future__ import annotations

import importlib.util
import os
import pathlib
import unittest
from unittest import mock

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "ejemplos" / "02_carga_variables_entorno.py"
ENV_PATH = ROOT / "kofi.env"


def _cargar_modulo():
    spec = importlib.util.spec_from_file_location("carga_variables_entorno", MODULE_PATH)
    assert spec is not None
    assert spec.loader is not None
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


class CargaVariablesEntornoTests(unittest.TestCase):
    def tearDown(self) -> None:
        try:
            ENV_PATH.unlink()
        except FileNotFoundError:
            pass

    def test_variable_en_blanco_no_oculta_valor_de_kofi_env(self) -> None:
        ENV_PATH.write_text(
            "DISCORD_BOT_TOKEN=token_desde_archivo\n",
            encoding="utf-8",
        )

        with mock.patch.dict(os.environ, {"DISCORD_BOT_TOKEN": "   "}):
            modulo = _cargar_modulo()

        self.assertEqual(modulo.DISCORD_BOT_TOKEN, "token_desde_archivo")

    def test_kofi_env_acepta_prefijo_export(self) -> None:
        ENV_PATH.write_text(
            "export DISCORD_BOT_TOKEN='token_exportado'\n",
            encoding="utf-8",
        )

        with mock.patch.dict(os.environ, {}, clear=True):
            modulo = _cargar_modulo()

        self.assertEqual(modulo.DISCORD_BOT_TOKEN, "token_exportado")


if __name__ == "__main__":
    unittest.main()
