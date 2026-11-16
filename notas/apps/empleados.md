---
tipo: app
app: empleados
ruta: apps/empleados
modelos:
  - RolEmpleado
  - Empleado
depende_de:
  - "[[autenticacion]]"
tags:
  - app
---
# empleados

Empleados y roles (unificados en Fase 2).

- Código: `apps/empleados/`
- Templates: `templates/empleados/`
- Grafo de código: `graphify query "empleados"`

## Relaciones
- Usa modelos de [[autenticacion]]

## Notas
- Validaciones y correcciones: [[QA 2026-11-12]], [[Validaciones por campo]]
- 2026-11-14 ([[2026-11-14]]): baja lógica con «Empleados eliminados» y Restaurar (queda inactivo y sin acceso); foto de perfil (`Empleado.foto`, carpeta `media/empleados/`).
- 2026-11-14 ([[2026-11-14]]): roles con baja lógica («Roles eliminados» + Restaurar).
