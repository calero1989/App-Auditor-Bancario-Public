"""
Carga de configuración desde variables de entorno o kofi.env (ilustrativo).
Los valores reales nunca se suben al repositorio público.
"""
from __future__ import annotations

import os


def _cargar_variable_env(nombre: str, predeterminado: str = "") -> str:
    valor = os.getenv(nombre)
    if valor is not None and valor.strip():
        return valor.strip()
    ruta_env = os.path.join(os.path.dirname(__file__), "..", "kofi.env")
    if os.path.exists(ruta_env):
        with open(ruta_env, encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea or linea.startswith("#") or "=" not in linea:
                    continue
                clave, _, texto = linea.partition("=")
                clave = clave.strip()
                if clave.startswith("export "):
                    clave = clave.removeprefix("export ").strip()
                if clave == nombre:
                    return texto.strip().strip('"').strip("'")
    return predeterminado


def _cargar_entero_env(nombre: str, predeterminado: int = 0) -> int:
    texto = _cargar_variable_env(nombre, str(predeterminado)).strip()
    if not texto:
        return predeterminado
    try:
        return int(texto)
    except ValueError as exc:
        raise ValueError(f"{nombre} debe ser un entero, recibido: {texto!r}") from exc


# Placeholders: en producción se leen de kofi.env o del entorno del servidor
DISCORD_BOT_TOKEN = _cargar_variable_env("DISCORD_BOT_TOKEN")
DISCORD_GUILD_ID = _cargar_entero_env("DISCORD_GUILD_ID", 0)
KO_FI_VERIFICATION_TOKEN = _cargar_variable_env("KOFI_VERIFICATION_TOKEN")
KO_FI_WEBHOOK_PORT = _cargar_entero_env("KO_FI_WEBHOOK_PORT", 8080)
# sku_id de Discord llega como int en entitlements; comparar como int
DISCORD_SKU_SOCIO_VCT_ID = _cargar_entero_env("DISCORD_SKU_SOCIO_VCT_ID", 0)
DISCORD_APPLICATION_ID = _cargar_entero_env("DISCORD_APPLICATION_ID", 0)
