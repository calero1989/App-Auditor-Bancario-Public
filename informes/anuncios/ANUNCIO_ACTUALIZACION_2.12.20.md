# Auditor Bancario VCT — Enlace FS22 y bono por actividad

**Título:** El dedicated y Discord ya se hablan  
**Versión:** 2.12.19 – 2.12.20 · **Noviembre 2026**  
**Autor:** Angel del Valle Calero (calero89) · © 2026 · Vanilla Center Trust [VCT]

Borrador para revisión. Aún no publicado en Discord, Patreon ni GitHub.

---

## 1. Qué ha cambiado

El **Auditor Bancario VCT** ya ve quién entra y quién sale del **servidor dedicado de Farming Simulator 22** (G-Portal). No hace falta ningún mod en el juego.

Eso sirve para tres cosas:

1. Saber quién está en el mapa.
2. Vincular tu nick de FS22 con tu cuenta de Discord.
3. Pagar un **bono por tiempo en partida** cuando sales, en **euros VCT** (la cartera de Discord). Ese dinero **no** es el de Giants dentro del juego.

Los trabajos grandes del campo (cosechar, sembrar, etc.) **siguen igual**: se declaran con `/declarar_trabajo_fs22` y los valida un Encargado.

---

## 2. El enlace: ojos del dedicated

Mientras el dedicated está **en marcha** y hay una partida cargada, el Auditor consulta cada pocos segundos la lista oficial de Giants (quién está dentro, de cuánto es la ocupación, minutos de sesión).

- Las **entradas y salidas** se anuncian solas en el canal de staff **fs22-log**.
- Cualquier jugador puede consultar quién hay ahora con **`/estado_fs22`** (la respuesta solo la ves tú).
- Si el dedicated está parado o no hay partida, el Auditor no ve a nadie.

El bot **no** lee el chat del juego, **no** ve si alguien pisa un cultivo y **no** mueve el dinero de Giants. Son dos economías distintas.

---

## 3. Cómo vincularte (`/vincular_fs22`)

Se hace **en Discord**, no en el juego. El comando es del Auditor.

### Pasos

1. Entra al dedicated FS22 de VCT con el **nick que usas en el mapa**.
2. En Discord, en un canal del servidor VCT (lo habitual es **comandos**), escribe:

   `/vincular_fs22` → tu nick exacto (ejemplo: `calero89`)

3. Tienes que estar **dentro de la partida en ese momento**. El nick tiene que coincidir con el que muestra el servidor (mayúsculas da igual; los espacios de más se ignoran).
4. Si sale el visto bueno, ya estás vinculado. La respuesta **solo la ves tú**.

### Si falla

- «Entra al dedicated…»: no estás en el mapa, o el nick no es el de la lista del servidor. Entra, espera un minuto y vuelve a intentarlo.
- «Ese nick ya está vinculado»: otra cuenta Discord lo tiene. Habla con un Encargado.
- No uses **fs22-log** para el comando: ese canal es de anuncios (entradas, salidas y recibos), no para slash.

### Para qué sirve el vínculo

Sin `/vincular_fs22` el Auditor puede **verte** en el mapa, pero **no te paga** el bono de actividad ni te trata como jugador FS22 a efectos de trabajos (`/declarar_trabajo_fs22` ya exigía el vínculo).

Un Discord = un nick. No se puede copiar el apodo de otro.

---

## 4. Bono por actividad (2.12.20)

Cuando **sales** de la partida, el Auditor cuenta los minutos que Giants ha registrado en esa sesión y, si estás vinculado, abona euros VCT a tu **cartera de Discord**.

| Regla | Valor |
| --- | --- |
| Quién cobra | Solo cuentas con `/vincular_fs22` |
| Cuándo | Al **salir** del dedicated (no mientras sigues dentro) |
| Tarifa | **500 € por hora**, prorrateada por minuto |
| Mínimo | **15 minutos** (si sales antes, 0 €) |
| Tope | **2.000 € por día** (Europa/Madrid) |
| Ejemplos | 15 min → 125 € · 1 h → 500 € · 4 h o más → 2.000 € ese día |
| Dónde se ve | Recibo en **fs22-log** y el saldo en `/bal` |

El mismo cierre no se paga dos veces. Si el dedicated pestañea y el bot no te ve unos segundos, puede contar como salida: por eso hay mínimo de 15 minutos.

**No es un sueldo por cosechar.** Es un plus por estar en el servidor. El trabajo de campo se cobra aparte, con Encargado.

Quien no se haya vinculado puede jugar igual; en fs22-log saldrá como «sin `/vincular_fs22`» y no recibirá bono.

---

## 5. Resumen para el jugador

1. Dedicated en marcha + tú dentro del mapa.  
2. En Discord: `/vincular_fs22` con tu nick (una vez).  
3. Juega.  
4. Al salir, si has estado 15 min o más, entra el bono (hasta 2.000 €/día).  
5. Los trabajos de verdad: `/declarar_trabajo_fs22` como siempre.

Consulta **`/version`** en Discord para ver la ficha de esta versión.

---

© 2026 Angel del Valle Calero · Vanilla Center Trust [VCT]
