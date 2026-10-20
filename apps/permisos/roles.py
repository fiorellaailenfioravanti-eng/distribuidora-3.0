"""
Fuente única de verdad para los roles y permisos del sistema.

Antes de esta corrección la misma lógica estaba replicada en cinco apps
(productos, clientes, pedidos, carrito, logistica). Eso hacía que un cambio
de política de acceso tivesse que editar cinco archivos y era la causa
directa del defecto H-5: los templates no usaban el filtro `has_group` y
evaluaban `user.groups.all.0.name`, que solo mira el primer grupo.

Reglas de negocio implementadas aquí:
  - `es_admin_o_vendedor`  →roles con poder de escritura en el panel (CRUD de
     productos, clientes, pedidos, empleados, zonas y rutas).
  - `es_repartidor`        → Delivery: solo ve sus propias hojas de ruta.
  - `puede_ver_nota_seguridad` → RNF-02. La nota de acceso al domicilio
     ("deja el portón abierto") es información sensible: la ven los
     superusuarios, los vendedores y **únicamente el repartidor que tiene
     asignada esa dirección** en alguna de sus hojas de ruta.
"""

GRUPO_VENDEDOR = 'Vendedor'
GRUPO_REPARTIDOR = 'Repartidor'


# ─────────────────────────────────────────────────────────────
# ROLES BÁSICOS
# ─────────────────────────────────────────────────────────────
def es_admin(user):
    """Superusuario de Django (staff con permisos totales)."""
    return bool(user and user.is_active and user.is_superuser)


def _en_grupo(user, nombre_grupo):
    if not user or not user.is_active:
        return False
    return user.groups.filter(name=nombre_grupo).exists()


def es_vendedor(user):
    return es_admin(user) or _en_grupo(user, GRUPO_VENDEDOR)


def es_repartidor(user):
    return _en_grupo(user, GRUPO_REPARTIDOR)


# ─────────────────────────────────────────────────────────────
# COMBINACIONES USADAS POR LAS VISTAS
# ─────────────────────────────────────────────────────────────
def es_admin_o_vendedor(user):
    """Escritura en el panel de administración."""
    return es_vendedor(user)


def es_admin_vendedor_o_repartidor(user):
    """Lectura de la sección logística (el repartidor solo ve lo suyo)."""
    return es_admin_o_vendedor(user) or es_repartidor(user)


def es_personal_interno(user):
    """Cualquier empleado de la distribuidora (excluye al cliente registrado)."""
    return es_admin_vendedor_o_repartidor(user)


# ─────────────────────────────────────────────────────────────
# EMPLEADOS
# ─────────────────────────────────────────────────────────────
def obtener_empleado(user):
    """Devuelve el perfil `empleados.Empleado` del usuario, o `None`.

    Usa el `related_name='perfil_empleado'` definido en `apps.empleados`.
    """
    if not user or not user.is_authenticated:
        return None
    return getattr(user, 'perfil_empleado', None)


def es_repartidor_asignado(user, hoja_ruta):
    """True si `user` es el chofer asignado a esa hoja de ruta."""
    empleado = obtener_empleado(user)
    if empleado is None:
        return False
    return hoja_ruta.empleado_id == empleado.id_empleado


# ─────────────────────────────────────────────────────────────
# RNF-02 — OCULTACIÓN DE INFORMACIÓN SENSIBLE
# ─────────────────────────────────────────────────────────────
def puede_ver_nota_seguridad(user, direccion):
    """¿Puede el usuario ver `direccion.desc_seguridad`?

    RNF-02: la nota es visible para superusuarios, vendedores y el repartidor
    asignado a la hoja de ruta que incluye esa dirección. Nunca para el
    propio cliente ni para un repartidor no asignado.
    """
    if es_admin_o_vendedor(user):
        return True

    if not es_repartidor(user) or direccion is None:
        return False

    # Import perezoso: `apps.logistica` referencia `apps.empleados`, así que
    # importarlo arriba del todo del módulo generaría un ciclo.
    from apps.logistica.models import DetalleHojaRuta

    return DetalleHojaRuta.objects.filter(
        direccion_entrega=direccion,
        hoja_ruta__empleado__usuario=user,
    ).exists()


# ─────────────────────────────────────────────────────────────
# ROL DEL EMPLEADO → GRUPO (auditoría H-25, decisión A-D3)
# ─────────────────────────────────────────────────────────────
GRUPOS_GESTIONADOS = (GRUPO_VENDEDOR, GRUPO_REPARTIDOR)


def sincronizar_grupo_empleado(empleado):
    """Deja al usuario del empleado sólo en el grupo que indica su rol.

    Un empleado inactivo o con un rol sin permisos queda fuera de los grupos
    gestionados. Nunca toca `is_superuser` ni otros grupos del usuario.
    """
    from django.contrib.auth.models import Group

    usuario = getattr(empleado, 'usuario', None)
    if usuario is None:
        return

    grupos = {nombre: Group.objects.get_or_create(name=nombre)[0] for nombre in GRUPOS_GESTIONADOS}
    usuario.groups.remove(*grupos.values())

    grupo = empleado.rol.grupo_permisos if empleado.rol_id else ''
    if empleado.activo and grupo in grupos:
        usuario.groups.add(grupos[grupo])
