---
tipo: hallazgo
estado: resuelto
severidad: alta
fecha: 2026-11-12
apps:
  - "[[autenticacion]]"
tags:
  - hallazgo
  - qa
---
# QA-06 Email de producción sin configurar

Detectado en [[QA 2026-11-12]].

## Qué pasa
«Olvidé mi contraseña» ya funciona, pero en producción necesita un servidor SMTP. Sin `EMAIL_*` en el `.env`, el mail no sale.

## Cómo reproducir
Desplegar con `production.py` sin variables de email y pedir un enlace.

## Arreglo propuesto
Elegir el proveedor (Gmail con contraseña de aplicación, Brevo, Mailgun…), completar `EMAIL_BACKEND`, `EMAIL_HOST`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` y `DEFAULT_FROM_EMAIL` en el `.env` y probar un envío real.

## Resolución
2026-11-14: el administrador carga la cuenta de envío en **Configuración** ([[configuracion]]) y la prueba con «Enviar correo de prueba». El `.env` queda como respaldo.
