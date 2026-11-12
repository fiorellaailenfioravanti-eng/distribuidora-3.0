"""
Fuente única de verdad para los permisos del sistema.

Cada pantalla y acción exige una **función** (`apps/permisos/funciones.py`),
por ejemplo `registrar_clientes` o `realizar_entregas`. Las funciones se
asignan a los **roles** de empleado con checkboxes (Empleados › Roles) y el
backend `apps.permisos.backends.RolBackend` las traduce a permisos de Django.

  - `puede(user, 'codigo')`        → ¿tiene esa función? (el superusuario, todas)
  - `@requiere('codigo')`          → decorador para vistas
  - `puede_ver_nota_seguridad`     → RNF-02: la nota de acceso al domicilio la
     ven quienes tienen `ver_notas_seguridad` y **sólo el repartidor asignado**
     a una hoja de ruta con esa dirección.
"""
from functools import wraps

from .funciones import POR_DEFECTO

GRUPO_VENDEDOR = 'Vendedor'
GRUPO_REPARTIDOR = 'Repartidor'
GRUPOS_GESTIONADOS = (GRUPO_VENDEDOR, GRUPO_REPARTIDOR)


# ─────────────────────────────────────────────────────────────
# FUNCIONES DEL USUARIO
# ─────────────────────────────────────────────────────────────
def funciones_de(user):
    """Códigos de las funciones del usuario (sin contar el superusuario).

    - Empleado con rol: las funciones marcadas en su rol (si está activo).
    - Usuario sin ficha de empleado pero en los grupos históricos
      «Vendedor» / «Repartidor»: las funciones por defecto de ese rol.
    """
    if not user or not user.is_authenticated or not user.is_active:
        return set()
    empleado = getattr(user, 'perfil_empleado', None)
    if empleado is not None and empleado.rol_id:
        if not empleado.activo:
            return set()
        codigos = empleado.rol.codigos_funciones()
        # Rol creado por código con tipo de acceso pero sin funciones marcadas:
        # usa las de su tipo. (Desde la pantalla, un rol sin casillas queda sin acceso.)
        if not codigos and empleado.rol.grupo_permisos in POR_DEFECTO:
            return set(POR_DEFECTO[empleado.rol.grupo_permisos])
        return codigos
    codigos = set()
    for grupo in user.groups.filter(name__in=GRUPOS_GESTIONADOS).values_list('name', flat=True):
        codigos |= POR_DEFECTO[grupo]
    return codigos


def puede(user, codigo):
    """¿El usuario tiene la función `codigo`?"""
    if not user or not user.is_authenticated or not user.is_active:
        return False
    return user.is_superuser or user.has_perm(f'permisos.{codigo}')


def puede_alguna(user, *codigos):
    return any(puede(user, codigo) for codigo in codigos)


def requiere(*codigos, destino='inicio'):
    """Decorador: exige iniciar sesión y al menos una de las funciones `codigos`."""
    def decorador(vista):
        @wraps(vista)
        def envuelta(request, *args, **kwargs):
            from django.contrib.auth.views import redirect_to_login
            from .views import sin_permiso
            if not request.user.is_authenticated:
                return redirect_to_login(request.get_full_path())
            if not puede_alguna(request.user, *codigos):
                return sin_permiso(request, destino)
            return vista(request, *args, **kwargs)
        return envuelta
    return decorador


# ─────────────────────────────────────────────────────────────
# TIPOS DE USUARIO
# ─────────────────────────────────────────────────────────────
def es_admin(user):
    """Superusuario de Django (tiene todas las funciones)."""
    return bool(user and user.is_active and user.is_superuser)


def es_personal_interno(user):
    """Cualquier empleado de la distribuidora (excluye al cliente registrado)."""
    if not user or not user.is_authenticated or not user.is_active:
        return False
    if user.is_superuser or getattr(user, 'perfil_empleado', None) is not None:
        return True
    return user.groups.filter(name__in=GRUPOS_GESTIONADOS).exists()


def usa_panel(user):
    """Entra al panel de administración (si no, su inicio es el recorrido)."""
    return puede(user, 'ver_panel')


# ─────────────────────────────────────────────────────────────
# EMPLEADOS Y HOJAS DE RUTA
# ─────────────────────────────────────────────────────────────
def obtener_empleado(user):
    """Devuelve el perfil `empleados.Empleado` del usuario, o `None`."""
    if not user or not user.is_authenticated:
        return None
    return getattr(user, 'perfil_empleado', None)


def es_repartidor_asignado(user, hoja_ruta):
    """True si `user` es el chofer asignado a esa hoja de ruta."""
    empleado = obtener_empleado(user)
    if empleado is None:
        return False
    return hoja_ruta.empleado_id == empleado.id_empleado


def puede_ver_hoja(user, hoja_ruta):
    """Ver una hoja de ruta: todas con `ver_todas_las_rutas`/`planificar_repartos`;
    con `realizar_entregas`, sólo las asignadas."""
    if puede_alguna(user, 'ver_todas_las_rutas', 'planificar_repartos'):
        return True
    return puede(user, 'realizar_entregas') and es_repartidor_asignado(user, hoja_ruta)


def puede_operar_hoja(user, hoja_ruta):
    """Registrar entregas, cobros o ventas en la calle de esa hoja."""
    if puede(user, 'planificar_repartos'):
        return True
    return puede(user, 'realizar_entregas') and es_repartidor_asignado(user, hoja_ruta)


# ─────────────────────────────────────────────────────────────
# RNF-02 — OCULTACIÓN DE INFORMACIÓN SENSIBLE
# ─────────────────────────────────────────────────────────────
def puede_ver_nota_seguridad(user, direccion):
    """¿Puede el usuario ver `direccion.desc_seguridad`?

    RNF-02: la ven quienes tienen `ver_notas_seguridad` y el repartidor
    asignado a una hoja de ruta que incluye esa dirección. Nunca el propio
    cliente ni un repartidor no asignado.
    """
    if puede(user, 'ver_notas_seguridad'):
        return True
    if not puede(user, 'realizar_entregas') or direccion is None:
        return False

    # Import perezoso: `apps.logistica` referencia `apps.empleados`.
    from apps.logistica.models import DetalleHojaRuta

    return DetalleHojaRuta.objects.filter(
        direccion_entrega=direccion,
        hoja_ruta__empleado__usuario=user,
    ).exists()


# ─────────────────────────────────────────────────────────────
# ROL DEL EMPLEADO → GRUPO (auditoría H-25, decisión A-D3)
# ─────────────────────────────────────────────────────────────
def sincronizar_grupo_empleado(empleado):
    """Deja al usuario del empleado sólo en el grupo del tipo de acceso de su rol.

    Los grupos ya no otorgan funciones a los empleados (las da el rol); se
    mantienen para el admin de Django y como compatibilidad. Nunca toca
    `is_superuser` ni otros grupos del usuario.
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
