---
tipo: app
app: clientes
ruta: apps/clientes
modelos:
  - Cliente
  - TelefonoContacto
  - DireccionEntrega
  - MovimientoBidon
depende_de:
  - "[[autenticacion]]"
  - "[[logistica]]"
  - "[[pedidos]]"
tags:
  - app
---
# clientes

Clientes, teléfonos, direcciones de entrega e historial de envases (RF-08).

- Código: `apps/clientes/`
- Templates: `templates/clientes/`
- Grafo de código: `graphify query "clientes"`

## Relaciones
- Usa modelos de [[autenticacion]]
- Usa modelos de [[logistica]]
- Usa modelos de [[pedidos]]

## Notas
-
