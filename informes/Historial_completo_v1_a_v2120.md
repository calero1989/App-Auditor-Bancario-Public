# Informe público — Auditor Bancario VCT

**Vanilla Center Trust [VCT]** · Farming Simulator 22 · Discord

**Autor:** Angel del Valle Calero (calero89) · © 2026

Historial de actualizaciones desde el **banco VCT inicial (2026.1 / v1.0)** hasta **2.12.0**.

Resumen del ecosistema: economía legal e ilegal, FS22, inactividad, prisión, tiendas, sociedad P2P, monetización Socio VCT y **progresión por niveles XP**.

---

## v2.12.0 — Sistema de niveles y XP (Jun 2026)

- Progresión N0–N30 (legal) y C5–C20 (criminal) con bloqueo de comandos
- XP por actividad, trabajos FS22 aprobados, nómina, juegos y crimen
- Roles auto N5 Jornalero · N15 Peón · N30 postulación Encargado
- Comandos /nivel_vct · /postular_encargado · /estado_postulacion_vct · /admin_nivel
- Usuarios existentes migrados a N15; cuentas nuevas empiezan en N0

## v2.11.2 — Comandos duplicados unificados (Jun 2026)

- Eliminado /novedades — usa /version para versión e historial de cambios
- Eliminado /aprobar_trabajo_fs22 — usa /aceptar_trabajo_fs22 para aprobar pendientes

## v2.11.1 — Inactividad granja: solo sectores FS22 (Jun 2026)

- Ciclo 40 d solo para Encargados/Dueños de ganadería, agricultura y silvicultura
- Staff, moderación, soporte, supervisores e Inversor usan el ciclo ciudadano (28 d)
- Dueño Banco excluido del ciclo granja

## v2.11.0 — Inactividad Encargados y Dueños (40 días) (Jun 2026)

- Ciclo admin: multa 100k (14 d), destitución Encargado (21 d), expropiación Dueño (30 d), expulsión (40 d)
- Fase 3 Dueño: intervención bancaria y embargo de industrias — aviso en canal trámites
- DM ~24 h antes de cada fase · `/actividad_vct` distingue ciclo ciudadano vs administración

## v2.10.0 — Ciclo de inactividad 28 días (4 fases) (Jun 2026)

- Fase 1 (7 d): multa 50.000 € · Fase 2 (14 d): despido Peón/Jornalero
- Fase 3 (21 d): cese Jornalero o cuarentena sin trámites · Fase 4 (28 d): expulsión
- Aviso por DM ~24 h antes de cada fase · `/actividad_vct` muestra el ciclo completo

## v2.9.9 — Fix /admin_saldos (Jun 2026)

- Corregido error interno al generar el informe de cuentas (índice de tupla)

## v2.9.8 — Registro de ciudadanos en /admin_saldos (Jun 2026)

- /admin_saldos: lista completa en archivos .txt (saldos + registro/inactividad)
- Por usuario: altas, bajas, multas/expulsiones por inactividad y reincorporaciones
- Embed con resumen: activos vs fuera del servidor y mayores sanciones

## v2.9.7 — Expediente penitenciario en ⛓️prisión (Jun 2026)

- Al arrestar: publicación automática del expediente en el canal ⛓️prisión
- Al salir (fianza o trabajos cumplidos): publicación de limpieza de expediente

## v2.9.6 — Contrabando FS22: venta ilegal con NRD (Jun 2026)

- /contrabando_fs22 vende productos FS22 a precio elevado y otorga NRD + rep. criminal
- 16 productos por sector (autocompletado); 30 % riesgo de inspección (multa 30k)
- Cooldown 4 h entre ventas ilegales

## v2.9.5 — Atraco planificado: tope caja fuerte y bonos (Jun 2026)

- Caja fuerte en atraco exitoso: tope **100.000 €** (antes 10.000 €) con decodificador
- Organizador: **+10.000 €** NRD y **+5** rep. criminal extra si el atraco tiene éxito
- Quien aporta el decodificador: **+10.000 €** NRD y **+5** rep. criminal extra (además del reparto común)

## v2.9.4 — Parches de seguridad economía (Jun 2026)

- Fix: el modal de contrato del ticket ya no abona dinero automáticamente
- Lock del banco en comandos y tiendas (evita carreras y double-spend)
- Reclusos bloqueados en catálogos de tienda fijados
- /delatar con cooldown 24 h global y por objetivo
- Fix: préstamos y desafíos no se borran si falla la validación
- /perseguir consume la persecución al instante (no doble uso)

## v2.9.3 — Alarma destacada en tienda legal (Jun 2026)

- Catálogo 🏪-tienda_legal_vct muestra la Alarma de seguridad como novedad 🆕

## v2.9.2 — Persecución con alarma obligatoria (Jun 2026)

- /perseguir solo con Alarma de seguridad VCT instalada
- Seguro Antirobo indemniza solo si la póliza está contratada y activa
- Máximo 1 arresto por ladrón y día (recuperación sí, prisión no repetida)

## v2.9.1 — /pagar y fianza desde caja (Jun 2026)

- /pagar_fianza_vct: elige pagar desde cartera legal o caja fuerte
- /pagar: entregar dinero legal en mano (sin impuesto de transferencia)

## v2.9.0 — Alarma, persecución y arresto (Jun 2026)

- Alarma de seguridad (tienda legal): baja éxito de /robar al 25 %
- /perseguir en 24 h tras robo o intento; /denunciar desactivado de momento
- Arresto, fianza 100.000 €, trabajos comunitarios y rol ⛓️| Recluso de VCT
- /seguro_vct ampliado: pólizas Antirobo (70 %) y Fianza judicial (50 % fianza)

## v2.8.0 — Tiendas interactivas con catálogo fijado (Jun 2026)

- /tienda_legal_vct, /tienda_especial_vct y /tienda_vct abren menús interactivos para comprar
- Catálogos persistentes fijados en 🏪-tienda_legal_vct, ⛺-tienda_especial_vct y 💳-tienda_vct
- /comprar_legal_vct usa autocomplete en lugar de lista fija de productos

## v2.7.9 — Alijo sin caducidad automática (Jun 2026)

- El alijo ya no se incauta solo a los 7 días; solo NRD visible caduca
- Mensajes sin referencia a visibilidad en /admin_saldos

## v2.7.8 — Claridad en /transferencia (Jun 2026)

- /transferencia explica cartera vs caja y muestra el máximo neto transferible si falta saldo

## v2.7.7 — /denunciar restringido (Jun 2026)

- Solo Fundador, Dueños, administradores o suscriptores Socio VCT (/tienda_vct) pueden denunciar

## v2.7.6 — Contratos P2P más seguros (Jun 2026)

- Fix: el contrato no se borra si el pagador no tiene saldo o responde quien no es el receptor
- /contrato_entre_ciudadanos y alias /contrato_entre_jugadores avisan por canal y DM
- /contrato_responder con motivo al rechazar y alertas DM al aceptar o rechazar

## v2.7.5 — FS22: cooperación y cobro al aceptar (Jun 2026)

- Ayudantes en /registrar_contrato_fs22 cobran cooperación independiente (+€ y rep) en el recibo
- /aceptar_trabajo_fs22 paga al trabajador; alerta DM al cobrar o al rechazar con motivo
- /aprobar_trabajo_fs22 sigue como alias de aceptar

## v2.7.4 — Fix /admin_saldos (Jun 2026)

- Corregido error al listar cuentas con extorsión activa

## v2.7.3 — Alerta en préstamos (Jun 2026)

- /prestamo_vct avisa al prestamista en canal y por DM con detalle e ID de respuesta

## v2.7.2 — Pendientes se limpian al completar (Jun 2026)

- Tras denunciar o pagar extorsión desaparece de /mis_pendientes_vct
- Sin duplicados ni re-aparición de denuncias ya presentadas

## v2.7.1 — Fix denunciar extorsión (Jun 2026)

- Sincroniza denuncia desde extorsión activa si faltaba el registro
- Mensaje claro con el extorsionista correcto al usar /denunciar

## v2.7.0 — Atraco con invitación a cómplices (Jun 2026)

- /atraco_planificado envía invitación; cómplices responden con /atraco_responder
- El atraco se ejecuta cuando todos responden y hay mínimo 2 participantes
- Plazo de respuesta: 24 h; visible en /mis_pendientes_vct

## v2.6.9 — Panel de pendientes (Jun 2026)

- Nuevo /mis_pendientes_vct: extorsión, denuncia, préstamos, contratos, desafíos, encargos y FS22

## v2.6.8 — Denunciar extorsiones (Jun 2026)

- /denunciar cubre extorsión: multa 35k (+15k si hay antecedentes), +3 rep. trabajador a la víctima
- Ventana de denuncia al recibir extorsión o tras represalia por impago

## v2.6.7 — Atraco planificado: decodificador y cómplices (Jun 2026)

- Caja fuerte robable si un cómplice lleva Decodificador Digital
- Cooldown de atraco solo para el organizador; cómplice puede liderar otro atraco

## v2.6.6 — Fix encargos oscuros (Jun 2026)

- Corregido bug que borraba encargos al guardar el calendario automático
- Cobro NRD solo tras publicar; IDs normalizados (EO-1 = EO-00001)

## v2.6.5 — Extorsión con alerta y represalia (Jun 2026)

- /extorsionar avisa a la víctima (canal + DM); plazo 24 h
- Impago: gran robo automático (cartera/caja) a favor del extorsionista

## v2.6.4 — Decodificador y Caja Fuerte (Jun 2026)

- El Decodificador Digital hackea la Caja Fuerte aunque la víctima tenga cartera vacía

## v2.6.3 — Denuncia anónima con aviso al denunciado (Jun 2026)

- /denunciar envía alerta anónima por DM al denunciado con el importe de la multa

## v2.6.2 — Alerta de desafío criminal (Jun 2026)

- /desafio_criminal avisa al retado con mención en canal y DM si está permitido

## v2.6.1 — Atraco planificado: víctima explícita (Jun 2026)

- /atraco_planificado: campo victima con autocompletado (Auditor o ciudadanos ≥100k €)

## v2.6.0 — Economía social y crimen organizado (Jun 2026)

- Préstamos, contratos P2P, seguro, auditoría voluntaria, fondo sector
- Atraco planificado, denunciar, extorsión, transferir NRD, delatar
- Encargos oscuros en boletín del Estado, contrabando FS22, desafío criminal

## v2.5.5 — Tesorería del Auditor — aportes y robos (Jun 2026)

- /aportar_vct dona dinero legal a la cartera del Auditor (robable con /robar)
- /tesoreria_vct consulta el saldo público de la tesorería
- La tesorería del bot no paga impuesto semanal (NRB VCT-BANCO)

## v2.5.4 — Dificultad en trabajo rápido y submundo (Jun 2026)

- /trabajo_rapido: pago y rep. trabajador aleatorios según dificultad del trabajo
- /mini_trabajos_ocultos: NRD y rep. criminal aleatorios según dificultad del encargo

## v2.5.3 — Trabajos comunitarios variables (Jun 2026)

- /trabajos_comunitarios reduce rep. criminal al azar según la dificultad del trabajo (1 a 8 puntos)
- Cooldown de trabajos comunitarios: 2 horas

## v2.5.2 — Fix Peón Agrícola en /cobrar (Jun 2026)

- Reconoce el rol Peón Agrícola (agrícola con tilde) además de Peón Agricultura

## v2.5.1 — Fix /cobrar (datetime en nómina) (Jun 2026)

- Corregido NameError que impedía cobrar sueldo por roles

## v2.5.0 — Alijo NRD — ocultar fondos no declarados (Jun 2026)

- Maletín offshore en /tienda_especial_vct desbloquea el alijo
- /ocultar_nrd (comisión 30 %) · /recuperar_nrd · /alijo_vct
- /admin_incautar_alijo para inspección profunda del staff
- Aviso DM a los 5 días sin movimiento; incautación automática a los 7

## v2.4.2 — Fix /cobrar con varios roles de trabajo (Jun 2026)

- Reconoce 🧤 Jornalero, Peón Agricultura y jornaleros por sector al cobrar nómina
- El recibo lista todos los rangos con sueldo detectados

## v2.4.1 — Corrección menú /comprar_legal_vct (Jun 2026)

- El selector de producto vuelve a cargar (lista fija en lugar de autocompletado roto)

## v2.4.0 — Tienda legal Banco VCT (5 paquetes) (May 2026)

- /tienda_legal_vct: financiero, agrícola/FS22, negocio, consumibles, coleccionables
- /comprar_legal_vct · /inventario_legal_vct · /cobrar_inversion_vct · /usar_legal_vct
- Bonos en trabajos FS22, /trabajo_rapido, transferencias (cuenta premium) y juegos (seguro)

## v2.3.1 — Comando /tienda_vct con botón de suscripción (May 2026)

- /tienda_vct: botón morado Suscribirse (SKU Socio VCT) + enlace a la tienda
- Para cuando al pinchar el bot solo sale Añadir aplicación o Mensaje

## v2.3.0 — Suscripción Discord Socio VCT (~5 €) (May 2026)

- SKU Socio VCT: el bot asigna el rol ⭐ | Socio VCT al suscribirse
- /verificar_socio_vct para actualizar el rol tras comprar
- /admin_sync_socios para sincronización manual (staff)
- Sincronización automática al arrancar y cada hora

## v2.2.2 — Más renombres Discord + limpieza de comandos fantasmas (May 2026)

- /tienda_especial_vct (antes /comercio_oculto)
- /admin_retirar_nrd (antes /admin_decomisar)
- /giro_casino_vct (antes /ruleta; color Oscuro en lugar de Negro)
- Al arrancar se eliminan comandos globales huérfanos (p. ej. /regla)

## v2.2.1 — Comandos renombrados (políticas Discord) (May 2026)

- /inventario_vct (antes /inv)
- /comercio_oculto (antes /mercado_negro)
- /entregar_efectivo (antes /pagar)
- /blanquear_fondos (antes /lavar)
- /mini_trabajos_ocultos (antes /trabajos_submundo)
- /admin_saldos (antes /admin_balances)
- /admin_decomisar (antes /admin_incautar)

## v2.2.0 — Sanciones automáticas por inactividad (May 2026)

- 7 días sin actividad: multa automática de 50.000 € (cartera puede quedar negativa)
- 14 días sin actividad: expulsión del servidor (autorizada)
- Actividad: mensajes en Discord y uso de comandos del Auditor
- /actividad_vct para consultar días inactivos y plazos
- Exentos: Fundador y administradores

## v2.1.0 — FS22 con menos carga para staff (sin mods) (May 2026)

- /declarar_trabajo_fs22: el jugador declara; el pago queda pendiente
- /aprobar_trabajo_fs22: encargado aprueba en un paso y paga solo
- /pendientes_fs22 y /que_paso por sector (multigranja)
- Sectores: banco, ganadería, agricultura, silvicultura
- /registrar_contrato_fs22 sigue disponible para registros completos al instante

## v2.0.0 — Generación 2 — estable en servidor (May 2026)

- Bot reorganizado (más fiable 24/7 en VPS)
- Comando /version con historial de novedades
- Versión visible en recibos y avisos del banco
- Panel privado de consulta para administración
- Copias de seguridad y reinicio limpio reforzados

## v2026.3 — Consultas y moderación (May 2026)

- /antecedentes y revisión de inventario activo
- /clear en trámites y filtro anti-spam básico
- Nombres de Discord sincronizados en cuentas del banco
- /estado_bot para administradores

## v2026.2 — Automatización y FS22 (May 2026)

- FS22: trabajos, contratos y economía agrícola en el banco
- Backup automático cada hora del banco
- Resumen diario (21:00) y ranking semanal (lunes)
- Impuesto semanal, avisos de nómina y bonos cumpleaños/aniversario
- Dinero negro caduca a los 7 días sin lavar
- Alertas de posibles multicuentas al unirse al servidor

## v2026.1 — Banco VCT y economía base (2026)

- Cuentas: cartera, caja fuerte, NRB y /bal
- /cobrar por roles, /pagar, fondo central e impuestos
- Dinero negro, /robar, /lavar y mercado negro
- Ko-fi: membresías Ciudadano y Socio preferente
- Juegos: tragaperras, dados, rasca
- Centro de trámites: tickets, contratos y apelaciones
- Marca Vanilla Center Trust [VCT] en recibos

---

## Enlaces

- **Patreon:** https://patreon.com/calero89
- **GitHub público (docs):** https://github.com/calero1989/App-Auditor-Bancario-Public
- **Versión en producción:** 2.12.0
- **Comando en Discord:** `/version` · `/nivel_vct`

*Informe público sin credenciales ni datos personales de jugadores.*

*© 2026 Angel del Valle Calero · Vanilla Center Trust [VCT]*