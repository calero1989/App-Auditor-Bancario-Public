# 📢 Actualización Auditor Bancario VCT 2.4.0 — Tienda legal del Banco VCT

**Vanilla Center Trust [VCT]** · Mayo 2026

---

## ¿Qué es esta actualización?

El Auditor pasa a la versión **2.4.0**. Se abre la **tienda legal del Banco VCT**: un catálogo de **inversiones, seguros, licencias y coleccionables** que se pagan con **dinero limpio** (tu **cartera** en `/bal`), no con dinero negro.

Complementa la tienda especial (`/tienda_especial_vct`), que sigue usando **fondos no declarados**.

---

## Comandos nuevos

| Comando | Uso |
|---------|-----|
| `/tienda_legal_vct` | Ver el índice de paquetes o el catálogo de uno |
| `/comprar_legal_vct` | Comprar un producto (clave del catálogo) |
| `/inventario_legal_vct` | Ver productos, buffs e inversiones activas |
| `/cobrar_inversion_vct` | Cobrar depósitos a plazo vencidos y bonus de cooperativa |
| `/usar_legal_vct` | Usar informe del Auditor o bono de reputación trabajador |

**Consulta también:** `/version` · `/novedades` · `/bal` (ahora muestra títulos de inversor si los tienes)

---

## Los 5 paquetes (resumen)

### 🏦 1. Inversiones financieras (Banco VCT)

| Producto | Precio | Qué hace |
|----------|--------|----------|
| **Depósito a plazo 7 días** | 50.000 – 500.000 € (tú eliges) | Inviertes cartera 7 días; al vencer **+10 %** (cobras con `/cobrar_inversion_vct`) |
| **Bonos del Fondo Central** | 100.000 € | **4 cupones** de 5.000 € (se abonan en el ciclo semanal del lunes) |
| **Cuenta premium bancaria** | 25.000 € | **30 días:** impuesto de transferencias **3 %** (en lugar de 5 %) y **+5 %** en `/trabajo_rapido` |
| **Seguro de cosecha** | 15.000 € | **1 uso:** si pierdes en dados, tragaperras, rasca o casino, recuperas **50 %** de la pérdida (máx. 5.000 €) |

### 🚜 2. Inversiones agrícolas / FS22

| Producto | Precio | Qué hace |
|----------|--------|----------|
| **Semillas certificadas VCT** | 10.000 € | Próximo trabajo FS22 de cosecha/siembra/transporte: **+10 %** neto |
| **Contrato de maquinaria** | 30.000 € | **3 trabajos** FS22 (transporte/cosecha): **+2.000 €** extra en cada uno |
| **Cooperativa agrícola** | 75.000 € | **14 días:** si te aprueban **5+ trabajos**, bonus **20.000 €** (cobro con `/cobrar_inversion_vct`) |
| **Póliza multigranja** | 20.000 € | **1 uso:** si un trabajo tuyo es **rechazado**, **+2 reputación trabajador** |

### 🏪 3. Negocio / equipamiento

| Producto | Precio | Qué hace |
|----------|--------|----------|
| **Puesto en mercado semanal** | 40.000 € | Cada **lunes**, ingreso aleatorio **2.000 – 6.000 €** en cartera |
| **Licencia de comercio** | 60.000 € | **30 días:** marca de comerciante activo (visible en inventario y `/bal`) |
| **Almacén refrigerado** | 35.000 € | **30 días:** **+3 %** extra al cobrar depósitos a plazo |
| **Certificado de inversor VCT** | 50.000 € | Permite depósitos hasta **500.000 €** y título en `/bal` |

### 📦 4. Consumibles legales

| Producto | Precio | Qué hace |
|----------|--------|----------|
| **Combustible agrícola** | 3.000 € | **+15 %** en el próximo `/trabajo_rapido` |
| **Informe del Auditor** | 8.000 € | Resumen de actividad del servidor (sin saldos ajenos) — `/usar_legal_vct` |
| **Asesoría fiscal VCT** | 12.000 € | Próximo **impuesto semanal:** **-20 %** (tope 10.000 € de ahorro) |
| **Bono reputación trabajador** | 5.000 € | **+3 rep. trabajador** (máx. 1 cada 7 días) — `/usar_legal_vct` |

### 🏅 5. Coleccionables / largo plazo

| Producto | Precio | Qué hace |
|----------|--------|----------|
| **Acción VCT — Bronce** | 25.000 € | Título inversor bronce en `/bal` |
| **Acción VCT — Plata** | 100.000 € | Sustituye bronce; **+5 %** en pagos FS22 certificados |
| **Acción VCT — Oro** | 500.000 € | Sustituye plata; **+10 %** en pagos FS22 certificados |
| **Terreno simbólico VCT** | 150.000 € | Prestigio / registro en tu perfil de inversor |

---

## Cómo comprar (ejemplos)

1. Abre el catálogo: `/tienda_legal_vct` o `/tienda_legal_vct paquete:financiero`
2. Compra con la **clave** del producto:

```
/comprar_legal_vct producto:combustible_agricola
/comprar_legal_vct producto:deposito_plazo_7d importe:100000
/comprar_legal_vct producto:semillas_certificadas
```

3. Revisa lo activo: `/inventario_legal_vct`
4. Cuando venza un depósito o la cooperativa: `/cobrar_inversion_vct`

---

## Bonos automáticos (sin comando extra)

- **Trabajos FS22 pagados:** se aplican semillas, maquinaria y acciones plata/oro en el recibo.
- **Trabajo rechazado:** la póliza multigranja suma reputación si la tenías.
- **Transferencias:** cuenta premium reduce el impuesto al **3 %**.
- **Juegos (pérdida):** el seguro de cosecha devuelve parte del dinero.
- **Lunes (mantenimiento del bot):** bonos del fondo central, puesto de mercado e impuesto semanal (con asesoría fiscal si la compraste).

El dinero de las compras legales ingresa al **Fondo Central VCT** (como otras tasas del servidor).

---

## Diferencia con otras tiendas

| | Tienda legal | Tienda especial |
|---|--------------|-----------------|
| Comando | `/tienda_legal_vct` | `/tienda_especial_vct` |
| Moneda | **Cartera legal** (`balance`) | **Dinero negro** |
| Enfoque | Inversiones, FS22, negocio, seguros | Sobornos, guante blanco, items ocultos |
| Socio Discord | No obligatorio | Puede requerir Socio VCT / preferente |

La suscripción **⭐ Socio VCT** (~5 €/mes en Discord) **no sustituye** la tienda legal: son sistemas distintos.

---

## Preguntas frecuentes

**¿Puedo tener cartera negativa y comprar?**  
No. Necesitas saldo suficiente en **cartera legal** al comprar.

**¿El depósito a plazo se pierde si no cobro?**  
No desaparece; queda en tu inventario hasta que uses `/cobrar_inversion_vct` tras la fecha de vencimiento.

**¿Los bonos FS22 se acumulan con varios productos?**  
Sí, si cumples condiciones (por ejemplo semillas + contrato maquinaria en el mismo pago).

**¿Dónde veo mi versión?**  
`/version` — **2.4.0**.

---

## Mensaje para copiar en Discord (`/anuncio` — descripción del embed)

Pega el bloque siguiente en el formulario de `/anuncio` (título sugerido: **Actualización 2.4.0 — Tienda legal Banco VCT**):

```
🏛️ NUEVA TIENDA LEGAL — AUDITOR VCT 2.4.0

Invierte y compra productos legales con tu CARTERA (dinero limpio en /bal).

📌 COMANDOS
• /tienda_legal_vct — catálogo (5 paquetes)
• /comprar_legal_vct — comprar producto
• /inventario_legal_vct — lo que tienes activo
• /cobrar_inversion_vct — depósitos vencidos y bonus cooperativa
• /usar_legal_vct — informe Auditor o bono reputación

📦 PAQUETES
1️⃣ Financiero — depósito 7d (+10%), bonos FC, cuenta premium, seguro juegos
2️⃣ Agrícola/FS22 — semillas +10%, maquinaria +2k, cooperativa 20k, póliza rechazo
3️⃣ Negocio — puesto mercado (lunes), licencia, almacén, certificado inversor
4️⃣ Consumibles — combustible trabajo rápido, informe, asesoría fiscal, bono rep.
5️⃣ Coleccionables — acciones bronce/plata/oro, terreno simbólico

💡 EJEMPLO: /comprar_legal_vct producto:deposito_plazo_7d importe:100000

La tienda especial (/tienda_especial_vct) sigue siendo con dinero negro.

Versión: /version · /novedades

— Vanilla Center Trust [VCT]
```

---

*Auditor Bancario VCT — proyecto y marca Vanilla Center Trust [VCT].*
