# 📋 Comandos del Auditor Bancario VCT

**Versión:** 2.9.3 · **Vanilla Center Trust [VCT]** · **88 comandos**  
**Autor:** Angel del Valle Calero (calero89) · © 2026

> En Discord escribe `/` y el nombre del comando.  
> Lo que ocurre en FS22/Luna **solo cuenta** si lo declaras aquí (salvo registro directo por staff).  
> **¿Primera vez?** Lee **[GUIA_INICIO_VCT.md](GUIA_INICIO_VCT.md)**.

---

## ℹ️ Información general

| Comando | Función |
|---------|---------|
| `/version` | Versión del bot e historial de cambios |
| `/novedades` | Igual que `/version` |
| `/tienda_vct` | Catálogo interactivo Socio VCT (botón suscripción Discord) · canal 💳-tienda_vct |
| `/verificar_socio_vct` | Comprueba tu suscripción y otorga el rol Socio VCT |
| `/mis_pendientes_vct` | Panel de todo lo pendiente (extorsión, préstamos, FS22, atracos, etc.) |

---

## 🏦 Banco y cuenta

| Comando | Función |
|---------|---------|
| `/bal` | Ver **NRB**, cartera legal, fondos no declarados (NRD), caja fuerte y reputación |
| `/reputacion` | Ver rep. **trabajador** y **criminal** (tuya o de otro) |
| `/cumpleanos` | Registrar cumpleaños (DD-MM) para bonus anual |
| `/depositar` | Pasar dinero de la cartera a la **caja fuerte** |
| `/retirar` | Sacar dinero de la caja fuerte a la cartera |
| `/transferencia` | Enviar dinero **legal** a otro ciudadano (impuesto al fondo VCT) |
| `/pagar` | Entregar dinero **legal en mano** (sin impuesto; solo cartera) |
| `/aportar_vct` | Donar dinero legal a la **tesorería del Auditor** (robable con `/robar`) |
| `/tesoreria_vct` | Ver saldo público de la tesorería del Auditor |
| `/actividad_vct` | Días sin actividad y plazos de multa/expulsión automática |
| `/cobrar` | Cobrar **nómina** según tus roles de Discord (cooldown por rol) |

---

## 🏛️ Tienda legal e inversiones

| Comando | Función |
|---------|---------|
| `/tienda_legal_vct` | Catálogo legal (incl. **Alarma de seguridad** 5.000 €) · 🏪-tienda_legal_vct |
| `/comprar_legal_vct` | Comprar producto legal (depósitos, buffs, etc.) |
| `/inventario_legal_vct` | Ver productos legales, buffs e inversiones activas |
| `/cobrar_inversion_vct` | Cobrar depósitos a plazo vencidos y bonus |
| `/usar_legal_vct` | Usar consumibles (informe del Auditor, bono reputación) |

---

## 🚜 Farming Simulator 22

| Comando | Quién | Función |
|---------|-------|---------|
| `/vincular_fs22` | Todos | Enlazar nick FS22 con Discord (**obligatorio** para cobrar) |
| `/declarar_trabajo_fs22` | Trabajadores | Declarar trabajo en mapa → **pendiente** (cobras al aceptar) |
| `/perfil_fs22` | Todos | Perfil FS22, ingresos, seguro VCT y licencias de sector |
| `/historial_fs22` | Todos | Historial de trabajos certificados |
| `/top_trabajadores` | Todos | Ranking por trabajos e ingresos |
| `/que_paso` | Todos | Resumen de actividad por sector (últimos días) |
| `/pendientes_fs22` | Staff | Cola de trabajos por aceptar (filtro por sector) |
| `/aceptar_trabajo_fs22` | Staff | Aceptar por ID (`P-00012`) → **pago + recibo + DM** al trabajador |
| `/aprobar_trabajo_fs22` | Staff | **Alias** de `/aceptar_trabajo_fs22` (compatibilidad) |
| `/rechazar_trabajo_fs22` | Staff | Rechazar con motivo → **DM** al trabajador con el motivo |
| `/registrar_contrato_fs22` | Staff | Registro **al instante** (varios trabajos, ayudantes, pago y recibo) |

**Sectores:** banco · ganadería · agricultura · silvicultura

**Flujo jornalero:** `/declarar_trabajo_fs22` → guardas el ID → staff `/aceptar_trabajo_fs22` → cobro en cartera, recibo en canal y aviso por DM.

**Ayudantes en contrato:** en `/registrar_contrato_fs22` cada ayudante cobra **cooperación independiente** (10.000 € + rep. trabajador), sin depender de rango ni sector; figura en el recibo.

---

## 🤝 Economía social

| Comando | Función |
|---------|---------|
| `/prestamo_vct` | Solicitar préstamo (avisa al prestamista en canal y por DM) |
| `/prestamo_responder` | Prestamista acepta o rechaza la solicitud |
| `/contrato_entre_ciudadanos` | Contrato P2P legal (máx. 50.000 €; avisa al receptor en canal y DM) |
| `/contrato_entre_jugadores` | **Alias** de `/contrato_entre_ciudadanos` |
| `/contrato_responder` | Receptor acepta o rechaza (con `motivo` si rechaza; avisos DM) |
| `/seguro_vct` | Pólizas: básico, **Antirobo** (70 % al atrapar ladrón) y **Fianza judicial** (50 % fianza) |
| `/auditoria_voluntaria` | Pago al fondo central: +rep. trabajador y menos multa inactividad (1×/mes) |
| `/licencia_sector` | Staff: emitir licencia temporal (transporte / mercado) |
| `/fondo_sector` | Ver caja común de un sector |
| `/fondo_sector_aportar` | Aportar dinero legal al fondo del sector |
| `/fondo_sector_gastar` | Encargado/dueño: gastar caja común del sector |

---

## 🕶️ Crimen, NRD y submundo

| Comando | Función |
|---------|---------|
| `/robar` | Robar a otro (éxito → NRD; alarma del objetivo baja éxito al 25 %). Víctima: `/perseguir` |
| `/atraco_planificado` | Atraco en equipo (2–4): invita cómplices por DM |
| `/atraco_responder` | Cómplice acepta o rechaza la invitación al atraco |
| `/perseguir` | Tras robo con **alarma** (24 h): recuperar fondos y arrestar al sospechoso |
| `/pagar_fianza_vct` | En ⛓️prisión: fianza desde **cartera** o **caja fuerte** (100k / 50k con seguro) |
| `/denunciar` | **Desactivado** — usa `/perseguir` si fuiste víctima de robo |
| `/entregar_efectivo` | Dar NRD en mano a otro jugador |
| `/blanquear_fondos` | Pasar NRD → cartera legal (comisión 15 %) |
| `/transferir_nrd` | Transferir NRD entre criminales (comisión alta, +rep. criminal) |
| `/extorsionar` | Exigir pago en NRD (aviso canal + DM; plazo 24 h) |
| `/pagar_extorsion_vct` | Pagar extorsión pendiente |
| `/delatar` | Delatar a quien acumula mucho NRD (recompensa legal + rep. trabajador) |
| `/encargo_oscuro` | Publicar encargo criminal en boletín del Estado |
| `/encargo_aceptar` | Aceptar encargo del boletín |
| `/contrabando_fs22` | Declaración arriesgada con riesgo de inspección aleatoria |
| `/desafio_criminal` | Desafiar a otro apostando NRD (aviso canal + DM al retado) |
| `/desafio_responder` | Aceptar o rechazar desafío criminal |
| `/antecedentes` | Consultar antecedentes públicos de robos fallidos/incautaciones |

---

## 🧳 Alijo y tienda especial (ilegal)

| Comando | Función |
|---------|---------|
| `/tienda_especial_vct` | Catálogo interactivo mercado negro (soborno, Guante Blanco, etc.) · canal ⛺-tienda_especial_vct |
| `/inventario_vct` | Ver items de tienda especial y estado del alijo |
| `/alijo_vct` | Estado del alijo oculto (requiere maletín) |
| `/ocultar_nrd` | Mover NRD visible al alijo (comisión 30 %, requiere maletín) |
| `/recuperar_nrd` | Sacar NRD del alijo a saldo visible |

---

## 🎮 Juegos VCT

| Comando | Función |
|---------|---------|
| `/juegos` | Lista de minijuegos y límites de apuesta |
| `/trabajo_rapido` | Mini trabajo legal: pago y rep. trabajador (cooldown 20 min) |
| `/mini_trabajos_ocultos` | Encargo clandestino: NRD y rep. criminal |
| `/trabajos_comunitarios` | Reduce rep. criminal según dificultad (cooldown 2 h) |
| `/rasca_vct` | Comprar rasca y probar suerte |
| `/dados` | Apuesta a dados contra el Auditor |
| `/tragaperras` | Tirada de tragaperras |
| `/giro_casino_vct` | Apuesta a rojo, oscuro o verde |

---

## 📋 Trámites, staff y moderación

| Comando | Quién | Función |
|---------|-------|---------|
| `/ticket` | Todos | Panel de gestión ciudadana (contratos / apelaciones) |
| `/clear` | Mod | Limpiar mensajes del canal |
| `/anuncio` | Staff | Formulario para anuncio oficial |
| `/anuncio_directo` | Staff | Anuncio corto sin formulario |
| `/inspeccionar` | Staff | Inspección por contrabando (multa + antecedente) |

---

## 🔧 Administración (Fundador / Admin)

| Comando | Función |
|---------|---------|
| `/admin_saldos` | Informe global: carteras, NRD, cajas y deudas de extorsión |
| `/fondo_central` | Ver estado del fondo central VCT |
| `/admin_dar` | Dar dinero legal a un ciudadano |
| `/admin_retirar` | Embargar dinero legal de la cartera |
| `/admin_retirar_nrd` | Incautar NRD visible de un ciudadano |
| `/admin_incautar_alijo` | Incautar fondos del alijo oculto (inspección staff) |
| `/admin_inv` | Ver inventarios de items de usuarios |
| `/admin_sync_socios` | Sincronizar roles Socio VCT con suscripciones Discord |
| `/estado_bot` | Estado del bot, banco y último backup |

---

## ⚙️ Automático (sin comando)

- Al **entrar** al servidor: rol Ciudadano + NRB generado  
- **Impuesto semanal** (lunes), resumen diario (21:00), backups cada hora  
- **Inactividad:** multa y expulsión automáticas según días sin actividad (mensajes/comandos reinician plazo)  
- **Préstamos impagados:** procesamiento diario a las 08:00 (antecedente + cobro)  
- **NRD visible:** caduca a los 7 días sin blanquear u ocultar; **alijo** sin caducidad automática
- **Tesorería Auditor:** no paga impuesto semanal; robable con `/robar` y `/atraco_planificado`  

---

## 📌 Texto corto para Discord (copiar y pegar)

```
📋 COMANDOS AUDITOR BANCARIO VCT v2.9.3 (88)

🏦 BANCO
/bal · /depositar · /retirar · /transferencia · /pagar
/reputacion · /cumpleanos · /actividad_vct
/aportar_vct · /tesoreria_vct · /cobrar

🏛️ TIENDA LEGAL
/tienda_legal_vct · /comprar_legal_vct · /inventario_legal_vct
/cobrar_inversion_vct · /usar_legal_vct

🚜 FS22
/vincular_fs22 · /declarar_trabajo_fs22 · /que_paso
/perfil_fs22 · /historial_fs22 · /top_trabajadores
Staff: /pendientes_fs22 · /aceptar_trabajo_fs22 · /rechazar_trabajo_fs22
       /registrar_contrato_fs22  (/aprobar_trabajo_fs22 = alias)

🤝 ECONOMÍA SOCIAL
/prestamo_vct · /prestamo_responder
/contrato_entre_ciudadanos · /contrato_entre_jugadores · /contrato_responder
/seguro_vct · /auditoria_voluntaria · /licencia_sector
/fondo_sector · /fondo_sector_aportar · /fondo_sector_gastar

🕶️ CRIMEN
/robar · /perseguir · /atraco_planificado · /atraco_responder · /pagar_fianza_vct
/entregar_efectivo · /blanquear_fondos · /transferir_nrd
/extorsionar · /pagar_extorsion_vct · /delatar
/encargo_oscuro · /encargo_aceptar · /contrabando_fs22
/desafio_criminal · /desafio_responder · /antecedentes

🧳 ALIJO / TIENDA ESPECIAL
/tienda_especial_vct · /inventario_vct · /alijo_vct
/ocultar_nrd · /recuperar_nrd

🎮 JUEGOS
/juegos · /trabajo_rapido · /mini_trabajos_ocultos · /trabajos_comunitarios
/rasca_vct · /dados · /tragaperras · /giro_casino_vct

⭐ SOCIO VCT · PENDIENTES
/tienda_vct · /verificar_socio_vct · /mis_pendientes_vct

📋 /ticket · /clear · /inspeccionar (staff)
/version · /novedades

En FS22 solo cuenta lo certificado en Discord.
— Angel del Valle Calero · Vanilla Center Trust [VCT]
```
