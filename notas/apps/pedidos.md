---
tipo: app
app: pedidos
ruta: apps/pedidos
modelos:
  - MetodoPago
  - Pedido
  - DetallePedido
  - PagoPedido
  - SuscripcionReposicion
depende_de:
  - "[[clientes]]"
  - "[[productos]]"
tags:
  - app
---
# pedidos

Pedidos, pagos parciales (RF-13), métodos de pago y reposición automática (RF-18).

- Código: `apps/pedidos/`
- Templates: `templates/pedidos/`
- Grafo de código: `graphify query "pedidos"`

## Relaciones
- Usa modelos de [[clientes]]
- Usa modelos de [[productos]]

## Notas
-
