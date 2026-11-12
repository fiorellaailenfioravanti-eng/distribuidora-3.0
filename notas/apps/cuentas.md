---
tipo: app
app: cuentas
ruta: apps/cuentas
modelos:
  - CuentaCorriente
  - MovimientoCuenta
depende_de:
  - "[[clientes]]"
  - "[[pedidos]]"
  - "[[abonos]]"
tags:
  - app
---
# cuentas

Cuentas corrientes, movimientos y morosidad (RF-14, RF-15).

- Código: `apps/cuentas/`
- Templates: `templates/cuentas/`
- Grafo de código: `graphify query "cuentas"`

## Relaciones
- Usa modelos de [[clientes]]
- Usa modelos de [[pedidos]]
- Usa modelos de [[abonos]]

## Notas
-
