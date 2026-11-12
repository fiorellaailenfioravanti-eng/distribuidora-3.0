---
tipo: app
app: promociones
ruta: apps/promociones
modelos:
  - Promocion
  - CompraPromocion
  - ConsumoPromocion
depende_de:
  - "[[productos]]"
  - "[[clientes]]"
  - "[[pedidos]]"
tags:
  - app
---
# promociones

Promociones prepagas, compras y consumos con caducidad (RF-09, RF-10).

- Código: `apps/promociones/`
- Templates: `templates/promociones/`
- Grafo de código: `graphify query "promociones"`

## Relaciones
- Usa modelos de [[productos]]
- Usa modelos de [[clientes]]
- Usa modelos de [[pedidos]]

## Notas
-
