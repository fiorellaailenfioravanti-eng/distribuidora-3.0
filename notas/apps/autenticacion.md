---
tipo: app
app: autenticacion
ruta: apps/autenticacion
modelos:
  - Usuario
  - CodigoRecuperacion
depende_de: []
tags:
  - app
---
# autenticacion

Usuario personalizado (AbstractUser), login y registro.

- Código: `apps/autenticacion/`
- Templates: `templates/autenticacion/`
- Grafo de código: `graphify query "autenticacion"`

## Relaciones
- Sin dependencias de modelos con otras apps.

## Notas
- Validaciones y correcciones: [[QA 2026-11-12]], [[Validaciones por campo]]
- 2026-11-14 ([[2026-11-14]]): registro rediseñado con nombre, apellido, domicilio y teléfonos dinámicos; la recuperación de contraseña envía con la cuenta de [[configuracion]].
- 2026-11-16 ([[2026-11-16]]): recuperar contraseña con **código temporal de 6 dígitos** por email (vence en 10 min, 5 intentos, 3 por hora, guardado como HMAC) y aviso de cambio. Correos HTML en `templates/autenticacion/correos/`. Resuelve [[QA-09 Recuperar contraseña usa vistas de clase]].
