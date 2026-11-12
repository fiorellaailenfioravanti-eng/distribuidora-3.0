"""Backend de autorización: las funciones del rol del empleado como permisos de Django."""
from django.contrib.auth.backends import BaseBackend


class RolBackend(BaseBackend):
    """`user.has_perm('permisos.<funcion>')` según `roles.funciones_de(user)`.

    No autentica (eso lo hace `ModelBackend`); sólo agrega permisos.
    """

    def get_all_permissions(self, user_obj, obj=None):
        if obj is not None or not user_obj.is_active or user_obj.is_anonymous:
            return set()
        if not hasattr(user_obj, '_permisos_de_rol'):
            from .roles import funciones_de
            user_obj._permisos_de_rol = {f'permisos.{codigo}' for codigo in funciones_de(user_obj)}
        return user_obj._permisos_de_rol

    def has_perm(self, user_obj, perm, obj=None):
        return perm in self.get_all_permissions(user_obj, obj)
