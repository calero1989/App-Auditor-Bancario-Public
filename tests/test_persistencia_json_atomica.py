from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "ejemplos"
    / "06_persistencia_json_atomica.py"
)


def _cargar_modulo():
    spec = importlib.util.spec_from_file_location("persistencia_json_atomica", MODULE_PATH)
    modulo = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(modulo)
    return modulo


class GuardarJsonAtomicoTests(unittest.TestCase):
    def test_conserva_temporal_completo_si_replace_falla(self) -> None:
        modulo = _cargar_modulo()
        with tempfile.TemporaryDirectory() as tmpdir:
            ruta = Path(tmpdir) / "banco.json"
            ruta.write_text('{"saldo": 1}', encoding="utf-8")

            with mock.patch.object(
                modulo.os,
                "replace",
                side_effect=PermissionError("archivo bloqueado"),
            ):
                with self.assertRaises(PermissionError):
                    modulo.guardar_json_atomico(str(ruta), {"saldo": 2})

            self.assertEqual(json.loads(ruta.read_text(encoding="utf-8")), {"saldo": 1})
            temporales = list(Path(tmpdir).glob("banco.json.*.tmp"))
            self.assertEqual(len(temporales), 1)
            self.assertEqual(
                json.loads(temporales[0].read_text(encoding="utf-8")),
                {"saldo": 2},
            )

    def test_elimina_temporal_parcial_si_serializacion_falla(self) -> None:
        modulo = _cargar_modulo()
        with tempfile.TemporaryDirectory() as tmpdir:
            ruta = Path(tmpdir) / "banco.json"

            with self.assertRaises(TypeError):
                modulo.guardar_json_atomico(str(ruta), {"no_json": object()})

            self.assertEqual(list(Path(tmpdir).glob("banco.json.*.tmp")), [])


if __name__ == "__main__":
    unittest.main()
