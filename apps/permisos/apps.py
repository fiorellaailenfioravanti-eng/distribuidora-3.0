"""
App sin modelos: centraliza los roles del sistema.

Se registra en `INSTALLED_APPS` solo para poder enganchar el receptor
`post_migrate` que asigna los permisos a los grupos base.

Por qué `post_migrate` y no una migración de datos: Django crea las filas de
`auth_permission` en su propio receptor `post_migrate`, que se ejecuta
**después** de todas las migraciones. Una migración `RunPython` que corre
durante `migrate` no encuentra todavía los permisos de las apps propias y los
omite en silencio. Es el mismo motivo por el que el propio Django no usa
migraciones para esto.
"""

from django.apps import AppConfig


class PermisosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.permisos'
    verbose_name = 'Permisos y Roles'

    def ready(self):
        from . import signals  # noqa: F401
