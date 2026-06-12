# Auditor Bancario VCT — Pack de plantillas comerciales

**Versión de referencia:** 2.9.7  
**Documento público** — escaparate y catálogo (sin código operativo)

---

## ¿Qué problema resuelven estas plantillas?

Montar un **simulador económico en Discord** para una comunidad de Farming Simulator 22 (o rol similar) lleva meses: impuestos, nóminas, dinero negro, tiendas, arrestos, certificación FS22, monetización…

El **Pack de Plantillas Comerciales VCT** no es un bot listo para copiar y pegar en público: es un **kit profesional** para quien quiera:

- Lanzar su propio auditor / banco virtual en Discord.
- Vender servicios white-label a otras comunidades.
- Estructurar Patreon o Ko-fi con entregables técnicos reales.

Las plantillas cubren los **patrones que ya funcionan en producción** en Vanilla Center Trust: economía dual, locks anti-fraude, tiendas persistentes, SKU Discord, webhooks Ko-fi y despliegue VPS.

---

## Qué incluye el pack (beneficios)

| Área | Qué obtienes |
|------|----------------|
| **Economía** | Tasas, impuestos, cooldowns y catálogos configurables |
| **Comandos slash** | Plantilla con validación, cooldown y persistencia JSON |
| **Tiendas** | Menús persistentes Discord (legal / especial / socio) |
| **Monetización** | Integración SKU Discord + webhook Ko-fi → roles |
| **Automatización** | Tareas horarias (backup, impuestos, caducidades) |
| **Comercial** | Fichas Patreon, README cliente, checklist white-label |
| **Legal** | Cabecera de licencia (1 servidor / sin reventa) |

### Ventajas frente a empezar de cero

- **Menos errores económicos** — patrones probados (lock de banco, guards de arresto).
- **Time-to-market** — semanas en lugar de meses.
- **Vendible** — documentación lista para tiers de pago.
- **Escalable** — modular como el Auditor Bancario real (~90 comandos).

---

## Vista previa (ejemplos ficticios, no operativos)

Así *podría* verse una constante de tu servidor — **valores de ejemplo**:

```python
IMPUESTO_TRANSACCION = 0.05   # tu servidor decide el %
NOMINA_JORNALERO = 2_500      # placeholder
```

Un comando slash **genérico** (sin lógica real):

```python
@tree.command(name="mi_accion")
async def mi_accion(interaction, cantidad: int):
  # validar saldo → mutar → guardar
  await interaction.response.send_message("OK")
```

Una tienda persistente **solo como concepto**:

```python
class MiTienda(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)  # sobrevive reinicios
```

> El código **completo, comentado y enlazado** al ecosistema VCT (config real, SKU, Ko-fi, checklist de entrega) **no está en este documento público**.

---

## Para quién es

- Administradores de servidores FS22 / rol que quieren monetizar su comunidad.
- Desarrolladores Python que venden bots a medida.
- Creadores de contenido con Patreon técnico.
- Comunidades que ya usan el Auditor VCT y quieren **replicar o personalizar** el modelo.

---

## Tiers orientativos (modelo VCT)

| Nivel | Contenido | Canal |
|-------|-----------|-------|
| Gratuito | Este escaparate + informes jugador en GitHub | Repo público |
| Ciudadano | Informe de código + ejemplos depurados | Ko-fi / Discord |
| Socio Preferente | **Pack plantillas completo** + soporte | Ko-fi tier alto |
| Patreon técnico | Plantillas + informe privado + actualizaciones | Patreon |
| White-label | Código + despliegue + licencia | Bajo consulta |

---

## Contenido exclusivo de pago (resumen)

Al suscribirte desbloqueas **archivos listos para usar**, entre otros:

1. Configuración de economía exportable  
2. Plantilla de slash command con validación  
3. Tienda persistente con Select  
4. Sincronización SKU Discord (Socio / suscripción)  
5. Webhook Ko-fi → roles  
6. Tarea automática horaria  
7. Fichas de producto Patreon y README comercial  
8. Checklist de entrega white-label  

*(Listado orientativo; el pack puede actualizarse con cada versión del Auditor.)*

---

## Call to Action — desbloquea el pack completo

El **código fuente operativo de las plantillas** es un beneficio **exclusivo para mecenas y socios**. No se publica en el repositorio público de GitHub.

### Suscríbete o apoya el proyecto

- **Patreon (informe técnico + plantillas):**  
  https://www.patreon.com/calero89

- **Ko-fi (Socio Preferente / plantillas comerciales):**  
  https://ko-fi.com/calero89

- **Discord VCT** — tras suscribirte, abre ticket o escribe a staff para recibir el zip / acceso al repo privado de plantillas.

---

## Preguntas frecuentes

**¿Es el bot completo del Auditor?**  
No. Este pack son **plantillas y patrones**. El bot de producción VCT permanece en repositorio privado.

**¿Puedo revender el bot a otros servidores?**  
Solo con licencia white-label acordada. La plantilla de licencia incluida en el pack limita a **un servidor** salvo contrato.

**¿Necesito VPS?**  
Recomendado para 24/7. Las plantillas incluyen referencias a despliegue systemd (detalle en tier de pago).

---

© Vanilla Center Trust [VCT] · Catálogo público de plantillas · v2.9.7  
*Proyecto de fan / comunidad. No afiliado a GIANTS Software ni Discord Inc.*
