---
tipo: hallazgo
estado: resuelto
severidad: baja
fecha: 2026-11-12
apps:
  - "[[autenticacion]]"
tags:
  - hallazgo
  - qa
---
# QA-09 Recuperar contraseña usa vistas de clase

Detectado en [[QA 2026-11-12]].

## Qué pasa
La regla del proyecto es usar vistas de función. La recuperación usa las vistas de Django (`PasswordResetView`…), configuradas en `urls.py` con templates y formularios propios.

## Cómo reproducir
—

## Arreglo propuesto
Aceptarlo como excepción documentada (son vistas probadas de Django) o envolverlas en funciones.

## Resolución
2026-11-16 ([[2026-11-16]]): la recuperación se rehízo con vistas de función y código temporal por email (`apps/autenticacion/recuperacion.py`).
