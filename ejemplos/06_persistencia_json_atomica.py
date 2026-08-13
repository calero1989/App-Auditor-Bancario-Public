"""
Escritura atómica de JSON (versión didáctica pública).

En producción se añade además: carpeta destino si no existe, copia `.ultimo_ok`
antes de reemplazar y reintentos ante PermissionError (Windows).
"""
from __future__ import annotations

import json
import os
import time


def _fsync_directorio(ruta: str) -> None:
    directorio = os.path.dirname(os.path.abspath(ruta)) or "."
    try:
        fd = os.open(directorio, os.O_RDONLY)
    except OSError:
        return
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def guardar_json_atomico(ruta: str, datos) -> None:
    """Escribe `datos` en `ruta` vía temporal + replace + fsync."""
    temporal = f"{ruta}.{os.getpid()}.{time.time_ns()}.tmp"
    temporal_completo = False
    try:
        with open(temporal, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
            f.flush()
            os.fsync(f.fileno())
        temporal_completo = True
        os.replace(temporal, ruta)  # Atómico en POSIX/Windows
        _fsync_directorio(ruta)
    except Exception:
        if not temporal_completo and os.path.exists(temporal):
            try:
                os.remove(temporal)
            except OSError:
                pass
        raise
