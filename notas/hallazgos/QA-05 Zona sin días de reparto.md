---
tipo: hallazgo
estado: abierto
severidad: media
fecha: 2026-11-12
apps:
  - "[[logistica]]"
tags:
  - hallazgo
  - qa
---
# QA-05 Zona sin días de reparto

Detectado en [[QA 2026-11-12]].

## Qué pasa
Se puede crear una zona sin días de reparto. Sus clientes no reciben fecha estimada y la planificación no genera hojas para ella.

## Cómo reproducir
Logística › Zonas › nueva zona sin marcar días.

## Arreglo propuesto
Exigir al menos un día, o mostrar una advertencia en la zona y en «Direcciones sin zona».
