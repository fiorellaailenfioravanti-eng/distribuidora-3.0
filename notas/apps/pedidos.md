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
- 2026-11-14 ([[2026-11-14]]): contador de pendientes en el menú y en el filtro; tabla ordenable por columna.
- 2026-11-14 ([[2026-11-14]]): para comprar alcanza con un teléfono de contacto (`TELEFONOS_MINIMOS = 1`).
- 2026-11-14 ([[2026-11-14]]): stock reservado por pedidos Pendientes/Confirmados (`services.con_stock_disponible`, `stock_reservado_por_producto`); el catálogo muestra el disponible y el inventario el reservado.
