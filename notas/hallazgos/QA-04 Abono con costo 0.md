---
tipo: hallazgo
estado: abierto
severidad: baja
fecha: 2026-11-12
apps:
  - "[[abonos]]"
tags:
  - hallazgo
  - qa
---
# QA-04 Abono con costo 0

Detectado en [[QA 2026-11-12]].

## Qué pasa
Se puede crear un abono con costo mensual $0 (el modelo admite ≥ 0).

## Cómo reproducir
Abonos › Nuevo › Costo mensual 0.

## Arreglo propuesto
Si los comodatos gratuitos existen, dejarlo; si no, exigir > 0.
