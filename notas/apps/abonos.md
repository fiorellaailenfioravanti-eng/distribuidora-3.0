---
tipo: app
app: abonos
ruta: apps/abonos
modelos:
  - Abono
depende_de:
  - "[[clientes]]"
  - "[[productos]]"
tags:
  - app
---
# abonos

Abonos mensuales de clientes (RF-05).

- Código: `apps/abonos/`
- Templates: `templates/abonos/`
- Grafo de código: `graphify query "abonos"`

## Relaciones
- Usa modelos de [[clientes]]
- Usa modelos de [[productos]]

## Notas
- Validaciones y correcciones: [[QA 2026-11-12]], [[Validaciones por campo]]
