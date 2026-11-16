---
tipo: app
app: configuracion
ruta: apps/configuracion
modelos:
  - ConfiguracionCorreo
depende_de:
  - "[[autenticacion]]"
  - "[[permisos]]"
tags:
  - app
---
# configuracion

Ajustes del sistema que el administrador cambia desde el panel (menú «Configuración», sólo superusuario).

- Código: `apps/configuracion/`
- Templates: `templates/configuracion/`
- Grafo de código: `graphify query "configuracion"`

## Correo de recuperación de contraseña
- `ConfiguracionCorreo` es una única fila: correo y nombre del remitente, servidor SMTP, puerto, TLS, usuario y contraseña de aplicación.
- Si está **activa y completa**, «Olvidé mi contraseña» envía con esa cuenta (`RecuperarContrasenaForm.send_mail`). Si no, usa el `.env` del servidor.
- La contraseña no se muestra al editar; dejarla vacía conserva la guardada. Se guarda sin los espacios con que la muestra Gmail.
- Botón **Enviar correo de prueba**: llega al email del administrador.
- Gmail: cuenta de Google → Seguridad → «Contraseñas de aplicaciones» (16 letras), servidor `smtp.gmail.com`, puerto 587, TLS.

## Relaciones
- La usa [[autenticacion]] (recuperar contraseña).
- Permiso: `es_admin` de [[permisos]].

## Notas
- Resuelve [[QA-06 Email de producción sin configurar]]. Ver [[2026-11-14]].
- 2026-11-16 ([[2026-11-16]]): el correo de prueba va a la cuenta que envía si el administrador no tiene email.
