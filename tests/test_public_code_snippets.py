import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _extract_python_snippet(section_title: str) -> str:
    report = REPO_ROOT / "informes" / "INFORME_PUBLICO_CODIGO_VCT.md"
    text = report.read_text(encoding="utf-8")
    pattern = rf"## {re.escape(section_title)}.*?```python\n(?P<code>.*?)\n```"
    match = re.search(pattern, text, re.DOTALL)
    if match is None:
        raise AssertionError(f"Python snippet for section {section_title!r} not found")
    return match.group("code")


class PublicCodeSnippetTests(unittest.IsolatedAsyncioTestCase):
    async def test_bank_transaction_snippet_persists_snapshot(self):
        code = _extract_python_snippet("5. Lock anti double-spend (`banco_sync.py`)")

        class DummyBot:
            def __init__(self):
                import asyncio

                self._banco_lock = asyncio.Lock()
                self.banco = {"123": {"balance": 10, "vault": 0}}

        bot = DummyBot()
        saves = []

        def guardar_json_atomico(path, snapshot):
            saves.append((path, snapshot))

        def ruta_banco():
            return "banco_vct.json"

        namespace = {
            "bot": bot,
            "guardar_json_atomico": guardar_json_atomico,
            "ruta_banco": ruta_banco,
        }
        exec(code, namespace)

        async with namespace["transaccion_banco"]():
            bot.banco["123"]["balance"] -= 3
            bot.banco["123"]["vault"] += 3

        self.assertEqual(
            saves,
            [("banco_vct.json", {"123": {"balance": 7, "vault": 3}})],
        )
        self.assertIsNot(saves[0][1], bot.banco)


if __name__ == "__main__":
    unittest.main()
