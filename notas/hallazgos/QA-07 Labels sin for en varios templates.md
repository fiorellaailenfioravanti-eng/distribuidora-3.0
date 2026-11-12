---
tipo: hallazgo
estado: abierto
severidad: baja
fecha: 2026-11-12
apps:
  - "[[clientes]]"
  - "[[pedidos]]"
  - "[[logistica]]"
tags:
  - hallazgo
  - qa
---
# QA-07 Labels sin for en varios templates

Detectado en [[QA 2026-11-12]].

## Qué pasa
Muchos `<label>` no están vinculados a su campo (`for=`). Afecta a lectores de pantalla y a hacer clic en la etiqueta. El popup ya lo resuelve buscando el label del bloque.

## Cómo reproducir
Clientes › Nuevo sin cuenta: el campo DNI no tiene nombre accesible.

## Arreglo propuesto
Agregar `for="{{ field.id_for_label }}"` en los templates de formularios, o pasar a un include común para renderizar campos.
