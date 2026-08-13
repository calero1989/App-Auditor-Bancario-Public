"""
Carga de configuración desde variables de entorno o kofi.env (ilustrativo).
Los valores reales nunca se suben al repositorio público.
"""
from __future__ import annotations

import os


def _valor_proceso_definido(valor: str | None) -> str | None:
    """None / vacío / solo espacios → no definido (permite caer a kofi.env)."""
    if valor is None:
        return None
    limpio = valor.strip()
    return limpio if limpio else None


def _clave_linea_env(clave: str) -> str:
    """Acepta `KEY` y `export KEY` (estilo shell)."""
    clave = clave.strip()
    if clave.startswith("export ") or clave.startswith("export\t"):
        clave = clave.split(None, 1)[1] if len(clave.split(None, 1)) > 1 else ""
    return clave.strip()


def _cargar_variable_env(nombre: str, predeterminado: str = "") -> str:
    valor = _valor_proceso_definido(os.getenv(nombre))
    if valor is not None:
        return valor
    ruta_env = os.path.join(os.path.dirname(__file__), "..", "kofi.env")
    if os.path.exists(ruta_env):
        with open(ruta_env, encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea or linea.startswith("#") or "=" not in linea:
                    continue
                clave, _, texto = linea.partition("=")
                if _clave_linea_env(clave) == nombre:
                    return texto.strip().strip('"').strip("'")
    return predeterminado


# Placeholders: en producción se leen de kofi.env o del entorno del VPS
DISCORD_BOT_TOKEN = _cargar_variable_env("DISCORD_BOT_TOKEN")
DISCORD_GUILD_ID = int(_cargar_variable_env("DISCORD_GUILD_ID", "0") or "0")
KO_FI_VERIFICATION_TOKEN = _cargar_variable_env("KOFI_VERIFICATION_TOKEN")
KO_FI_WEBHOOK_PORT = int(_cargar_variable_env("KO_FI_WEBHOOK_PORT", "8080") or "8080")
DISCORD_SKU_SOCIO_VCT_ID = _cargar_variable_env("DISCORD_SKU_SOCIO_VCT_ID")
DISCORD_APPLICATION_ID = _cargar_variable_env("DISCORD_APPLICATION_ID", "0")
