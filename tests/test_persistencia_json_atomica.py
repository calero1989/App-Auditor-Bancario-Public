from __future__ import annotations

import importlib.util
import json
import os
import pathlib
import tempfile
import unittest
from unittest import mock


ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "ejemplos" / "06_persistencia_json_atomica.py"


def _cargar_modulo():
    spec = importlib.util.spec_from_file_location("persistencia_json_atomica", MODULE_PATH)
    assert spec is not None
    assert spec.loader is not None
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


class GuardarJsonAtomicoTests(unittest.TestCase):
    def test_guarda_json_y_sincroniza_archivo_y_directorio(self) -> None:
        modulo = _cargar_modulo()
        real_fsync = os.fsync
        fsyncs: list[int] = []

        def registrar_fsync(fd: int) -> None:
            fsyncs.append(fd)
            real_fsync(fd)

        with tempfile.TemporaryDirectory() as tmpdir:
            ruta = os.path.join(tmpdir, "banco_vct.json")
            datos = {"cuentas": {"123": {"balance": 5000, "vault": 2000}}}

            with mock.patch.object(modulo.os, "fsync", side_effect=registrar_fsync):
                modulo.guardar_json_atomico(ruta, datos)

            with open(ruta, encoding="utf-8") as archivo:
                self.assertEqual(json.load(archivo), datos)
            self.assertGreaterEqual(len(fsyncs), 2)
            self.assertEqual([], list(pathlib.Path(tmpdir).glob("*.tmp")))


if __name__ == "__main__":
    unittest.main()
