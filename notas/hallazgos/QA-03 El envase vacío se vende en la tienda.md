---
tipo: hallazgo
estado: abierto
severidad: media
fecha: 2026-11-12
apps:
  - "[[productos]]"
  - "[[carrito]]"
tags:
  - hallazgo
  - qa
---
# QA-03 El envase vacío se vende en la tienda

Detectado en [[QA 2026-11-12]].

## Qué pasa
El producto «Envase bidón 20 L» (`es_envase=True`) está activo y el cliente puede agregarlo al carrito y comprarlo como cualquier producto.

## Cómo reproducir
Tienda › Catálogo › Envase bidón 20 L › Agregar.

## Arreglo propuesto
Decidir si la venta de envases es sólo presencial. Si es así: excluir `es_envase=True` del catálogo y del carrito.
