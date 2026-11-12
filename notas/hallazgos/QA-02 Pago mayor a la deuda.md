---
tipo: hallazgo
estado: abierto
severidad: media
fecha: 2026-11-12
apps:
  - "[[cuentas]]"
tags:
  - hallazgo
  - qa
---
# QA-02 Pago mayor a la deuda

Detectado en [[QA 2026-11-12]].

## Qué pasa
En una cuenta corriente se puede registrar un pago mayor al saldo deudor: queda **saldo a favor** sin aviso.

## Cómo reproducir
Cuentas › una cuenta con deuda de $1.000 › Registrar pago de $99.999.999.

## Arreglo propuesto
Decidir: (a) bloquear pagos mayores al saldo, (b) permitirlos con confirmación y mostrar «saldo a favor», o (c) dejarlo así y documentarlo.
