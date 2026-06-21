# Auditor Bancario VCT — Informe para NotebookLM (conocimiento del sistema)

**Proyecto:** Vanilla Center Trust [VCT]  
**Autor:** Angel del Valle Calero (calero89) · © 2026  
**Producto:** Auditor Bancario VCT (bot de economía y trámites en Discord)  
**Versión de referencia:** 2.12.0 (junio 2026)  
**Contexto:** Comunidad de rol vinculada a Farming Simulator 22  
**Idioma:** Español  

> Documento optimizado para **NotebookLM**: qué es el sistema, reglas para jugadores, economía, FS22, inactividad, niveles XP y comandos.  
> **No incluye** infraestructura, tokens, IPs, rutas de servidor ni secretos.

**Fuentes complementarias (URLs):**
- Post Patreon 2.12.0: https://www.patreon.com/calero89/posts/auditor-bancario-161084864  
- Historial completo MD: https://github.com/calero1989/App-Auditor-Bancario-Public/blob/main/informes/Historial_completo_v1_a_v2120.md  
- Repo docs público: https://github.com/calero1989/App-Auditor-Bancario-Public  

---

## 1. ¿Qué es el Auditor Bancario VCT?

Bot de Discord que centraliza **economía virtual**, **reputación**, **trámites**, **certificación FS22** y **progresión por niveles** en Vanilla Center Trust.

Cada ciudadano tiene cuenta bancaria (NRB), saldos, reputación dual, nivel XP y obligaciones. El bot **certifica** actividad declarada en Discord; no lee el juego FS22 directamente.

### Regla fundamental

> Lo hecho en el mapa FS22 **solo cuenta en la economía VCT** si se **declara o registra en Discord** (salvo registro inmediato por encargados/staff).

### Al unirse

- Rol **Ciudadano de VCT**
- **NRB** único generado automáticamente
- Cuenta en el banco del bot
- **Nivel XP inicial N0** (cuentas nuevas). Veteranos ya registrados antes de 2.12.0: **N15** automático

---

## 2. Economía: dinero, impuestos, reputación

### 2.1 Tres tipos de dinero

| Concepto | Campo bot | Descripción |
|----------|-----------|-------------|
| Cartera legal | balance | Dinero oficial; transferencias con 5 % al fondo central |
| Caja fuerte | vault | Ahorro; más protegido en atracos |
| Fondos no declarados | dinero_negro (NRD) | Ilegal; blanquear u ocultar en alijo |

### 2.2 Reputación dual (independiente del nivel XP)

- **rep_trabajador** — trabajos FS22, contratos, cooperación, auditoría voluntaria  
- **rep_criminal** — robos, extorsión, mercado negro, contrabando  

La **reputación** es perfil RP; el **nivel N/C** desbloquea **comandos**.

### 2.3 Impuestos y comisiones

| Operación | Tasa |
|-----------|------|
| Transferencia legal | 5 % fondo central |
| Blanquear NRD | 15 % |
| Impuesto semanal (lunes) | 20 % cartera legal |
| Transferir NRD a otro criminal | 20 % |
| Ocultar en alijo | 30 % |

### 2.4 Caducidad NRD visible

- Aviso ~5 días; **caduca a 7 días** si no se blanquea ni oculta  
- **Alijo** no caduca solo; incautación solo por admin  

### 2.5 Fondo central y tesorería

- **Fondo central:** impuestos y comisiones del ecosistema  
- **Tesorería VCT** (`/aportar_vct`): donación robable; no paga impuesto semanal  

---

## 3. Progresión XP y niveles (v2.12.0)

### 3.1 Dos barras de progresión

| Barra | Rango | Función |
|-------|-------|---------|
| **Nivel N** (trabajador) | 0–30 | Desbloquea economía legal, FS22, tienda legal, sociedad, casino |
| **Nivel C** (criminal) | 0–20 | Rama paralela: mercado negro, robos, extorsión, atracos |

Consulta: **`/nivel_vct`**. Comandos bloqueados muestran mensaje con nivel requerido.

### 3.2 Fuentes de XP (con topes diarios anti-farmeo)

| Fuente | XP aprox. | Rama |
|--------|-----------|------|
| Mensajes en Discord | +2 (tope/día) | Legal |
| Trabajo FS22 **aprobado** (no al declarar) | +120 | Legal |
| Cobrar nómina `/cobrar` | +15 | Legal |
| `/trabajo_rapido` | +25 | Legal |
| Auditoría voluntaria | +80 | Legal |
| Robo exitoso | +30 | Criminal |
| Mini trabajos ocultos | +20 | Criminal |
| Contrabando FS22 | +25 | Criminal |

**No se gana XP en cuarentena por inactividad.**

### 3.3 Hitos automáticos de rol Discord

| Nivel N | Efecto |
|---------|--------|
| **N5** | Rol **Jornalero** (si no tiene rol superior) |
| **N15** | Rol **Peón** (sector según perfil FS22) |
| **N30** | Elegible **`/postular_encargado`** → rol **Candidato Encargado** (staff confirma Encargado real) |

**Nómina `/cobrar`:** sigue dependiendo del **rol Discord remunerado**, no solo del nivel.

### 3.4 Comandos base N0 (cuenta nueva)

`/bal` · `/actividad_vct` · `/vincular_fs22` · `/declarar_trabajo_fs22` · `/version` · `/ticket` · `/tienda_vct` · `/nivel_vct`

### 3.5 Desbloqueos acumulativos por nivel N (resumen)

| Nivel | Nuevos comandos (ejemplos) |
|-------|----------------------------|
| N3 | `/reputacion`, `/cumpleanos`, `/trabajos_fs22` |
| N5 | `/depositar`, `/retirar`, `/cobrar`, `/perfil_fs22`, `/trabajo_rapido` |
| N6 | `/top_trabajadores` |
| N8 | `/transferencia`, `/pagar`, `/tienda_legal_vct` |
| N10 | `/mis_pendientes_vct`, `/antecedentes`, `/inventario_legal_vct` |
| N12 | `/comprar_legal_vct`, `/tesoreria_vct`, `/que_paso`, `/juegos` |
| N15 | `/prestamo_vct`, `/seguro_vct`, `/perseguir`, `/trabajos_comunitarios` |
| N18 | Contratos P2P, casino (`/rasca_vct`, `/dados`, etc.) |
| N20 | `/auditoria_voluntaria` |
| N25 | `/delatar` (+ permisos Fundador/Dueño/admin/Socio) |
| N30 | `/postular_encargado`, `/estado_postulacion_vct`, `/pendientes_fs22` (solo lectura) |

### 3.6 Rama criminal por nivel C

| Nivel C | Comandos |
|---------|----------|
| C5 | `/tienda_especial_vct`, `/inventario_vct` |
| C8 | `/alijo_vct`, `/ocultar_nrd`, `/mini_trabajos_ocultos` |
| C10 | `/robar`, `/blanquear_fondos` |
| C12 | `/desafio_criminal`, `/transferir_nrd` |
| C15 | `/extorsionar`, `/contrabando_fs22` |
| C18 | `/encargo_oscuro`, `/encargo_aceptar` |
| C20 | `/atraco_planificado`, `/atraco_responder` |

### 3.7 Comandos sin nivel (solo rol staff/granja)

`/registrar_contrato_fs22` · `/aceptar_trabajo_fs22` · `/rechazar_trabajo_fs22` · `/licencia_sector` · `/fondo_sector_gastar` · `/inspeccionar` · `/admin_*` · `/anuncio` · `/clear`

Encargados/Dueños de granja **bypass** comandos de su competencia FS22 aunque no tengan N30.

### 3.8 Postulación Encargado (N30)

1. Alcanzar **N30** sin bloqueo de ascenso por sanción  
2. `/postular_encargado` (sector: ganadería, agricultura o silvicultura)  
3. Rol **📋 | Candidato Encargado**  
4. Staff revisa; Encargado real es **cambio manual de rol**  
5. Inactividad fase 2+ cancela postulación  

Comandos: `/postular_encargado`, `/estado_postulacion_vct`, `/admin_nivel` (admin).

---

## 4. Inactividad (v2.10–2.11)

**Actividad válida:** mensajes en Discord **o** comandos del Auditor. Reinicia el plazo.

**Consulta:** `/actividad_vct` · Aviso **DM ~24 h** antes de cada fase.

**Exentos:** Fundador y administradores Discord.

### 4.1 Ciclo ciudadano (28 días)

Peones, Jornaleros y ciudadanos sin cargo de granja:

| Fase | Días sin actividad | Consecuencia |
|------|-------------------|--------------|
| 1 | 7 | Multa **50.000 €** |
| 2 | 14 | Despido rol **Peón** y/o **Jornalero** |
| 3 | 21 | Cese Jornalero **o cuarentena** (sin trámites ni tiendas) |
| 4 | 28 | Expulsión del servidor |

**Cuarentena (fase 3):** solo `/bal`, `/actividad_vct`, `/version`.

### 4.2 Ciclo granja / administración (40 días)

Solo **Encargados** y **Dueños** de ganadería, agricultura o silvicultura:

| Fase | Días | Consecuencia |
|------|------|--------------|
| 1 | 14 | Multa **100.000 €** |
| 2 | 21 | Destitución **Encargado** |
| 3 | 30 | Expropiación **Dueño** + intervención bancaria (industrias embargadas) |
| 4 | 40 | Expulsión |

**No aplica** a staff, moderación, soporte, supervisores banco, Dueño Banco ni Inversor (usan ciclo ciudadano si corresponde).

Fase 2 inactividad también aplica **bloqueo de ascenso XP 30 días** y cancela postulación Encargado.

---

## 5. Nóminas y roles Discord

`/cobrar` paga por cada rol remunerado fuera de cooldown:

| Rol | Pago orientativo | Cooldown |
|-----|------------------|----------|
| Fundador / Dueños sector | 50.000 € | 60 min |
| Supervisor / Inspector | 20.000 € | 60 min |
| Encargado sector | 10.000 € | 30 min |
| Peón sector | 5.000 € | 30 min |
| Jornalero | 2.500 € | 30 min |
| Inversor Banco | 100.000 € | 60 min |

Varios rangos → cobro acumulado en una nómina.

---

## 6. Farming Simulator 22

### 6.1 Sectores

Banco/Central · Ganadería · Agricultura · Silvicultura

### 6.2 Flujos de trabajo

**Jornalero (con aprobación):**
1. `/vincular_fs22` (obligatorio)
2. `/declarar_trabajo_fs22` → pendiente (ID P-xxxxx)
3. Staff: `/aceptar_trabajo_fs22` o `/rechazar_trabajo_fs22`
4. Al aceptar: pago neto, recibo, **+XP**, DM al trabajador

**Staff (inmediato):** `/registrar_contrato_fs22` — hasta 5 tipos + ayudantes (cooperación 10.000 € c/u).

### 6.3 Catálogo

36 tipos de trabajo; bruto ~3.000–15.000 €; neto −5 % impuesto. Lista: `/trabajos_fs22`.

### 6.4 Comandos FS22 útiles

`/perfil_fs22` · `/historial_fs22` · `/top_trabajadores` · `/que_paso` · `/pendientes_fs22` (staff o N30+ lectura)

---

## 7. Tienda legal

Paquetes: financiero, agrícola/FS22, negocio, consumible, coleccionable.

Producto destacado: **Alarma de seguridad** (5.000 €) — reduce éxito de robos; habilita `/perseguir`.

Comandos: `/tienda_legal_vct`, `/comprar_legal_vct`, `/inventario_legal_vct`, `/cobrar_inversion_vct`, `/usar_legal_vct`

Menús interactivos fijados en canal 🏪 tienda legal.

---

## 8. Mercado negro y alijo

Tienda especial (NRD): soborno, Guante Blanco, decodificador, maletín offshore.

Alijo requiere maletín; `/ocultar_nrd`, `/recuperar_nrd`, `/alijo_vct`.

Comandos: `/tienda_especial_vct`, `/inventario_vct`, etc.

---

## 9. Crimen, orden público y prisión

### Robo `/robar`
- Sin alarma: 50 % éxito · Con alarma: 25 %  
- Éxito → NRD al ladrón · Fallo → multa  

### Persecución `/perseguir`
- Víctima con alarma, ventana 24 h post-robo  
- Éxito → recuperación parcial, posible arresto  
- Seguro antirobo: hasta 70 % indemnización  

### Arresto
- Rol Recluso · Canal ⛓️ prisión  
- `/pagar_fianza_vct` (100.000 € o 50 % con seguro fianza)  
- `/trabajos_comunitarios` (5 tareas)  
- Expediente publicado en canal prisión (v2.9.7)  

### Atraco planificado
- 2–4 jugadores · 35 % éxito  
- Caja fuerte con decodificador: tope **100.000 €** (v2.9.5)  
- Bonos organizador y decodificador: +10.000 € NRD y +5 rep. criminal  

### Otras mecánicas
Extorsión · delatar (N25 + permisos) · desafío criminal · encargos oscuros · **contrabando FS22** (16 productos, 30 % inspección, cooldown 4 h) · blanquear · antecedentes  

`/denunciar` **desactivado** → usar `/perseguir`.

### Seguros `/seguro_vct`
Básico · Antirobo 7 d · Fianza judicial 7 d  

---

## 10. Economía social P2P

Préstamos · contratos entre ciudadanos (máx. 50.000 €) · fondos de sector · licencias staff · auditoría voluntaria.

Panel central: **`/mis_pendientes_vct`**

---

## 11. Minijuegos y casino

`/trabajo_rapido` · `/mini_trabajos_ocultos` · `/trabajos_comunitarios` · `/rasca_vct` · `/dados` · `/tragaperras` · `/giro_casino_vct`

Apuestas típicas: 100–10.000 €.

---

## 12. Trámites, Socio VCT, automatizaciones

### Trámites `/ticket`
Contrato (formulario → staff registra FS22) · Apelación

### Socio VCT
Suscripción Discord ~5 €/mes · `/tienda_vct` · `/verificar_socio_vct`

### Automatizaciones (sin acción del jugador)
Backup horario · resumen diario 21:00 · impuesto semanal lunes · ranking FS22 lunes · control inactividad diario 10:00 · nómina aviso · cumpleaños/aniversario · caducidad NRD · préstamos impagados

---

## 13. Administración (concepto)

Fundador / admin Discord: saldos globales, dar/retirar fondos, incautar alijo, inventarios, estado bot, sync socios.

`/admin_saldos` genera TXT con saldos y **registro ciudadanos** (altas, bajas, inactividad).

---

## 14. Inventario de comandos (2.12.0)

### Info y progresión
`/version` · `/nivel_vct` · `/postular_encargado` · `/estado_postulacion_vct` · `/tienda_vct` · `/verificar_socio_vct` · `/mis_pendientes_vct`

### Banco
`/bal` · `/reputacion` · `/cumpleanos` · `/depositar` · `/retirar` · `/transferencia` · `/pagar` · `/aportar_vct` · `/tesoreria_vct` · `/actividad_vct` · `/cobrar`

### FS22
`/vincular_fs22` · `/declarar_trabajo_fs22` · `/perfil_fs22` · `/historial_fs22` · `/top_trabajadores` · `/que_paso` · `/trabajos_fs22` · `/aceptar_trabajo_fs22` · `/rechazar_trabajo_fs22` · `/registrar_contrato_fs22` · `/pendientes_fs22`

### Tienda legal / especial / juegos / sociedad / crimen
(Ver secciones 7–11; ~87 comandos jugador + staff)

### Admin
`/admin_saldos` · `/admin_dar` · `/admin_retirar` · `/admin_retirar_nrd` · `/admin_incautar_alijo` · `/admin_inv` · `/admin_nivel` · `/admin_sync_socios` · `/estado_bot` · `/fondo_central`

**Eliminados en 2.11.2:** `/novedades` (usar `/version`) · `/aprobar_trabajo_fs22` (usar `/aceptar_trabajo_fs22`)

---

## 15. Historial de versiones recientes

| Versión | Tema principal |
|---------|----------------|
| **2.12.0** | Niveles XP N0–N30 / C5–C20, bloqueo comandos, roles auto, postulación Encargado |
| 2.11.2 | Unificación `/version` y `/aceptar_trabajo_fs22` |
| 2.11.1 | Inactividad granja solo sectores FS22 |
| 2.11.0 | Ciclo inactividad admin 40 d |
| 2.10.0 | Ciclo inactividad ciudadano 28 d, cuarentena |
| 2.9.8 | Registro ciudadanos en admin_saldos |
| 2.9.7 | Expediente penitenciario automático |
| 2.9.6 | Contrabando FS22 |
| 2.9.5 | Atraco: tope vault 100k, bonos |
| 2.9.4 | Lock banco, seguridad economía |
| 2.9.0 | Alarma, persecución, arresto, fianza |
| 2.8.0 | Tiendas interactivas en canales |
| 2.0.0 | Generación 2 estable en VPS |
| 2026.1 | Banco base, NRD, Ko-fi, juegos, tickets |

Historial detallado versión por versión: ver PDF/MD en Patreon y GitHub público (enlaces arriba).

---

## 16. Glosario

| Término | Significado |
|---------|-------------|
| VCT | Vanilla Center Trust |
| NRB | Número de Registro Bancario |
| NRD | Fondos no declarados |
| N / C | Nivel trabajador / criminal (XP) |
| FS22 | Farming Simulator 22 |
| Cuarentena | Bloqueo severo por inactividad fase 3 |
| Alijo | Bolsillo oculto de NRD |
| P2P | Contrato entre dos ciudadanos |

---

## 17. Uso en NotebookLM

**Preguntas que este documento responde bien:**
- ¿Qué comandos tiene un ciudadano nuevo (N0)?  
- ¿Cuándo multa/expulsa la inactividad?  
- ¿Cómo certificar un trabajo FS22?  
- ¿Qué desbloquea el nivel N15 o C10?  
- ¿Cómo funciona robo, persecución y fianza?  
- ¿Qué cambió en la versión 2.12.0?  

**Combinar con:** PDF historial completo (Patreon) para changelog exhaustivo v1.0→2.12.0.

---

© 2026 Angel del Valle Calero · Vanilla Center Trust [VCT] · Auditor Bancario 2.12.0 · Documento de conocimiento (sin datos de acceso)
