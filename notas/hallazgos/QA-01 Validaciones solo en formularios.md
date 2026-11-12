---
tipo: hallazgo
estado: abierto
severidad: alta
fecha: 2026-11-12
apps:
  - "[[productos]]"
  - "[[clientes]]"
  - "[[empleados]]"
  - "[[logistica]]"
tags:
  - hallazgo
  - qa
---
# QA-01 Validaciones solo en formularios

Detectado en [[QA 2026-11-12]].

## Qué pasa
Las reglas nuevas (precio > 0, stock ≥ 0, formato de DNI, teléfonos, patente) están en los **formularios**. Los modelos no tienen validadores, así que el admin de Django, los comandos (`seed_demo`) o un servicio pueden guardar datos inválidos.

## Cómo reproducir
Crear un `Producto` desde el admin de Django con precio negativo, o `Producto.objects.create(precio=-1)`.

## Arreglo propuesto
Mover las reglas a `validators=[...]` de los campos del modelo (migración sin cambios en la base) y llamar a `full_clean()` en los servicios que crean objetos.
