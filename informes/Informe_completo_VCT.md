# Auditor Bancario VCT — Informe para conocimiento del sistema

**Proyecto:** Vanilla Center Trust [VCT]  
**Producto:** Auditor Bancario VCT (bot de economía y trámites en Discord)  
**Versión de referencia:** 2.9.4  
**Contexto:** Comunidad de rol vinculada a Farming Simulator 22  
**Idioma del documento:** Español  

> Este documento describe **qué es el sistema, cómo funciona para los jugadores y qué reglas gobiernan la economía**.  
> No incluye datos de infraestructura, accesos, secretos ni despliegue técnico.

---

## 1. ¿Qué es el Auditor Bancario VCT?

El **Auditor Bancario VCT** es un bot de Discord que centraliza la **economía virtual**, la **reputación**, los **trámites** y la **certificación de actividad** de la comunidad Vanilla Center Trust.

Funciona como un **banco central ficticio** dentro del servidor de Discord: cada ciudadano tiene cuenta, saldos, historial y obligaciones. El bot no sustituye al juego FS22, pero **certifica** lo que los jugadores declaran o lo que el staff registra.

### Regla fundamental

> **Lo que ocurre en el mapa de Farming Simulator solo cuenta en la economía VCT si se declara o registra en Discord** mediante los comandos del Auditor (salvo registro directo por encargados).

### Al unirse al servidor

- Se asigna el rol de **Ciudadano de VCT**
- Se genera un **NRB** (Número de Registro Bancario) único
- Se crea la cuenta en el sistema del Auditor

---

## 2. Conceptos económicos para jugadores

### 2.1 Tres tipos de dinero

| Concepto | Nombre en el bot | Descripción |
|----------|------------------|-------------|
| **Cartera legal** | Balance | Dinero oficial, visible, con impuestos en transferencias |
| **Caja fuerte** | Vault | Ahorro guardado; más difícil de robar en atracos en equipo |
| **Fondos no declarados** | NRD (dinero negro) | Dinero ilegal; debe lavarse u ocultarse; caduca si no se gestiona |

### 2.2 Reputación dual

Cada jugador tiene dos barras de reputación independientes:

- **Reputación trabajador** — sube con trabajos, contratos, denuncias legítimas, cooperación
- **Reputación criminal** — sube con robos, extorsión, mercado negro, desafíos ilegales

El perfil del ciudadano refleja ambas dimensiones.

### 2.3 Impuestos y comisiones (resumen)

| Operación | Tasa aproximada |
|-----------|-----------------|
| Transferencia legal entre ciudadanos | 5 % al fondo central VCT |
| Lavado de NRD a legal | 15 % |
| Impuesto semanal automático (lunes) | 20 % sobre cartera legal |
| Transferencia de NRD entre criminales | 20 % comisión |
| Ocultar NRD en alijo | 30 % comisión |

### 2.4 Caducidad del dinero negro visible

- El **NRD en saldo visible** avisa a los 5 días y **caduca a los 7 días** si no se blanquea ni se oculta en alijo
- El **alijo** (bolsillo oculto) **no caduca automáticamente**; solo puede incautarse por inspección administrativa

### 2.5 Fondo central y tesorería

- El **fondo central VCT** recibe impuestos y comisiones del servidor
- La **tesorería del Auditor** es una cuenta institucional a la que se puede donar; es robable en mecánicas de crimen y no paga impuesto semanal

---

## 3. Nóminas y roles de Discord

Los jugadores con rangos remunerados en Discord pueden cobrar con `/cobrar`:

| Tipo de rol | Ejemplos | Pago orientativo | Cooldown orientativo |
|-------------|----------|------------------|----------------------|
| Dirección / dueños de sector | Fundador, Dueño Banco, Dueño Agricultura… | 50.000 € | 60 minutos |
| Supervisión | Supervisor, Inspector | 20.000 € | 60 minutos |
| Encargados de sector | Encargado Ganadería, Agricultura, Silvicultura | 10.000 € | 30 minutos |
| Peones de sector | Peón Ganadero, Agrícola, Silvicultura | 5.000 € | 30 minutos |
| Jornalero | Jornalero general | 2.500 € | 30 minutos |
| Inversor institucional | Inversor del Banco Central | 100.000 € | 60 minutos |

Si un jugador tiene **varios rangos remunerados**, puede cobrar todos los que estén fuera de cooldown en una sola nómina.

---

## 4. Farming Simulator 22 — certificación de trabajos

### 4.1 Sectores VCT

- Banco / Central  
- Ganadería  
- Agricultura  
- Silvicultura  

### 4.2 Vinculación obligatoria

Antes de cobrar trabajos, el jugador debe usar `/vincular_fs22` para enlazar su nick del juego con Discord.

### 4.3 Dos flujos de trabajo

**Flujo jornalero (con aprobación):**

1. El trabajador declara con `/declarar_trabajo_fs22`
2. El trabajo queda **pendiente** con un ID (ej. P-00012)
3. Un encargado acepta con `/aceptar_trabajo_fs22` o rechaza con motivo
4. Al aceptar: pago neto en cartera, recibo público y aviso por mensaje privado

**Flujo staff (inmediato):**

- `/registrar_contrato_fs22` registra, paga y emite recibo al instante
- Permite hasta **5 tipos de trabajo** en un mismo contrato
- Permite **ayudantes** que cobran cooperación independiente (10.000 € + reputación trabajador cada uno)

### 4.4 Tipos de trabajo registrables (36)

**Trabajo de campo clásico:** Cosecha, Cosecha especial, Siembra, Siembra especial, Abonado, Mantenimiento de hierba, Arado, Labrado, Tala, Transporte, Compra, Venta, Segar, Empacar (paja, heno, ensilaje, hierba), Ensilar, Palets.

**Trabajo de campo ampliado:** Hilerar, Henificar, Recoger piedras, Astillado, Compactación de silo, Encintar pacas, Esparcir estiércol, Esparcir purín, Escardar, Plantar, Labrar, Rodillo, Esparcir cal.

**Contratos de sector:** Contrato de ganadería, agricultura, silvicultura, banco central.

**Pagos bruto orientativos:** entre 3.000 € y 6.000 € la mayoría de tareas; contratos de sector entre 12.000 € y 15.000 €; tareas especiales hasta 10.000 €.

El pago neto al trabajador es el bruto menos un **5 %** de impuesto de transacción al fondo central.

**Consulta de catálogo:** `/trabajos_fs22` lista todos los tipos con su pago bruto.

### 4.5 Otros comandos FS22 útiles

- `/perfil_fs22` — perfil, ingresos, seguros, licencias  
- `/historial_fs22` — trabajos certificados  
- `/top_trabajadores` — ranking  
- `/que_paso` — actividad reciente por sector  
- `/pendientes_fs22` — cola de aprobación (staff)  

---

## 5. Tienda legal

La tienda legal vende productos pagados con **cartera legal**. Está organizada en paquetes:

### Paquete financiero
- Depósito a plazo 7 días (+10 % al vencer)
- Bonos del fondo central (cupones semanales)
- Cuenta premium bancaria (menos impuesto en transferencias)
- Seguro de cosecha (recuperación parcial en juegos de azar)

### Paquete agrícola / FS22
- Semillas certificadas (+10 % en próximo trabajo aprobado)
- Contrato de maquinaria (+2.000 € en trabajos elegibles)
- Cooperativa agrícola (bonus por volumen de trabajos)
- Póliza multigranja (protección de reputación ante rechazo)

### Paquete negocio
- Puesto en mercado semanal (ingreso aleatorio los lunes)
- Licencia de comercio
- Almacén refrigerado
- Certificado de inversor
- **Alarma de seguridad VCT** (5.000 €) — reduce probabilidad de robo exitoso contra el titular

### Paquete consumible
- Combustible agrícola, informe del Auditor, bono de reputación trabajador

### Paquete coleccionable
- Items de largo plazo y colección VCT

**Comandos:** `/tienda_legal_vct`, `/comprar_legal_vct`, `/inventario_legal_vct`, `/cobrar_inversion_vct`, `/usar_legal_vct`

Los catálogos también están disponibles como **menús interactivos fijados** en canales dedicados del servidor.

---

## 6. Mercado negro y alijo

### 6.1 Tienda especial

Productos pagados con **NRD**:

| Producto | Precio orientativo | Efecto |
|----------|-------------------|--------|
| Soborno clandestino | 500.000 NRD | Reduce reputación criminal |
| Licencia Guante Blanco | 25.000 NRD | Varios robos fallidos sin multa |
| Decodificador Digital | 10.000 NRD | Hackea caja fuerte tras robo o atraco fallido |
| Maletín offshore | 150.000 NRD | Desbloquea sistema de alijo |

### 6.2 Alijo

- Requiere **maletín offshore** comprado previamente
- `/ocultar_nrd` mueve NRD visible al alijo (con comisión)
- `/recuperar_nrd` saca fondos del alijo
- `/alijo_vct` consulta estado
- El alijo **no caduca solo**; el NRD visible sí

**Comandos:** `/tienda_especial_vct`, `/inventario_vct`, `/alijo_vct`, `/ocultar_nrd`, `/recuperar_nrd`

---

## 7. Crimen, orden público y justicia

### 7.1 Robo individual (`/robar`)

| Situación de la víctima | Probabilidad de éxito del ladrón |
|-------------------------|----------------------------------|
| Sin alarma de seguridad | 50 % |
| Con alarma instalada | 25 % |

- Éxito: el ladrón recibe NRD
- Fallo: multa y antecedente
- Con alarma: la víctima puede iniciar persecución en 24 horas

### 7.2 Persecución (`/perseguir`)

**Requisitos:** la víctima debe tener **alarma de seguridad** instalada y una persecución activa tras robo o intento (plazo 24 h).

**Resolución:** minijuego basado en reputación trabajador vs criminal más azar.

- **Éxito víctima:** recupera parte del botín; puede arrestar al sospechoso; seguro Antirobo indemniza hasta 70 % (con póliza activa)
- **Fallo víctima:** el sospechoso escapa con bonus de reputación criminal
- **Límite:** máximo **1 arresto por ladrón y día** (la recuperación sí puede repetirse)

### 7.3 Arresto y prisión

Cuando un sospechoso es arrestado:

- Recibe rol de **Recluso de VCT**
- Debe usar canal de prisión para trámites permitidos
- Puede salir pagando **fianza** (100.000 €, o 50 % con seguro de fianza judicial)
- O completando **trabajos comunitarios** (5 tareas con tiempo entre ellas)

En arresto **no puede** hacer movimientos financieros normales ni comprar en catálogos de tienda.

### 7.4 Atraco planificado en equipo

| Parámetro | Valor |
|-----------|-------|
| Tamaño del equipo | 2 a 4 jugadores |
| Probabilidad de éxito | 35 % |
| Botín de cartera (si éxito) | 15 % a 35 % del saldo legal de la víctima |
| Botín de caja fuerte (con decodificador) | 10 % a 25 %, tope 10.000 € |
| Multa por fallo (sin decodificador) | 15.000 € por participante |
| Cooldown del organizador | 48 horas |
| Patrimonio mínimo de la víctima | 100.000 € (cartera + caja combinadas) |

Flujo: organizador invita cómplices → todos responden → se ejecuta automáticamente al completar respuestas.

### 7.5 Otras mecánicas criminales

- **Extorsión** — exige pago en NRD con plazo de 24 h
- **Delatar** — recompensa legal por delatar a quien acumula mucho NRD (con cooldown de 24 h)
- **Desafío criminal** — apuesta de NRD resuelta con dados
- **Encargo oscuro** — publicación de encargo en boletín del Estado
- **Contrabando FS22** — declaración arriesgada con posible inspección
- **Blanqueo** — NRD → legal con comisión del 15 %
- **Transferencia NRD** — entre criminales con alta comisión
- **Antecedentes** — historial público de incidentes

El comando `/denunciar` está **desactivado**; se usa el flujo de persecución con alarma.

### 7.6 Seguros (`/seguro_vct`)

| Póliza | Beneficio principal |
|--------|---------------------|
| Básico semanal | Cobertura parcial tras robo |
| Antirobo (7 días) | Indemnización al atrapar ladrón |
| Fianza judicial (7 días) | Descuento del 50 % en fianza de arresto |

---

## 8. Economía social entre ciudadanos

### Préstamos
- Solicitud con `/prestamo_vct`; el prestamista responde
- Monto máximo orientativo: 500.000 €
- Impagos generan antecedentes y cobros automáticos

### Contratos entre ciudadanos (P2P)
- Oferta legal entre dos jugadores (máx. 50.000 €)
- El receptor debe aceptar o rechazar con motivo
- El pago solo se ejecuta si hay saldo y aceptación

### Fondos de sector
- Cada sector (ganadería, agricultura, silvicultura, banco) tiene caja común
- Aportaciones y gastos autorizados por encargados

### Licencias de sector
- Emitidas por staff: transporte o mercado, duración 7 días

### Auditoría voluntaria
- Pago mensual al fondo central a cambio de reputación trabajador y reducción de multa por inactividad

### Panel de pendientes
`/mis_pendientes_vct` centraliza: préstamos, contratos, extorsiones, atracos, trabajos FS22, desafíos, encargos.

---

## 9. Minijuegos y casino

| Comando | Naturaleza |
|---------|------------|
| `/trabajo_rapido` | Mini trabajo legal con cooldown |
| `/mini_trabajos_ocultos` | Encargo clandestino en NRD |
| `/trabajos_comunitarios` | Reduce reputación criminal |
| `/rasca_vct` | Rasca y gana |
| `/dados` | Apuesta a dados |
| `/tragaperras` | Tragaperras |
| `/giro_casino_vct` | Ruleta (rojo/negro/verde) |

Apuestas típicas entre 100 € y 10.000 €.

---

## 10. Trámites y panel ciudadano

### Centro de trámites (`/ticket`)
Panel con botones persistentes:
- **Crear contrato** — envía formulario al registro oficial (el plus del Auditor lo cobra staff con registro FS22, no automáticamente)
- **Apelación** — solicitud de revisión de sanción

### Anuncios oficiales
Staff puede publicar anuncios con formulario o mensaje directo.

### Inspección
Staff puede inspeccionar por contrabando con multa y antecedente.

---

## 11. Socio VCT y membresías

- **Socio VCT** — suscripción vía tienda de Discord; rol especial y ventajas configurables
- **Ko-fi** — donaciones/suscripciones pueden vincularse a roles de ciudadano o socio según tier
- Verificación manual con `/verificar_socio_vct` tras comprar suscripción Discord

---

## 12. Automatizaciones del sistema (sin intervención del jugador)

| Evento | Comportamiento |
|--------|----------------|
| Entrada al servidor | Rol ciudadano + creación de cuenta NRB |
| Backup de datos | Periódico (horario) |
| Resumen económico | Diario por la noche (zona España) |
| Impuesto semanal | Lunes por la mañana |
| Ranking semanal trabajadores | Lunes |
| Control de inactividad | Diario: multa a 7 días sin actividad, expulsión posible a 14 días |
| Préstamos vencidos | Procesamiento matinal |
| Cumpleaños y aniversario en servidor | Bonificaciones automáticas |
| Aviso de nómina disponible | Cada varias horas |
| Caducidad NRD visible | Tras 7 días sin gestionar |

**Actividad válida:** enviar mensajes en Discord o usar comandos del Auditor reinicia el contador de inactividad.

---

## 13. Administración (concepto, no accesos)

Roles de **Fundador**, **Dueño**, **Encargado** o **administrador de Discord** pueden:

- Ver saldos globales y fondo central
- Dar o retirar fondos a ciudadanos
- Incautar NRD o alijos
- Ver inventarios
- Consultar estado del bot y última copia de seguridad
- Sincronizar roles de socio

Los ciudadanos normales no tienen acceso a estas funciones.

---

## 14. Arquitectura conceptual (sin infraestructura)

El Auditor Bancario es una aplicación **Python** que usa la API de **Discord** (comandos slash, botones, menús persistentes).

**Persistencia:** archivos JSON locales (cuentas de jugadores, estado de eventos globales, fondo central).

**Modularidad interna:**
- Núcleo del bot y eventos
- Comandos por áreas (banco, FS22, crimen, sociedad, juegos, admin)
- Lógica de economía, impuestos y reputación
- Tiendas legal y especial
- Sistema de persecución y prisión
- Tareas programadas automáticas
- Integración opcional con plataformas de donación

**Seguridad de datos (concepto):**
- Guardado atómico para evitar corrupción de archivos
- Copias de seguridad periódicas
- Bloqueo de transacciones concurrentes para evitar errores de saldo
- Secretos y datos de jugadores fuera del repositorio público de código

---

## 15. Ejemplos de implementación (ilustrativos)

Los fragmentos siguientes son **versiones depuradas** del código real. No incluyen tokens, IDs de canales Discord, rutas de servidor ni lógica criminal/admin completa. El código de producción permanece en el repositorio privado; en GitHub público están en la carpeta [`ejemplos/`](ejemplos/).

### 15.1 Constantes de economía

Las reglas descritas en las secciones 2–4 se codifican como constantes centralizadas:

```python
IMPUESTO_TRANSACCION = 0.05
IMPUESTO_LAVADO = 0.15
IMPUESTO_SEMANAL = 0.20
NEGRO_CADUCIDAD_DIAS = 7
ATRACO_EXITO_CHANCE = 0.35
TRABAJOS_FS22 = {"hilerar": "Hilerar", "plantar": "Plantar", ...}
PAGOS_TRABAJOS_FS22 = {"hilerar": 4000, "plantar": 5000, ...}
```

Archivo completo: `ejemplos/01_economia_constantes.py`

### 15.2 Variables de entorno

Secretos y IDs de guild se leen de `kofi.env` o del entorno del sistema, nunca del repositorio:

```python
def _cargar_variable_env(nombre: str, predeterminado: str = "") -> str:
    valor = os.getenv(nombre)
    if valor:
        return valor.strip()
    # ... leer kofi.env línea a línea ...
    return predeterminado

DISCORD_BOT_TOKEN = _cargar_variable_env("DISCORD_BOT_TOKEN")
DISCORD_GUILD_ID = int(_cargar_variable_env("DISCORD_GUILD_ID", "0") or "0")
```

Archivo completo: `ejemplos/02_carga_variables_entorno.py` · Plantilla: `kofi.env.example`

### 15.3 Guard de arresto en tiendas (v2.9.4)

Antes de procesar un botón de tienda, se comprueba si el jugador está arrestado:

```python
async def bloquear_si_arrestado(interaction, banco) -> bool:
    uid = str(interaction.user.id)
    if uid not in banco or not esta_arrestado(banco[uid]):
        return False
    await interaction.response.send_message(MENSAJE_BLOQUEO_ARRESTO, ephemeral=True)
    return True
```

Archivo completo: `ejemplos/03_guard_arresto_tiendas.py`

### 15.4 Autocompletado FS22 (límite 25 de Discord)

Con más de 25 tipos de trabajo, Discord no admite `choices` estáticas. Se usa autocompletado dinámico; `@tree.command` debe ir **antes** de `@autocomplete`:

```python
@tree.command(name="registrar_contrato_fs22", ...)
@app_commands.autocomplete(tipo=_autocomplete_tipo_fs22)
async def registrar_contrato_fs22(interaction, tipo: str):
    ...
```

Archivo completo: `ejemplos/04_fs22_autocomplete.py`

### 15.5 Lock de transacciones bancarias (v2.9.4)

Todos los slash commands que mutan saldos se envuelven en un lock async para evitar double-spend:

```python
@asynccontextmanager
async def transaccion_banco(*, persistir: bool = True):
    async with bot._banco_lock:
        yield bot
        if persistir:
            guardar_json_atomico(ruta_banco(), bot.banco)
```

Archivo completo: `ejemplos/05_lock_transacciones_banco.py`

---

## 16. Historial de evolución reciente

| Versión | Tema |
|---------|------|
| 2.9.4 | Parches de seguridad económica: lock de banco, arresto en tiendas, cooldown delatar, fixes préstamos |
| 2.9.3 | Alarma de seguridad destacada en tienda legal |
| 2.9.2 | Persecución obligatoria con alarma; límite de arrestos diarios |
| 2.9.1 | Pago en mano legal; fianza desde caja fuerte |
| 2.9.0 | Alarma, persecución, arresto, fianza, seguros ampliados |
| 2.8.0 | Tiendas interactivas con catálogos fijados en canales |
| 2.7.x | Economía social (préstamos, P2P), panel pendientes, alijo sin caducidad auto |

---

## 17. Inventario de comandos por categoría

### Información general
`/version`, `/novedades`, `/tienda_vct`, `/verificar_socio_vct`, `/mis_pendientes_vct`

### Banco y cuenta
`/bal`, `/reputacion`, `/cumpleanos`, `/depositar`, `/retirar`, `/transferencia`, `/pagar`, `/aportar_vct`, `/tesoreria_vct`, `/actividad_vct`, `/cobrar`

### Tienda legal
`/tienda_legal_vct`, `/comprar_legal_vct`, `/inventario_legal_vct`, `/cobrar_inversion_vct`, `/usar_legal_vct`

### Farming Simulator 22
`/vincular_fs22`, `/declarar_trabajo_fs22`, `/perfil_fs22`, `/historial_fs22`, `/top_trabajadores`, `/que_paso`, `/trabajos_fs22`, `/pendientes_fs22`, `/aceptar_trabajo_fs22`, `/aprobar_trabajo_fs22`, `/rechazar_trabajo_fs22`, `/registrar_contrato_fs22`

### Economía social
`/prestamo_vct`, `/prestamo_responder`, `/contrato_entre_ciudadanos`, `/contrato_entre_jugadores`, `/contrato_responder`, `/seguro_vct`, `/auditoria_voluntaria`, `/licencia_sector`, `/fondo_sector`, `/fondo_sector_aportar`, `/fondo_sector_gastar`

### Crimen y submundo
`/robar`, `/atraco_planificado`, `/atraco_responder`, `/perseguir`, `/pagar_fianza_vct`, `/entregar_efectivo`, `/blanquear_fondos`, `/transferir_nrd`, `/extorsionar`, `/pagar_extorsion_vct`, `/delatar`, `/encargo_oscuro`, `/encargo_aceptar`, `/contrabando_fs22`, `/desafio_criminal`, `/desafio_responder`, `/antecedentes`

### Alijo y mercado negro
`/tienda_especial_vct`, `/inventario_vct`, `/alijo_vct`, `/ocultar_nrd`, `/recuperar_nrd`

### Juegos
`/juegos`, `/trabajo_rapido`, `/mini_trabajos_ocultos`, `/trabajos_comunitarios`, `/rasca_vct`, `/dados`, `/tragaperras`, `/giro_casino_vct`

### Trámites y moderación
`/ticket`, `/clear`, `/anuncio`, `/anuncio_directo`, `/inspeccionar`

### Administración
`/admin_saldos`, `/fondo_central`, `/admin_dar`, `/admin_retirar`, `/admin_retirar_nrd`, `/admin_incautar_alijo`, `/admin_inv`, `/admin_sync_socios`, `/estado_bot`

---

## 18. Glosario rápido

| Término | Significado |
|---------|-------------|
| **VCT** | Vanilla Center Trust |
| **NRB** | Número de Registro Bancario |
| **NRD** | Fondos no declarados (dinero negro de rol) |
| **FS22** | Farming Simulator 22 |
| **Staff / Encargado** | Jugador con permiso de registrar trabajos y gestionar sector |
| **Fondo central** | Tesorería común del servidor (impuestos) |
| **Alijo** | Bolsillo oculto de NRD |
| **P2P** | Contrato directo entre dos ciudadanos |
| **Cooldown** | Tiempo de espera antes de repetir acción |

---

## 19. Visión del proyecto

1. **Presente** — Economía completa en Discord certificando actividad FS22 manualmente  
2. **Corto plazo** — Servidor de juego dedicado para la comunidad VCT  
3. **Largo plazo** — Integración automática entre eventos en partida y economía Discord  

---

## 20. Público objetivo de este documento

Este informe está pensado para:

- **NotebookLM** y herramientas de análisis de conocimiento
- Nuevos desarrolladores o colaboradores (sin datos sensibles)
- Documentación de diseño de juego y economía de rol
- Guía de referencia para staff y diseñadores de contenido

**No sustituye** la guía rápida de jugador ni los manuales de despliegue técnico.

---

© Vanilla Center Trust [VCT] · Auditor Bancario · Documento de conocimiento público interno (sin datos de acceso)
