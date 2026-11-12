---
tipo: app
app: planta
ruta: apps/planta
modelos:
  - RecargaBidones
  - DetalleRecarga
depende_de:
  - "[[productos]]"
tags:
  - app
---
# planta

Recarga de bidones en la planta: una vez por día el recargador anota cuántos bidones llenó de cada tipo.
Suma al stock de llenos y descuenta los envases vacíos del mismo tamaño.

- Código: `apps/planta/` · Templates: `templates/planta/`
- Pantallas: `/planta/recarga/` (Recargador y Administrador) · `/planta/stock/` (Administrador y Vendedor)
- Recargables: 20 L primera y segunda marca (envase 20 L) · 10 L primera y segunda marca (envase 10 L)

## Reglas
- Una recarga por día; se corrige durante el día y se mueve sólo la diferencia.
- No deja recargar más bidones que los envases vacíos disponibles de ese tamaño.
- Un producto se marca recargable en Productos › Editar › «Se recarga en planta» + «Envase asociado».

## Relaciones
- Usa modelos de [[productos]]

## Notas
- Permisos: [[Roles y permisos]]
