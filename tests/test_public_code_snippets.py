import json
import re
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class PublicCodeSnippetTests(unittest.TestCase):
    def test_atomic_json_helper_snippet_writes_file(self):
        report = REPO_ROOT / "informes" / "INFORME_PUBLICO_CODIGO_VCT.md"
        text = report.read_text(encoding="utf-8")
        match = re.search(
            r"## 4\. Persistencia segura.*?```python\n(?P<code>.*?)\n```",
            text,
            re.DOTALL,
        )
        self.assertIsNotNone(match, "storage.py snippet not found")

        namespace: dict[str, object] = {}
        exec(match.group("code"), namespace)

        payload = {"123": {"balance": 5000, "vault": 2500}}
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "banco_vct.json"
            namespace["guardar_json_atomico"](str(path), payload)

            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), payload)
            self.assertEqual(list(Path(tmpdir).glob("banco_vct.json.*.tmp")), [])


if __name__ == "__main__":
    unittest.main()
