"""
Copia los datos de `logistica.Empleado` / `logistica.RolEmpleado` a los modelos
canónicos de `apps.empleados`.

Corrige los hallazgos H-2 y H-3: `Empleado` y `RolEmpleado` estaban definidos
por duplicado en dos apps, generando cuatro tablas
(`empleados_empleado`, `empleados_rolempleado`, `logistica_empleado`,
`logistica_rolempleado`). Como `logistica_empleado` quedó vacía, el selector de
repartidor de `HojaRutaForm` nunca tenía opciones y **no se podía crear
ninguna hoja de ruta**.

`apps.empleados` pasa a ser la única fuente de verdad: concentra nombre,
apellido, DNI, celular y email, mientras que el modelo duplicado de logística
solo tenía `usuario`, `rol` y `activo`.

Los roles se emparejan por texto: `RolEmpleado.descripcion` (logistica) contra
`RolEmpleado.nombre` (empleados). Si no hay coincidencia se crea el rol
equivalente en `apps.empleados`.
"""

from django.db import migrations


def _nombre_completo_de_usuario(usuario):
    completo = (usuario.get_full_name() or '').strip()
    partes = completo.split()
    if len(partes) >= 2:
        return partes[0], ' '.join(partes[1:])
    if partes:
        return partes[0], ''
    return usuario.username, ''


def copiar_empleados_logistica(apps, schema_editor):
    EmpleadoLogistica = apps.get_model('logistica', 'Empleado')
    RolLogistica = apps.get_model('logistica', 'RolEmpleado')
    Empleado = apps.get_model('empleados', 'Empleado')
    RolEmpleado = apps.get_model('empleados', 'RolEmpleado')

    # 1) Roles: emparejar por texto, creando el que falte.
    mapa_roles = {}
    for rol in RolLogistica.objects.all():
        equivalente, _ = RolEmpleado.objects.get_or_create(
            nombre=rol.descripcion[:60],
            defaults={'descripcion': rol.descripcion},
        )
        mapa_roles[rol.id_rol] = equivalente

    # 2) Empleados.
    for emp in EmpleadoLogistica.objects.select_related('usuario', 'rol').all():
        if Empleado.objects.filter(usuario_id=emp.usuario_id).exists():
            continue

        rol_destino = mapa_roles.get(emp.rol_id)
        if rol_destino is None:
            rol_destino, _ = RolEmpleado.objects.get_or_create(
                nombre='Sin rol asignado',
                defaults={'descripcion': 'Rol provisorio creado al unificar empleados'},
            )

        nombre, apellido = _nombre_completo_de_usuario(emp.usuario)

        Empleado.objects.create(
            usuario_id=emp.usuario_id,
            nombre=nombre,
            apellido=apellido,
            # El modelo original no guardaba DNI. Se genera un valor único
            # provisional para respetar la restricción; el dato real se carga
            # desde la ficha del empleado.
            dni=f'SIN-DNI-{emp.pk:04d}',
            email=emp.usuario.email or '',
            activo=emp.activo,
            rol=rol_destino,
        )


def revertir_empleados_logistica(apps, schema_editor):
    Empleado = apps.get_model('empleados', 'Empleado')
    Empleado.objects.filter(dni__startswith='SIN-DNI-').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('logistica', '0004_remove_detallehojaruta_direccion_and_more'),
        ('empleados', '0002_rename_fecha_alta_remove_fecha_ingreso'),
    ]

    operations = [
        migrations.RunPython(
            copiar_empleados_logistica,
            revertir_empleados_logistica,
        ),
    ]
