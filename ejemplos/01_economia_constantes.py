"""
Constantes de economía VCT (extracto ilustrativo).
Sin IDs de canales Discord ni rutas de despliegue.
"""
from __future__ import annotations

# --- Impuestos y comisiones ---
IMPUESTO_TRANSACCION = 0.05          # 5 % transferencias legales → fondo central
IMPUESTO_LAVADO = 0.15               # 15 % al blanquear NRD
IMPUESTO_SEMANAL = 0.20              # 20 % lunes sobre cartera legal
TRANSFERIR_NRD_COMISION = 0.20       # 20 % entre criminales
ALIJO_COMISION = 0.30                # 30 % al ocultar NRD en alijo

# --- Dinero negro visible ---
NEGRO_AVISO_DIAS = 5
NEGRO_CADUCIDAD_DIAS = 7
ALIJO_CADUCIDAD_AUTOMATICA = False    # el alijo no caduca solo

# --- Persecución y arresto (v2.9.x) ---
ROBO_EXITO_CHANCE = 0.50
ROBO_EXITO_CHANCE_CON_ALARMA = 0.25
COSTE_ALARMA_SEGURIDAD = 5_000
FIANZA_VCT = 100_000
TRABAJOS_ARRESTO_REQUERIDOS = 5

# --- Atraco planificado (resumen) ---
ATRACO_EXITO_CHANCE = 0.35
ATRACO_MIN_JUGADORES = 2
ATRACO_MAX_JUGADORES = 4
ATRACO_COOLDOWN_HORAS = 48

# --- Reputación por acción ---
REP_TRABAJO_FS22 = 10
REP_ROBAR_EXITO = 10
REP_LAVAR = -2

# --- Trabajos FS22: clave interna → nombre visible (extracto) ---
TRABAJOS_FS22 = {
    "cosecha": "Cosecha",
    "siembra": "Siembra",
    "hilerar": "Hilerar",
    "plantar": "Plantar",
    "labrar": "Labrar",
    "contrato_agricultura": "Contrato de agricultura",
}

PAGOS_TRABAJOS_FS22 = {
    "cosecha": 5000,
    "siembra": 5000,
    "hilerar": 4000,
    "plantar": 5000,
    "labrar": 5000,
    "contrato_agricultura": 12000,
}
