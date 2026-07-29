import os
import runpy
import unittest
from pathlib import Path
from unittest.mock import patch


CONFIG_EXAMPLE = Path(__file__).resolve().parents[1] / "ejemplos" / "02_carga_variables_entorno.py"


class EnvConfigTests(unittest.TestCase):
    def test_discord_sku_is_int_for_entitlement_comparisons(self) -> None:
        sku_id = "123456789012345678"
        with patch.dict(os.environ, {"DISCORD_SKU_SOCIO_VCT_ID": sku_id}, clear=False):
            config = runpy.run_path(CONFIG_EXAMPLE)

        self.assertEqual(config["DISCORD_SKU_SOCIO_VCT_ID"], int(sku_id))
        self.assertIs(type(config["DISCORD_SKU_SOCIO_VCT_ID"]), int)


if __name__ == "__main__":
    unittest.main()
