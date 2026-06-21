# 📢 Actualización Auditor Bancario VCT 2.5.0 — Alijo NRD (ocultación de fondos)

**Vanilla Center Trust [VCT]** · Junio 2026

**Autor:** Angel del Valle Calero (calero89) · © 2026

---

## ¿Qué es esta actualización?

El Auditor pasa a la versión **2.5.0**. Se añade el **alijo NRD**: un sistema para **esconder fondos no declarados** fuera del saldo visible del banco, tras comprar el **Maletín offshore VCT** en la tienda especial.

No sustituye a `/blanquear_fondos` (legalizar) ni a la tienda legal (`/tienda_legal_vct`). Es una capa extra de **riesgo/recompensa** en el submundo económico VCT.

> **Importante:** El staff **no ve** el alijo en `/admin_saldos`. Solo puede incautarlo con **`/admin_incautar_alijo`** (inspección profunda). El NRD **visible** sigue pudiendo retirarse con `/admin_retirar_nrd`.

---

## Resumen rápido

| Concepto | Detalle |
|----------|---------|
| Desbloqueo | **Maletín offshore VCT** en `/tienda_especial_vct` — **150.000 €** en NRD |
| Ocultar | `/ocultar_nrd` — comisión **30 %** (va al Fondo Central) |
| Recuperar | `/recuperar_nrd` — del alijo al NRD visible |
| Tope del alijo | **1.000.000.000 €** (1 billón) |
| Aviso | **DM a los 5 días** sin mover NRD visible ni alijo |
| Incautación automática | **Día 7** sin movimiento (visible y/o alijo) |
| Versión | `/version` · `/novedades` |

---

## Paso 1 — Comprar el maletín (obligatorio)

En **`/tienda_especial_vct`** elige:

**Maletín offshore VCT — desbloquea alijo (150.000 € negro)**

- Pago con **dinero negro** (NRD visible).
- Desbloqueo **permanente** en tu cuenta.
- Sin maletín **no** puedes usar `/ocultar_nrd` ni `/recuperar_nrd`.

Tras la compra verás el estado en **`/alijo_vct`** y en **`/inventario_vct`** (sección alijo).

---

## Paso 2 — Comandos del jugador

| Comando | Descripción |
|---------|-------------|
| `/alijo_vct` | Capacidad libre, saldo en alijo, plazos de inactividad, NRD visible |
| `/ocultar_nrd` | Mueves NRD **visible** al alijo (parámetro `monto`) |
| `/recuperar_nrd` | Sacas NRD del alijo al saldo visible (`monto` opcional; vacío = todo) |
| `/inventario_vct` | Items de tienda especial + resumen del alijo si está desbloqueado |
| `/bal` | Indica si tienes alijo activo (el importe oculto solo en `/alijo_vct`) |

### Cómo funciona `/ocultar_nrd`

1. Tienes NRD en la cartera (campo **Dinero negro** de `/bal`).
2. Ejecutas `/ocultar_nrd monto:100000` (ejemplo).
3. Se descuenta **100.000 €** del NRD visible.
4. **Comisión 30 %** → **30.000 €** al Fondo Central VCT.
5. Entran **70.000 €** en el **alijo** (hasta el tope de 1 billón en total en alijo).

**Fórmula:** `alijo += monto × (1 − 0,30)`

### Cómo funciona `/recuperar_nrd`

- Sin comisión extra al sacar del alijo.
- El dinero vuelve al **NRD visible** (cuenta en `/bal`).
- Reinicia el plazo de los **7 días** sobre ese saldo visible.

---

## Qué ve (y qué no ve) cada uno

| Quién | NRD visible (`/bal`, `/admin_saldos`) | Alijo oculto |
|-------|--------------------------------------|--------------|
| **Tú** | Sí | Sí, en `/alijo_vct` |
| **Staff rutina** (`/admin_saldos`, `/admin_retirar_nrd`) | Sí | **No** |
| **Staff inspección** (`/admin_incautar_alijo`) | Sí | **Sí** (forzado) |

---

## Plazos: aviso e incautación automática

Aplica por separado al **NRD visible** y al **alijo**:

| Días sin movimiento | Efecto |
|---------------------|--------|
| **5** | **Mensaje privado (DM)** del bot: aviso de riesgo |
| **7** | **Incautación automática** de ese saldo + registro en antecedentes + aviso en canal de trámites |

**Cuenta como movimiento** (reinicia el plazo), entre otros:

- `/ocultar_nrd` · `/recuperar_nrd`
- `/blanquear_fondos` · `/entregar_efectivo`
- `/robar` (ganancia en negro) · `/mini_trabajos_ocultos`
- Compras en `/tienda_especial_vct` pagadas con NRD
- Cualquier cambio en tu NRD visible o en el alijo

**No cuenta:** solo mirar `/bal` o `/alijo_vct` sin mover fondos.

---

## Comandos de administración (staff)

| Comando | Uso |
|---------|-----|
| `/admin_retirar_nrd` | Retira NRD **visible** (como hasta ahora) |
| `/admin_incautar_alijo` | **Inspección profunda** — incauta el alijo (monto opcional; vacío = todo el alijo) |
| `/admin_saldos` | **No** incluye el alijo; solo NRD visible por ciudadano |

La incautación por alijo genera registro de antecedentes y puede ingresar al Fondo Central según la operación administrativa.

---

## Ejemplo completo

1. Tienes **200.000 €** en dinero negro (visible).
2. Compras el maletín: **−150.000 €** → quedan **50.000 €** visibles.
3. `/ocultar_nrd monto:50000` → comisión **15.000 €** → **35.000 €** al alijo · **0 €** visible.
4. Un inspector usa `/admin_retirar_nrd` → **0 €** (no ve el alijo).
5. Si nadie usa `/admin_incautar_alijo` y no mueves fondos **7 días** → el sistema vacía alijo y/o visible según corresponda.
6. `/recuperar_nrd` (sin monto) → todo el alijo vuelve a NRD visible para blanquear o gastar.

---

## Relación con otras tiendas VCT

| Sistema | Moneda | Comando principal |
|---------|--------|-------------------|
| **Alijo NRD** (2.5.0) | Dinero negro | `/tienda_especial_vct` → maletín → `/ocultar_nrd` |
| **Tienda especial** | Dinero negro | `/tienda_especial_vct` (guante, decodificador, sobornos…) |
| **Tienda legal** (2.4.0) | Cartera legal | `/tienda_legal_vct` · `/comprar_legal_vct` |
| **Legalizar** | Negro → limpio | `/blanquear_fondos` (comisión ~15 %) |

---

## Preguntas frecuentes

**¿El alijo evita el `/admin_retirar_nrd`?**  
Oculta fondos del saldo **visible**. El staff necesita **`/admin_incautar_alijo`** para el alijo.

**¿Puedo tener cartera legal y alijo a la vez?**  
Sí. Son sistemas distintos (cartera / NRD visible / alijo / caja fuerte).

**¿La comisión del 30 % se aplica al recuperar?**  
No. Solo al **ocultar** (`/ocultar_nrd`).

**¿Qué pasa si supero 1 billón en el alijo?**  
No puedes ocultar más hasta recuperar fondos o hasta que baje el saldo del alijo.

**¿El rol Ciudadano o Socio VCT desbloquea el alijo?**  
No. Solo el **Maletín offshore** en la tienda especial.

**¿Dónde veo la versión?**  
`/version` — actualmente **2.5.0**.

---

## Mensaje para copiar en Discord (`/anuncio`)

**Título sugerido:** `Actualización 2.5.0 — Alijo NRD (ocultar fondos no declarados)`

Pega el bloque siguiente en la descripción del formulario de `/anuncio`:

```
📢 ACTUALIZACIÓN AUDITOR VCT 2.5.0 — ALIJO NRD

🧳 NUEVO: esconde fondos no declarados fuera del saldo visible del banco.

1️⃣ Compra el Maletín offshore en /tienda_especial_vct (150.000 € negro)
2️⃣ /ocultar_nrd — guarda NRD en el alijo (comisión 30 % → Fondo Central)
3️⃣ /recuperar_nrd — saca dinero del alijo al saldo visible
4️⃣ /alijo_vct — consulta capacidad y plazos

📊 Límites
• Tope alijo: 1.000.000.000 €
• No aparece en /admin_saldos (solo inspección profunda)

⏱️ Plazos (visible Y alijo)
• 5 días sin mover → aviso por DM
• 7 días sin mover → incautación automática

👮 Staff
• /admin_retirar_nrd → solo NRD visible
• /admin_incautar_alijo → incautar el alijo (inspección profunda)

💡 Alternativas: /blanquear_fondos (legalizar) · /tienda_legal_vct (inversiones legales)

Versión: /version · /novedades

— Angel del Valle Calero · Vanilla Center Trust [VCT]
```

---

## Anexo — Otras novedades recientes (2.4.x)

Si aún no las anunciaste, conviene un segundo mensaje o ampliar el tablón:

| Versión | Tema | Comandos clave |
|---------|------|----------------|
| **2.4.0** | Tienda legal (5 paquetes, cartera legal) | `/tienda_legal_vct` · `/comprar_legal_vct` · `/inventario_legal_vct` · `/cobrar_inversion_vct` |
| **2.4.1** | Fix menú de compra legal | Lista fija en `/comprar_legal_vct` |
| **2.4.2** | Fix nómina varios roles | `/cobrar` reconoce más nombres de rol (🧤 Jornalero, Peón Agricultura…) |

Documento ampliado tienda legal: `ANUNCIO_ACTUALIZACION_2.4.0.md`

---

*© 2026 Angel del Valle Calero · Auditor Bancario VCT — proyecto y marca Vanilla Center Trust [VCT].*
