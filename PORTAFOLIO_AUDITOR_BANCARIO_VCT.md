# Portafolio — Auditor Bancario VCT

**Autor:** Angel del Valle Calero (calero89)  
**Marca:** Vanilla Center Trust [VCT]  
**Versión actual:** 2.12.11  
**Contacto:** vidagaming.89@gmail.com

---

## Resumen en una frase

Diseñé y desarrollé un **ecosistema económico completo en Discord** para una comunidad de Farming Simulator 22: banco virtual, trabajos certificados, crimen de rol, tiendas, progresión y automatizaciones 24/7, con el bot en producción en un VPS.

---

## 1. Contexto

### ¿Qué es?

**Auditor Bancario VCT** es el “banco oficial” de una comunidad de rol en Discord vinculada a **Farming Simulator 22**. Los jugadores no solo chatean: tienen cuenta bancaria, cobran nóminas, declaran trabajos del mapa, compran en tiendas, compiten por reputación y pueden entrar en la economía criminal (dinero negro, robos, contrabando).

### ¿Para quién?

- **Jugadores:** una experiencia clara con comandos `/`, recibos y reglas entendibles.
- **Staff / encargados:** herramientas para certificar trabajos FS22, moderar y gestionar sectores.
- **Fundador / administración:** panel local, backups, publicación automatizada y documentación pública/privada.

### Alcance del proyecto

| Indicador | Dato |
|-----------|------|
| Comandos slash | ~88 |
| Módulos de código | Arquitectura modular `vct_auditor/` |
| Disponibilidad | Bot 24/7 en VPS Linux |
| Integraciones | Discord, Ko-fi, Patreon (opcional), web de postulaciones |
| Documentación | Informes públicos, guías de inicio, changelog por versión |

---

## 2. El reto / problema

### Situación inicial

Una comunidad de FS22 necesitaba **más que un servidor de Discord**: hacía falta una **economía creíble** donde lo que ocurre en el juego tenga consecuencias en el rol, sin depender de mods que conecten el juego con Discord (complejos y frágiles).

### Problemas concretos a resolver

1. **Desconexión juego ↔ Discord**  
   Lo que un jugador hace en el mapa no se reflejaba en una economía compartida.

2. **Abuso y desconfianza**  
   Sin certificación, cualquiera podía “inventarse” ingresos. Hacía falta staff, IDs de trabajo y trazabilidad.

3. **Complejidad para el usuario**  
   Muchas mecánicas (legal, FS22, crimen, tiendas, niveles) sin una guía clara generan abandono.

4. **Riesgo técnico**  
   Dinero virtual con valor de rol: bugs de doble cobro, timeouts de Discord, cooldowns fantasma o guards mal aplicados rompen la confianza de la comunidad.

5. **Operación continua**  
   El bot debía vivir en un VPS, actualizarse con seguridad y dejar copias de respaldo sin exponer secretos.

### Objetivo de diseño

> **Usabilidad primero:** que un jugador nuevo entienda en minutos cómo jugar, y que un fallo técnico nunca castigue sin explicación (mensajes claros, respuestas ephemeral, errores controlados).

---

## 3. El proceso

### Fase 1 — Fundamentos (economía y banco)

- Cuenta por jugador (cartera, caja fuerte, dinero negro).
- Nóminas por roles de Discord.
- Transferencias, depósitos, impuestos y reputación (trabajador / criminal).
- Persistencia en JSON con escritura atómica y locks anti carreras.

**Decisión de usabilidad:** comandos con nombres en español y mensajes que explican *qué pasó* y *qué hacer después*.

### Fase 2 — Integración FS22 (sin mods en el juego)

- Flujo: jugar en el mapa → declarar en Discord → staff certifica → cobro y recibo.
- Comandos: vincular nick, declarar trabajo, perfil, historial, actividad por sector.
- Regla de oro comunicada a la comunidad: **solo cuenta lo certificado en Discord**.

**Por qué así:** máxima compatibilidad (solo FS22 base + Discord), control antitrampas y panel claro para encargados.

### Fase 3 — Profundidad de juego

- Economía social: préstamos, contratos entre jugadores, fondos de sector, seguros.
- Submundo: robos, extorsión, blanqueo, contrabando FS22, arresto y fianza.
- Progresión por niveles (N/C) que desbloquean comandos de forma progresiva.
- Tiendas interactivas en Discord (legal, especial, socio) con guards de arresto y nivel.

### Fase 4 — Producción y confiabilidad

- Refactor a paquete modular `vct_auditor/`.
- Despliegue en VPS (`systemctl`, logs, `kofi.env` fuera de Git).
- Script de publicación: backup local, push a repos privado/público, validación `py_compile`.
- Correcciones críticas documentadas: timeouts de Discord (defer + persistencia fuera del lock), cooldowns que no deben bloquear sin respuesta, carga de variables de entorno robusta.

### Fase 5 — Documentación y divulgación

- Guía de inicio para nuevos ciudadanos.
- Informes públicos (código explicado, correcciones, plantillas).
- Carpeta `ejemplos/` y tests de regresión en patrones sensibles (persistencia, locks, entorno).
- Repo público solo con documentación; código y datos en repo privado.

### Flujo de experiencia (jugador FS22)

```
Entrar al Discord → /bal
       ↓
/vincular_fs22 (una vez)
       ↓
Jugar en el mapa (servidor dedicado multijugador)
       ↓
/declarar_trabajo_fs22 → recibes ID
       ↓
Staff acepta → dinero + recibo + DM
```

---

## 4. Resultados

### Impacto en la comunidad

- **Economía viva** con decenas de sistemas interconectados en un solo bot.
- **Rol FS22 integrado** sin obligar a instalar mods técnicos.
- **Staff empoderado** con comandos de certificación, inspección y administración.
- **Jugadores informados** mediante `/version`, `/novedades`, guías y canales oficiales.

### Logros técnicos (selección)

| Área | Resultado |
|------|-----------|
| Escala | ~88 comandos slash organizados por dominio |
| Estabilidad | Bot en producción 24/7; despliegue documentado y repetible |
| Seguridad económica | Locks de banco, guards de arresto/nivel, persistencia atómica |
| UX Discord | Respuestas ephemeral, defer ante timeouts, mensajes de cooldown legibles |
| Calidad | Tests de regresión en persistencia, locks y configuración |
| DevOps | Publicación automatizada, backups, repos privado + público |

### Caso destacado (usabilidad + fiabilidad)

**Problema:** `/contrabando_fs22` mostraba “La aplicación no ha respondido” y, al reintentar, bloqueaba 4 horas sin haber completado la acción.

**Solución:** eliminar cooldown prematuro de Discord, ACK inmediato (`defer`), persistencia fuera del lock del event loop, y cooldown real solo tras éxito en banco.

**Resultado:** el jugador siempre recibe feedback; no pierde horas por un fallo de red/tiempo.

### Entregables que demuestran el proyecto

- Bot Discord en producción (Auditor Bancario VCT).
- Panel local de supervisión (`panel_vct.py`).
- Documentación pública en GitHub.
- Informes PDF para Patreon / comunidad.
- Pipeline de actualización con un comando (`publicar_vct.ps1`).

---

## 5. Habilidades demostradas

| Categoría | Ejemplos |
|-----------|----------|
| **Producto** | Diseño de economía de rol, progresión, onboarding |
| **Backend** | Python, discord.py, persistencia JSON, webhooks Ko-fi |
| **UX / Usabilidad** | Comandos claros, mensajes de error útiles, guías paso a paso |
| **Arquitectura** | Modularización, separación config / dominio / comandos |
| **DevOps** | VPS Linux, systemd, despliegue por archivos, backups |
| **Calidad** | Tests unitarios, informes de correcciones, changelog versionado |
| **Comunicación** | Docs públicas, anuncios de actualización, informes para no técnicos |

---

## 6. Cómo usar este portafolio (para ti)

### En LinkedIn / CV (párrafo corto)

> Desarrollé **Auditor Bancario VCT**, un ecosistema económico en Discord para una comunidad de Farming Simulator 22: ~88 comandos, banco virtual, certificación de trabajos in-game, tiendas, crimen de rol y automatizaciones 24/7 en VPS. Prioricé **usabilidad** (onboarding claro, mensajes comprensibles) y **fiabilidad** (anti double-spend, guards, tests de regresión).

### En una entrevista (30 segundos)

> Es un banco virtual dentro de Discord para una comunidad de simulación agrícola. Los jugadores declaran lo que hacen en el mapa, el staff lo certifica, y el bot paga, registra y aplica reglas de crimen, tiendas y niveles. Lo tengo en producción en un VPS, con documentación y tests en las partes críticas.

### Para un reclutador no técnico

> Imagina un **banco + ayuntamiento + tienda + comisaría** dentro de Discord, conectado al rol de un juego de granjas. Yo lo diseñé, lo programé, lo documenté y lo mantengo en un servidor siempre encendido.

### Enlaces de referencia (públicos)

- Documentación: [App-Auditor-Bancario-Public](https://github.com/calero1989/App-Auditor-Bancario-Public)
- Ko-fi: [calero89](https://ko-fi.com/calero89)

*(El código fuente completo y datos de producción son privados por licencia y seguridad.)*

---

## 7. Próximos pasos (visión)

- Servidor dedicado FS22 multijugador (hasta 16 jugadores) en VPS Windows, paralelo al bot.
- Seguir endureciendo UX en comandos de cooldown largo y tiendas persistentes.
- Ampliar documentación pública y materiales para nuevos ciudadanos.

---

## Pie de página

**Auditor Bancario VCT** · Vanilla Center Trust [VCT]  
© 2026 Angel del Valle Calero (calero89) · Todos los derechos reservados.

*Documento de portafolio — uso personal para presentación profesional y divulgación del proyecto.*
