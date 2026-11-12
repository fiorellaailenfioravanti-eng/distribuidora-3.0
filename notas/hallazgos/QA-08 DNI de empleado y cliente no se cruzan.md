---
tipo: hallazgo
estado: abierto
severidad: baja
fecha: 2026-11-12
apps:
  - "[[empleados]]"
  - "[[clientes]]"
tags:
  - hallazgo
  - qa
---
# QA-08 DNI de empleado y cliente no se cruzan

Detectado en [[QA 2026-11-12]].

## Qué pasa
El DNI es único dentro de clientes y dentro de empleados, pero un empleado y un cliente distintos pueden tener el mismo DNI.

## Cómo reproducir
Crear un empleado con el DNI de un cliente existente.

## Arreglo propuesto
Decidir si un empleado puede ser también cliente (en ese caso es correcto). Si no, validar contra ambas tablas.
