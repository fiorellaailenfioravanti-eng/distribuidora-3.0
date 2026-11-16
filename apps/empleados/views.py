from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import HttpResponseNotAllowed

from apps.permisos.views import sin_permiso
from apps.permisos.roles import puede, requiere
from distribuidora.utils import normalizar_texto

from .models import Empleado, RolEmpleado
from .forms import EmpleadoForm, RolEmpleadoForm

@login_required
def listar_empleados(request):
    if not puede(request.user, 'gestionar_empleados'):
        return sin_permiso(request)

    query = request.GET.get('q', '')
    rol_id = request.GET.get('rol', '')
    estado = request.GET.get('estado', '')

    empleados = Empleado.objects.select_related('rol').filter(eliminado=False)
    eliminados = Empleado.objects.select_related('rol').filter(eliminado=True)

    if query:
        q_norm = normalizar_texto(query)
        emp_ids = []
        for emp in empleados:
            texto = f"{emp.nombre} {emp.apellido} {emp.dni} {emp.email}"
            if q_norm in normalizar_texto(texto):
                emp_ids.append(emp.id_empleado)
        empleados = empleados.filter(id_empleado__in=emp_ids)

    if rol_id:
        empleados = empleados.filter(rol_id=rol_id)
        
    if estado == 'activo':
        empleados = empleados.filter(activo=True)
    elif estado == 'inactivo':
        empleados = empleados.filter(activo=False)

    paginator = Paginator(empleados, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    roles = RolEmpleado.objects.all()

    return render(request, 'empleados/listar_empleados.html', {
        'empleados': page_obj,
        'query': query,
        'rol_id': rol_id,
        'estado': estado,
        'roles': roles,
        'eliminados': eliminados,
    })

@login_required
def crear_empleado(request):
    if not puede(request.user, 'gestionar_empleados'):
        return sin_permiso(request)

    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado creado exitosamente.')
            return redirect('apps.empleados:listar_empleados')
    else:
        form = EmpleadoForm(user=request.user)

    return render(request, 'empleados/form_empleado.html', {
        'form': form,
        'titulo': 'Crear Empleado',
        'funciones_por_rol': _funciones_por_rol(),
    })

@login_required
def ver_empleado(request, pk):
    if not puede(request.user, 'gestionar_empleados'):
        return sin_permiso(request)
        
    empleado = get_object_or_404(Empleado, pk=pk)
    return render(request, 'empleados/ver_empleado.html', {'empleado': empleado})

@login_required
def editar_empleado(request, pk):
    if not puede(request.user, 'gestionar_empleados'):
        return sin_permiso(request)

    empleado = get_object_or_404(Empleado, pk=pk)
    
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES, instance=empleado, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado actualizado exitosamente.')
            return redirect('apps.empleados:listar_empleados')
    else:
        form = EmpleadoForm(instance=empleado, user=request.user)

    return render(request, 'empleados/form_empleado.html', {
        'form': form,
        'empleado': empleado,
        'titulo': 'Editar Empleado',
        'funciones_por_rol': _funciones_por_rol(),
    })

@login_required
def cambiar_estado_empleado(request, pk):
    if not puede(request.user, 'gestionar_empleados'):
        return sin_permiso(request)

    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, pk=pk)
        empleado.activo = not empleado.activo
        empleado.save()
        estado = "activado" if empleado.activo else "desactivado"
        messages.success(request, f'El empleado ha sido {estado} exitosamente.')
        return redirect('apps.empleados:listar_empleados')
    return HttpResponseNotAllowed(['POST'])

@login_required
def eliminar_empleado(request, pk):
    if not puede(request.user, 'gestionar_empleados'):
        return sin_permiso(request)

    # Baja lógica (como los productos): no se borra, queda oculto y sin acceso.
    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, pk=pk)
        empleado.dar_de_baja()
        messages.success(request, f'«{empleado.nombre_completo()}» se eliminó. '
                                  'Lo podés restaurar desde «Empleados eliminados».')
        return redirect('apps.empleados:listar_empleados')
    return HttpResponseNotAllowed(['POST'])


@login_required
def restaurar_empleado(request, pk):
    if not puede(request.user, 'gestionar_empleados'):
        return sin_permiso(request)

    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, pk=pk)
        empleado.restaurar()
        messages.success(request, f'«{empleado.nombre_completo()}» volvió a la lista de empleados.')
        return redirect('apps.empleados:listar_empleados')
    return HttpResponseNotAllowed(['POST'])

def _funciones_por_rol():
    """{id_rol: [descripción de cada función]} para mostrar qué puede hacer cada rol."""
    from apps.permisos.funciones import FUNCIONES, POR_DEFECTO
    nombres = dict(FUNCIONES)
    datos = {}
    for rol in RolEmpleado.objects.prefetch_related('funciones'):
        codigos = rol.codigos_funciones() or set(POR_DEFECTO.get(rol.grupo_permisos, ()))
        datos[rol.pk] = [nombres[c] for c, _ in FUNCIONES if c in codigos]
    return datos


def _plantillas():
    """Roles base para precargar las casillas: [(nombre, 'cod1,cod2,...'), ...]."""
    from apps.permisos.funciones import CODIGOS, POR_DEFECTO
    return [(nombre, ','.join(c for c in CODIGOS if c in codigos)) for nombre, codigos in POR_DEFECTO.items()]


@login_required
def listar_roles(request):
    if not puede(request.user, 'gestionar_empleados'):
        return sin_permiso(request)

    roles = RolEmpleado.objects.annotate(
        empleados_count=Count('empleados', filter=Q(empleados__eliminado=False), distinct=True),
        funciones_count=Count('funciones', distinct=True),
    ).prefetch_related('funciones')
    return render(request, 'empleados/roles/listar_roles.html', {
        'roles': roles,
        'eliminados': RolEmpleado.todos.filter(eliminado=True).order_by('nombre'),
    })

@login_required
def crear_rol(request):
    if not puede(request.user, 'gestionar_empleados'):
        return sin_permiso(request)

    if request.method == 'POST':
        form = RolEmpleadoForm(request.POST, usuario=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rol creado exitosamente.')
            return redirect('apps.empleados:listar_roles')
    else:
        form = RolEmpleadoForm(usuario=request.user)

    return render(request, 'empleados/roles/form_rol.html', {
        'form': form,
        'titulo': 'Nuevo rol',
        'plantillas': _plantillas(),
    })

@login_required
def editar_rol(request, pk):
    if not puede(request.user, 'gestionar_empleados'):
        return sin_permiso(request)

    rol = get_object_or_404(RolEmpleado, pk=pk)
    
    if request.method == 'POST':
        form = RolEmpleadoForm(request.POST, instance=rol, usuario=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rol actualizado exitosamente.')
            return redirect('apps.empleados:listar_roles')
    else:
        form = RolEmpleadoForm(instance=rol, usuario=request.user)

    return render(request, 'empleados/roles/form_rol.html', {
        'form': form,
        'rol': rol,
        'titulo': f'Permisos del rol «{rol.nombre}»',
        'plantillas': _plantillas(),
    })

@login_required
def eliminar_rol(request, pk):
    if not puede(request.user, 'gestionar_empleados'):
        return sin_permiso(request)

    if request.method == 'POST':
        rol = get_object_or_404(RolEmpleado, pk=pk)
        if rol.empleados.filter(eliminado=False).exists():
            messages.error(request, 'No se puede eliminar el rol porque tiene empleados asignados.')
        else:
            # Baja lógica: deja de ofrecerse al cargar empleados.
            rol.eliminado = True
            rol.save(update_fields=['eliminado'])
            messages.success(request, f'Rol «{rol.nombre}» eliminado. Lo podés restaurar desde «Roles eliminados».')
        return redirect('apps.empleados:listar_roles')
    return HttpResponseNotAllowed(['POST'])


@login_required
def restaurar_rol(request, pk):
    if not puede(request.user, 'gestionar_empleados'):
        return sin_permiso(request)
    if request.method == 'POST':
        rol = get_object_or_404(RolEmpleado.todos, pk=pk)
        rol.eliminado = False
        rol.save(update_fields=['eliminado'])
        messages.success(request, f'Rol «{rol.nombre}» restaurado.')
        return redirect('apps.empleados:listar_roles')
    return HttpResponseNotAllowed(['POST'])
