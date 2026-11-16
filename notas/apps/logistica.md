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
- Validaciones y correcciones: [[QA 2026-11-12]], [[Validaciones por campo]]
- 2026-11-14 ([[2026-11-14]]): la hoja de ruta tiene campo Zona obligatorio y enlace para crear zonas.
- 2026-11-14 ([[2026-11-14]]): eliminar hojas de ruta en Borrador; lista ordenable; Zonas y Camiones con el diseño del panel.
- 2026-11-14 ([[2026-11-14]]): zonas con baja lógica («Zonas eliminadas» + Restaurar); «Sin Asignar» no se elimina.
- 2026-11-14 ([[2026-11-14]]): camiones y hojas en Borrador con baja lógica («… eliminados» + Restaurar); `HojaRuta.todos` / `Camion.todos` incluyen los eliminados.
