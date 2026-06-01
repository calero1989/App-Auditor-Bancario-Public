# 📢 Actualización Auditor Bancario VCT 2.1.0 — Trabajos en el mapa (sin mods)

**Vanilla Center Trust [VCT]** · Mayo 2026

---

## ¿Qué es esta actualización?

El Auditor pasa a la versión **2.1.0**. El objetivo es **reducir la carga del staff** cuando las granjas están activas, **sin mods** y **sin instalar el juego en el PC**.

El bot **no puede ver el mapa de FS22** (Luna, vanilla, etc.). Por eso el sistema oficial es:

> **En VCT solo existe lo que queda registrado en Discord.**

Cada trabajo en el mapa debe **declararse** y un encargado lo **aprueba**; entonces el bot paga, guarda el historial y publica el recibo.

---

## Empresa multigranja — sectores

La empresa VCT se organiza por **granjas / sectores**:

| Sector | Roles típicos |
|--------|----------------|
| 🏛️ **Banco / Central** | Dueño, Encargado, Peón, Jornaleros |
| 🐄 **Ganadería** | Dueño, Encargado, Peón, Jornaleros |
| 🌽 **Agricultura** | Dueño, Encargado, Peón, Jornaleros |
| 🌲 **Silvicultura** | Dueño, Encargado, Peón, Jornaleros |

Cada registro de trabajo lleva **sector** y **terreno**, para saber **qué pasó en el mapa** aunque no estuviera staff conectado.

---

## Comandos nuevos

### Para todos los trabajadores

| Comando | Uso |
|---------|-----|
| `/vincular_fs22` | **Obligatorio una vez** — enlaza tu nombre de jugador FS22 con Discord |
| `/declarar_trabajo_fs22` | Tras trabajar en el mapa: sector, terreno, tipo de trabajo |
| `/que_paso` | Ver qué se ha hecho (últimos días), por sector o todo el mapa |
| `/version` o `/novedades` | Ver versión del bot e historial de cambios |

### Para Dueños, Encargados y administración

| Comando | Uso |
|---------|-----|
| `/pendientes_fs22` | Ver cola de trabajos por aprobar |
| `/aprobar_trabajo_fs22` | Aprobar por ID (ej. `P-00012`) → **pago automático** |
| `/rechazar_trabajo_fs22` | Rechazar declaración falsa o incorrecta |
| `/registrar_contrato_fs22` | Registro **completo al instante** (varios trabajos, ayudantes, etc.) |

---

## Cómo debe actuar cada uno

### 🧤 Jornaleros y peones

1. Antes de cobrar por trabajos FS22: **`/vincular_fs22`** con tu nick del juego.
2. Cuando termines un trabajo en el mapa (cosecha, transporte, etc.):
   - Usa **`/declarar_trabajo_fs22`**
   - Elige **sector**, **terreno** y **tipo de trabajo**
3. Guarda el **ID** que te devuelve el bot (ej. `P-00015`).
4. **No cobras hasta que un encargado apruebe** — el pago lo hace el bot al aprobar.
5. Si entras al servidor y quieres ponerte al día: **`/que_paso`**.

**No hace falta** que el staff esté en el mapa contigo; hace falta que **declares** en Discord.

---

### 👔 Encargados y dueños de sector

1. Revisa el canal de **registro de contratos FS22** o usa **`/pendientes_fs22`** (puedes filtrar por sector).
2. Comprueba que el trabajo es real (terreno, persona, tipo).
3. Si es correcto: **`/aprobar_trabajo_fs22`** con el ID → el bot paga y manda recibo.
4. Si es falso o incompleto: **`/rechazar_trabajo_fs22`** con motivo breve.
5. Contratos grandes (varios trabajos, varios ayudantes, plus de cooperación): sigue **`/registrar_contrato_fs22`**.

**No necesitas estar 24 h en el juego** — revisas la cola cuando puedas (unos minutos).

---

### 🔱 Fundación / administración

- Misma función de aprobar/rechazar que encargados.
- **`/registrar_contrato_fs22`** para casos especiales o pagos inmediatos.
- **`/que_paso`** para informar a quien entra al servidor.
- El resto del Auditor (banco, nóminas, impuestos, mercado negro, etc.) **no cambia**.

---

## Flujo en 3 pasos (resumen)

```
1. Trabajo en el mapa (FS22 / Luna)
        ↓
2. Jugador: /declarar_trabajo_fs22  →  Pendiente (ID)
        ↓
3. Encargado: /aprobar_trabajo_fs22  →  Pago + historial + aviso en canales
```

---

## Reglas importantes

- **Máximo 5 declaraciones pendientes** por persona — declara y espera aprobación.
- **Mentir o abusar** del sistema puede tratarse como infracción (antecedentes / sanciones admin).
- Lo **no declarado** no existe para el banco VCT.
- Los **ayudantes** y trabajos múltiples en un solo registro siguen yendo por **`/registrar_contrato_fs22`** (staff).

---

## Preguntas frecuentes

**¿El bot ve automáticamente lo que hago en Luna?**  
No. Vanilla + Luna no permiten eso. Por eso existe la declaración.

**¿Tengo que instalar FS22 en el PC?**  
No. Declaras desde Discord después de jugar.

**¿Puedo cobrar nómina (`/cobrar`) y declarar trabajos?**  
Sí. Son cosas distintas: nómina por **rol Discord**; trabajos FS22 por **declaración + aprobación**.

**¿Dónde veo la versión del bot?**  
`/version` — actualmente **2.1.0**.

---

*Auditor Bancario VCT — proyecto y marca Vanilla Center Trust [VCT].*
