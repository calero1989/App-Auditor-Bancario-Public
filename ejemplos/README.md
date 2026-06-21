# Ejemplos de código — Auditor Bancario VCT

Fragmentos **ilustrativos** extraídos del bot real, depurados para publicación:

- Sin tokens, contraseñas ni rutas de servidor
- Sin IDs numéricos de canales ni guild de Discord
- Sin lógica criminal completa ni comandos de administración

El código de producción permanece en el repositorio privado. Estos archivos sirven para entender **patrones de diseño** y **reglas de economía** codificadas.

| Archivo | Tema |
|---------|------|
| [01_economia_constantes.py](01_economia_constantes.py) | Tasas, impuestos, límites y catálogo FS22 (extracto) |
| [02_carga_variables_entorno.py](02_carga_variables_entorno.py) | Lectura de `kofi.env` sin secretos reales |
| [03_guard_arresto_tiendas.py](03_guard_arresto_tiendas.py) | Bloqueo de botones/menús si el jugador está arrestado |
| [04_fs22_autocomplete.py](04_fs22_autocomplete.py) | Autocompletado de trabajos FS22 (límite 25 de Discord) |
| [05_lock_transacciones_banco.py](05_lock_transacciones_banco.py) | Lock async para evitar carreras en mutaciones del banco |

© 2026 Angel del Valle Calero · Vanilla Center Trust [VCT] · Fragmentos de referencia pública
