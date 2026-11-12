from django.db import models

from .funciones import FUNCIONES


class Funcion(models.Model):
    """Ancla de los permisos de `funciones.py` (no tiene tabla propia).

    Django crea un `Permission` por cada entrada de `Meta.permissions`;
    los roles los guardan en `RolEmpleado.funciones`.
    """

    class Meta:
        managed = False
        default_permissions = ()
        permissions = FUNCIONES
        verbose_name = 'Función del sistema'
        verbose_name_plural = 'Funciones del sistema'
