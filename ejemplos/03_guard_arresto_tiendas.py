"""
Guard reutilizable: impide usar tiendas (botones/menús) si el ciudadano está arrestado.
Patrón usado en tienda legal y tienda especial (v2.9.4).
"""
from __future__ import annotations

import discord


MENSAJE_BLOQUEO_ARRESTO = (
    "⛓️ Estás arrestado. Completa los trabajos comunitarios antes de usar la tienda."
)


def esta_arrestado(datos_cuenta: dict) -> bool:
    return int(datos_cuenta.get("arresto_trabajos_pendientes", 0)) > 0


async def bloquear_si_arrestado(interaction: discord.Interaction, banco: dict) -> bool:
    """True si el usuario está arrestado (mensaje ephemeral ya enviado)."""
    if interaction.user.bot:
        return False
    uid = str(interaction.user.id)
    if uid not in banco or not esta_arrestado(banco[uid]):
        return False
    try:
        if interaction.response.is_done():
            await interaction.followup.send(MENSAJE_BLOQUEO_ARRESTO, ephemeral=True)
        else:
            await interaction.response.send_message(MENSAJE_BLOQUEO_ARRESTO, ephemeral=True)
    except discord.HTTPException:
        pass
    return True
