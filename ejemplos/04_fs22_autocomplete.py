"""
Autocompletado de tipos de trabajo FS22 y registro de comando slash.
Discord limita a 25 opciones: se filtra por búsqueda y se priorizan trabajos nuevos.
"""
from __future__ import annotations

import unicodedata

import discord
from discord import app_commands

TRABAJOS_FS22 = {
    "cosecha": "Cosecha",
    "hilerar": "Hilerar",
    "plantar": "Plantar",
    "labrar": "Labrar",
}

NUEVOS_TRABAJOS_FS22 = frozenset({"hilerar", "plantar", "labrar"})


def _normalizar(texto: str) -> str:
    texto = unicodedata.normalize("NFD", (texto or "").lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def choices_autocomplete_trabajos_fs22(current: str) -> list[tuple[str, str]]:
    busqueda = _normalizar(current.strip())
    items = list(TRABAJOS_FS22.items())
    if busqueda:
        candidatos = [
            (clave, nombre)
            for clave, nombre in items
            if busqueda in _normalizar(nombre)
            or busqueda in _normalizar(clave.replace("_", " "))
        ]
        candidatos.sort(key=lambda par: par[1].lower())
    else:
        nuevos = sorted(
            (p for p in items if p[0] in NUEVOS_TRABAJOS_FS22),
            key=lambda par: par[1].lower(),
        )
        resto = sorted(
            (p for p in items if p[0] not in NUEVOS_TRABAJOS_FS22),
            key=lambda par: par[1].lower(),
        )
        candidatos = nuevos + resto
    return candidatos[:25]


async def _autocomplete_tipo_fs22(
    interaction: discord.Interaction,
    current: str,
) -> list[app_commands.Choice[str]]:
    return [
        app_commands.Choice(name=nombre[:100], value=clave)
        for clave, nombre in choices_autocomplete_trabajos_fs22(current)
    ]


def registrar_comando_fs22(tree: app_commands.CommandTree) -> None:
    # @tree.command debe ir ANTES de @autocomplete (orden correcto en discord.py)
    @tree.command(name="registrar_contrato_fs22", description="Registrar contrato FS22")
    @app_commands.describe(tipo="Escribe para buscar: Hilerar, Plantar…")
    @app_commands.autocomplete(tipo=_autocomplete_tipo_fs22)
    async def registrar_contrato_fs22(interaction: discord.Interaction, tipo: str):
        clave = tipo if tipo in TRABAJOS_FS22 else None
        await interaction.response.send_message(
            f"Trabajo registrado: **{TRABAJOS_FS22.get(clave, tipo)}**",
            ephemeral=True,
        )
