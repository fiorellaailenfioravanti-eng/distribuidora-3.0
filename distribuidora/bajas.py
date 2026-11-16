"""
Baja lógica: los registros eliminados no se borran, se marcan con `eliminado=True`.

`SinEliminadosManager` es el manager por defecto (`objects`) de esos modelos, así
que todas las consultas (y los accesos relacionados, como `cliente.telefonos`) ya
los dejan afuera sin tocar cada vista. `todos` incluye a los eliminados: se usa
para la lista de eliminados y para restaurar.
"""
from django.db import models


class SinEliminadosManager(models.Manager):
    """Oculta los registros dados de baja (`eliminado=True`)."""

    def get_queryset(self):
        return super().get_queryset().filter(eliminado=False)


class SinHojaEliminadaManager(models.Manager):
    """Para paradas y cargas: oculta las que pertenecen a una hoja de ruta eliminada."""

    def get_queryset(self):
        return super().get_queryset().filter(hoja_ruta__eliminado=False)
