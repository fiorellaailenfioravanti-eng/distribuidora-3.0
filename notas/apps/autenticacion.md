---
tipo: app
app: autenticacion
ruta: apps/autenticacion
modelos:
  - Usuario
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
