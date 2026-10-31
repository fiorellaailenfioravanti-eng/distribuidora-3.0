"""
Asignación de permisos a los grupos base del sistema.

Corrección del hallazgo H-1: el grupo 'Vendedor' no existía en la base de
datos, por lo que `groups.filter(name='Vendedor').exists()` era False para
todos los usuarios y la rama Vendedor del sistema quedaba inaccesible salvo
para el superusuario.

Este receptor se ejecuta en `post_migrate`, es idempotente y se puede volver a
ejecutar las veces que haga falta sin duplicar permisos.
"""

from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver

from .roles import GRUPO_REPARTIDOR, GRUPO_VENDEDOR, sincronizar_grupo_empleado

# Modelos que el grupo Vendedor administra desde el panel de administración.
# El acceso a las vistas del proyecto se controla aparte, con las funciones de
# `roles.py` (vistas) y su context processor `roles_usuario` (templates).
MODELOS_VENDEDOR = [
    ('productos', 'categoria'),
    ('productos', 'producto'),
    ('clientes', 'cliente'),
    ('clientes', 'direccionentrega'),
    ('clientes', 'telefonocontacto'),
    ('pedidos', 'pedido'),
    ('pedidos', 'detallepedido'),
    ('pedidos', 'pagopedido'),
    ('pedidos', 'metodopago'),
    ('empleados', 'empleado'),
    ('empleados', 'rolempleado'),
    ('logistica', 'zona'),
    ('logistica', 'barrio'),
    ('logistica', 'camion'),
    ('logistica', 'rutareparto'),
    ('logistica', 'hojaruta'),
    ('logistica', 'detallehojaruta'),
    ('clientes', 'movimientobidon'),
    ('promociones', 'promocion'),
    ('promociones', 'comprapromocion'),
    ('promociones', 'consumopromocion'),
]

# El Repartidor solo necesita registrar entregas en campo y ver su hoja de ruta.
MODELOS_REPARTIDOR = [
    ('logistica', 'detallehojaruta'),
    ('logistica', 'hojaruta'),
]

PERMISOS_VENDEDOR = ['add', 'change', 'delete', 'view']
PERMISOS_REPARTIDOR = ['add', 'change', 'view']


def _sincronizar(nombre_grupo, modelos, operaciones):
    from django.contrib.auth.models import Permission
    from django.contrib.contenttypes.models import ContentType

    grupo, _creado = Group.objects.get_or_create(name=nombre_grupo)

    content_types = []
    codigos = []
    for app_label, modelo in modelos:
        content_type = ContentType.objects.filter(
            app_label=app_label,
            model=modelo,
        ).first()
        if content_type is None:
            continue
        content_types.append(content_type)
        for operacion in operaciones:
            codigos.append(f'{operacion}_{modelo}')

    permisos = Permission.objects.filter(
        content_type__in=content_types,
        codename__in=codigos,
    )
    # `add()` y no `set()`: la sincronización es aditiva a propósito. Con
    # `set()` cada `migrate` borraba cualquier permiso que un administrador
    # hubiera asignado a mano al grupo (un cliente nuevo, un permiso de otra
    # app, un permiso retirado de la lista de arriba). Agregar nunca destruye
    # trabajo; si hay que quitar un permiso, se hace desde el panel.
    grupo.permissions.add(*permisos)


@receiver(post_migrate)
def sincronizar_permisos_grupos(sender, **kwargs):
    """Crea los grupos base y les asigna sus permisos tras cada `migrate`."""
    _sincronizar(GRUPO_VENDEDOR, MODELOS_VENDEDOR, PERMISOS_VENDEDOR)
    _sincronizar(GRUPO_REPARTIDOR, MODELOS_REPARTIDOR, PERMISOS_REPARTIDOR)


@receiver(post_save, sender='empleados.Empleado')
def sincronizar_grupo_al_guardar_empleado(sender, instance, **kwargs):
    """Alta, edición, cambio de rol o de estado del empleado → grupo correcto.

    Además, el personal no compra en la tienda: si su usuario quedó con un
    perfil de cliente vacío (lo crea la señal de alta de usuarios), se elimina.
    """
    sincronizar_grupo_empleado(instance)
    if instance.usuario_id:
        from apps.clientes.services import retirar_perfil_cliente_vacio
        retirar_perfil_cliente_vacio(instance.usuario)


@receiver(post_save, sender='empleados.RolEmpleado')
def sincronizar_grupo_al_cambiar_rol(sender, instance, created, **kwargs):
    """Si cambian los permisos de un rol, se re-sincronizan sus empleados."""
    if created:
        return
    for empleado in instance.empleados.select_related('usuario', 'rol'):
        sincronizar_grupo_empleado(empleado)
