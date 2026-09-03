from __future__ import annotations

import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
ENV_EXAMPLE = ROOT / "kofi.env.example"


def _leer_variables_env_example() -> dict[str, str]:
    variables: dict[str, str] = {}
    for linea in ENV_EXAMPLE.read_text(encoding="utf-8").splitlines():
        linea = linea.strip()
        if not linea or linea.startswith("#") or "=" not in linea:
            continue
        clave, _, valor = linea.partition("=")
        variables[clave.strip()] = valor.strip()
    return variables


class KofiEnvExampleTests(unittest.TestCase):
    def test_discord_guild_id_es_placeholder_publico(self) -> None:
        variables = _leer_variables_env_example()
        self.assertEqual(variables["DISCORD_GUILD_ID"], "0")


if __name__ == "__main__":
    unittest.main()
