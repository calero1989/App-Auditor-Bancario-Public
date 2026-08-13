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

    def test_conserva_temporal_completo_si_replace_falla(self) -> None:
        modulo = _cargar_modulo()
        with tempfile.TemporaryDirectory() as tmpdir:
            ruta = pathlib.Path(tmpdir) / "banco.json"
            ruta.write_text('{"saldo": 1}', encoding="utf-8")

            with mock.patch.object(
                modulo.os,
                "replace",
                side_effect=PermissionError("archivo bloqueado"),
            ):
                with self.assertRaises(PermissionError):
                    modulo.guardar_json_atomico(str(ruta), {"saldo": 2})

            self.assertEqual(json.loads(ruta.read_text(encoding="utf-8")), {"saldo": 1})
            temporales = list(pathlib.Path(tmpdir).glob("banco.json.*.tmp"))
            self.assertEqual(len(temporales), 1)
            self.assertEqual(
                json.loads(temporales[0].read_text(encoding="utf-8")),
                {"saldo": 2},
            )

    def test_elimina_temporal_parcial_si_serializacion_falla(self) -> None:
        modulo = _cargar_modulo()
        with tempfile.TemporaryDirectory() as tmpdir:
            ruta = pathlib.Path(tmpdir) / "banco.json"

            with self.assertRaises(TypeError):
                modulo.guardar_json_atomico(str(ruta), {"no_json": object()})

            self.assertEqual(list(pathlib.Path(tmpdir).glob("banco.json.*.tmp")), [])


if __name__ == "__main__":
    unittest.main()
