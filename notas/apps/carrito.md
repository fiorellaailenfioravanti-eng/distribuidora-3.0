---
tipo: app
app: carrito
ruta: apps/carrito
modelos:
  - Carrito
  - ItemCarrito
depende_de:
  - "[[autenticacion]]"
  - "[[productos]]"
tags:
  - app
---
# carrito

Carrito de la tienda online.

- Código: `apps/carrito/`
- Templates: `templates/carrito/`
- Grafo de código: `graphify query "carrito"`

## Relaciones
- Usa modelos de [[autenticacion]]
- Usa modelos de [[productos]]

## Notas
- Validaciones y correcciones: [[QA 2026-11-12]], [[Validaciones por campo]]
