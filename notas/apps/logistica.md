---
tipo: app
app: logistica
ruta: apps/logistica
modelos:
  - Zona
  - CalendarioExcepcion
  - Barrio
  - Camion
  - RutaReparto
  - HojaRuta
  - DetalleHojaRuta
  - CargaHojaRuta
depende_de:
  - "[[empleados]]"
  - "[[autenticacion]]"
  - "[[pedidos]]"
  - "[[clientes]]"
  - "[[productos]]"
tags:
  - app
---
# logistica

Zonas, barrios, camiones, rutas y hojas de ruta de reparto (RF-16, RF-17, RF-19).

- Código: `apps/logistica/`
- Templates: `templates/logistica/`
- Grafo de código: `graphify query "logistica"`

## Relaciones
- Usa modelos de [[empleados]]
- Usa modelos de [[autenticacion]]
- Usa modelos de [[pedidos]]
- Usa modelos de [[clientes]]
- Usa modelos de [[productos]]

## Notas
-
