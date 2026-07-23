"""
Escritura atómica de JSON (versión didáctica pública).

Producción (`vct_auditor/storage.py`) añade además:
- carpeta destino si no existe
- copia de seguridad `.ultimo_ok` antes de reemplazar
- reintentos ante PermissionError (Windows)
"""
from __future__ import annotations

import json
import os
import time


def guardar_json_atomico(ruta: str, datos) -> None:
    """Escribe `datos` en `ruta` vía fichero temporal + replace + fsync."""
    temporal = f"{ruta}.{os.getpid()}.{time.time_ns()}.tmp"
    try:
        with open(temporal, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
            f.flush()
            os.fsync(f.fileno())
        os.replace(temporal, ruta)  # Atómico en POSIX/Windows
    finally:
        if os.path.exists(temporal):
            try:
                os.remove(temporal)
            except OSError:
                pass
