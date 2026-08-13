# Auditor Bancario VCT — Informe público: corrección de errores y parches

**Versión actual:** 2.12.11  
**Autor:** Angel del Valle Calero (calero89) · © 2026 · Vanilla Center Trust [VCT]  
**Público** — transparencia sobre bugs corregidos y mejoras de seguridad económica

---

## 1. Filosofía de correcciones VCT

El Auditor maneja **dinero virtual con valor de rol**. Un bug que duplique saldo o permita bypass de arresto rompe la confianza de la comunidad. Desde v2.9.4 se priorizan:

1. **Integridad de saldos** (no double-spend).
2. **Validar antes de borrar** estados pendientes.
3. **Bloquear acciones prohibidas** (arresto, cooldowns).
4. **Transparencia** en changelog (`/version`, `/novedades`).

---

## 2. Parches críticos v2.9.4 (seguridad economía)

### 2.1 Modal de contrato abonaba dinero automáticamente

| | |
|---|---|
| **Problema** | El formulario del ticket de trámites ejecutaba un abono al enviar el modal, sin validación staff. |
| **Impacto** | Dinero gratis explotable por cualquier ciudadano. |
| **Corrección** | Eliminado el abono automático en `ModalContrato` (`views.py`). El pago solo ocurre vía `/registrar_contrato_fs22` por encargado. |
| **Estado** | ✅ Corregido |

### 2.2 Carreras concurrentes en el banco (double-spend)

| | |
|---|---|
| **Problema** | Dos comandos simultáneos podían leer el mismo saldo y ambos descontar menos de lo debido. |
| **Impacto** | Duplicación de fondos o saldos negativos inconsistentes. |
| **Corrección** | `banco_sync.py`: `asyncio.Lock` + `envolver_arbol_comandos()` envuelve **todos** los slash commands. |
| **Patrón** | `async with transaccion_banco(): await comando_original()` |
| **Estado** | ✅ Corregido |

### 2.3 Reclusos compraban en tiendas fijadas

| | |
|---|---|
| **Problema** | Los catálogos persistentes (botones) no comprobaban arresto. |
| **Impacto** | Bypass de condena penitenciaria. |
| **Corrección** | `interaction_guards.bloquear_si_arrestado()` en `shop_views.py` antes de cada compra. |
| **Estado** | ✅ Corregido |

### 2.4 `/delatar` spameable

| | |
|---|---|
| **Problema** | Sin cooldown global ni por objetivo. |
| **Impacto** | Acoso y farmeo de recompensas. |
| **Corrección** | `DELATAR_COOLDOWN_HORAS = 24` en `config.py` + registro por objetivo en `sociedad.py`. |
| **Estado** | ✅ Corregido |

### 2.5 Préstamos y desafíos borrados antes de validar

| | |
|---|---|
| **Problema** | `pop()` del pendiente ocurría antes de comprobar saldos/apuestas. |
| **Impacto** | Pérdida del contrato/desafío si fallaba la validación posterior. |
| **Corrección** | Validar primero; solo `pop` si la operación va a completarse. |
| **Estado** | ✅ Corregido |

### 2.6 Doble uso de persecución

| | |
|---|---|
| **Problema** | `/perseguir` podía ejecutarse dos veces sobre el mismo robo. |
| **Impacto** | Doble recuperación o doble arresto. |
| **Corrección** | `consumir_persecucion()` al iniciar el procesamiento en `persecucion.py`. |
| **Estado** | ✅ Corregido |

---

## 3. Parches críticos v2.12.10 – v2.12.11 (inactividad y contrabando)

### 3.1 Actividad en chat no persistía (expulsiones injustas)

| | |
|---|---|
| **Problema** | `on_message` actualizaba `ultima_actividad` en RAM pero `guardar_datos()` solo se llamaba si el mensaje otorgaba XP (tope diario 20 XP). Comandos vía `on_interaction` nunca guardaban. |
| **Impacto** | Usuario escribía en chat horas antes del control de inactividad (10:00) pero el JSON seguía con fecha antigua → multa, despido, cuarentena y expulsión en cadena. |
| **Agravante** | Sin `ultima_actividad` guardada, el bot infería desde `last_pay` por defecto (2000-01-01) → miles de días inactivo. |
| **Corrección** | `bot_core.py`: siempre `guardar_datos()` tras mensaje; interacciones (sin autocomplete) también guardan. `automation.py`: flush RAM antes del backup horario. |
| **Estado** | ✅ Corregido v2.12.11 |

### 3.2 Contrabando mezclaba productos de todos los sectores

| | |
|---|---|
| **Problema** | Autocompletado de `/contrabando_fs22` no recibía el sector de Discord → listaba los 16 productos. |
| **Corrección** | Lectura sector desde namespace + payload; filtro estricto por sector; validación al ejecutar. |
| **Estado** | ✅ Corregido v2.12.10 |

---

## 4. Mejoras v2.9.2 – v2.9.3

| Versión | Corrección / mejora |
|---------|---------------------|
| 2.9.2 | `/perseguir` exige alarma VCT instalada |
| 2.9.2 | Seguro antirobo solo indemniza con póliza activa |
| 2.9.2 | Máximo 1 arresto por ladrón y día natural |
| 2.9.3 | Alarma destacada en catálogo tienda legal (visibilidad) |

---

## 5. Correcciones funcionales v2.6.x – v2.8.x

| Versión | Tema |
|---------|------|
| 2.6.6 | Encargos oscuros no se borraban al guardar calendario automático |
| 2.7.9 | Alijo ya no caduca automáticamente (solo NRD visible) |
| 2.8.0 | Tiendas interactivas: autocomplete en lugar de choices fijas (>25 productos) |
| 2.6.7 | Cooldown atraco solo organizador, no cómplices |

---

## 6. Mejoras recientes v2.9.5 – v2.12.9

| Versión | Cambio | Tipo |
|---------|--------|------|
| 2.9.5 | Tope caja fuerte atraco 100k + bonos líder/decodificador | Balance |
| 2.9.6 | `/contrabando_fs22` rediseñado (NRD + rep, no solo declaración) | Feature fix |
| 2.9.7 | Expediente penitenciario público en canal prisión | Feature |
| 2.12.9 | Consolidación comandos, fix desplegable víctima atraco | Feature |
| 2.12.10 | Contrabando filtrado por sector | Bugfix |
| 2.12.11 | Persistencia actividad inactividad | Bugfix crítico |

---

## 7. Cómo reportar un bug en VCT

1. Describir comando exacto y parámetros.
2. Captura del mensaje del bot (ephemeral o canal).
3. Hora aproximada (zona Europe/Madrid).
4. Si es económico: NRB del ciudadano afectado → staff usa `/admin_saldos`.

---

## 8. Proceso de despliegue de un parche

```
1. Corregir en PC local (vct_auditor/)
2. Actualizar version.py + changelog.py
3. Probar en entorno de prueba si existe
4. scp archivos modificados al VPS
5. systemctl restart vct-bot
6. Verificar journalctl + /version en Discord
7. Anuncio en canal noticias (opcional)
```

---

## 9. Errores conocidos / limitaciones actuales

| Tema | Estado |
|------|--------|
| Saldo negativo en multas si no hay fondos | Mitigado en contrabando v2.12.7; revisar otros comandos |
| Patreon API no crea posts automáticamente | Publicación manual |
| Activity Discord no integrada | No aplica al bot actual |

---

## 10. Tabla resumen parches de seguridad

| ID | Severidad | Versión | Área |
|----|-----------|---------|------|
| SEC-01 | Crítica | 2.9.4 | Modal contrato abono |
| SEC-02 | Alta | 2.9.4 | Lock banco |
| SEC-03 | Alta | 2.9.4 | Tiendas + arresto |
| SEC-04 | Media | 2.9.4 | Cooldown delatar |
| SEC-05 | Media | 2.9.4 | Préstamos/desafíos pop |
| SEC-06 | Media | 2.9.4 | Persecución doble |
| SEC-07 | Media | 2.9.2 | Arresto 1/día |

| SEC-08 | Crítica | 2.12.11 | Actividad inactividad no persistida |
| SEC-09 | Media | 2.12.10 | Contrabando sector autocomplete |

---

© 2026 Angel del Valle Calero · Vanilla Center Trust [VCT] · Informe público de correcciones · v2.12.11
