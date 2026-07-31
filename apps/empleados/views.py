import unicodedata
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponseNotAllowed

from apps.clientes.views import es_admin_o_vendedor
from .models import Empleado, RolEmpleado
from .forms import EmpleadoForm, RolEmpleadoForm

def _normalizar(texto):
    if not texto:
        return ""
    texto = unicodedata.normalize('NFD', texto)
    return ''.join(c for c in texto if unicodedata.category(c) != 'Mn').lower()

@login_required
def listar_empleados(request):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('home')

    query = request.GET.get('q', '')
    rol_id = request.GET.get('rol', '')
    estado = request.GET.get('estado', '')

    empleados = Empleado.objects.select_related('rol').all()

    if query:
        q_norm = _normalizar(query)
        emp_ids = []
        for emp in empleados:
            texto = f"{emp.nombre} {emp.apellido} {emp.dni} {emp.email}"
            if q_norm in _normalizar(texto):
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
    })

@login_required
def crear_empleado(request):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('apps.empleados:listar_empleados')

    if request.method == 'POST':
        form = EmpleadoForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado creado exitosamente.')
            return redirect('apps.empleados:listar_empleados')
    else:
        form = EmpleadoForm(user=request.user)

    return render(request, 'empleados/form_empleado.html', {
        'form': form,
        'titulo': 'Crear Empleado'
    })

@login_required
def ver_empleado(request, pk):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('apps.empleados:listar_empleados')
        
    empleado = get_object_or_404(Empleado, pk=pk)
    return render(request, 'empleados/ver_empleado.html', {'empleado': empleado})

@login_required
def editar_empleado(request, pk):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('apps.empleados:listar_empleados')

    empleado = get_object_or_404(Empleado, pk=pk)
    
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado actualizado exitosamente.')
            return redirect('apps.empleados:listar_empleados')
    else:
        form = EmpleadoForm(instance=empleado, user=request.user)

    return render(request, 'empleados/form_empleado.html', {
        'form': form,
        'empleado': empleado,
        'titulo': 'Editar Empleado'
    })

@login_required
def cambiar_estado_empleado(request, pk):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('apps.empleados:listar_empleados')

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
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('apps.empleados:listar_empleados')

    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, pk=pk)
        empleado.delete()
        messages.success(request, 'Empleado eliminado exitosamente.')
        return redirect('apps.empleados:listar_empleados')
    return HttpResponseNotAllowed(['POST'])

@login_required
def listar_roles(request):
    if not request.user.is_superuser:
        messages.error(request, 'Solo los administradores principales pueden gestionar roles.')
        return redirect('apps.empleados:listar_empleados')

    roles = RolEmpleado.objects.annotate(empleados_count=Count('empleados'))
    return render(request, 'empleados/roles/listar_roles.html', {'roles': roles})

@login_required
def crear_rol(request):
    if not request.user.is_superuser:
        messages.error(request, 'Solo los administradores principales pueden gestionar roles.')
        return redirect('apps.empleados:listar_roles')

    if request.method == 'POST':
        form = RolEmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rol creado exitosamente.')
            return redirect('apps.empleados:listar_roles')
    else:
        form = RolEmpleadoForm()

    return render(request, 'empleados/roles/form_rol.html', {
        'form': form,
        'titulo': 'Crear Rol'
    })

@login_required
def editar_rol(request, pk):
    if not request.user.is_superuser:
        messages.error(request, 'Solo los administradores principales pueden gestionar roles.')
        return redirect('apps.empleados:listar_roles')

    rol = get_object_or_404(RolEmpleado, pk=pk)
    
    if request.method == 'POST':
        form = RolEmpleadoForm(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rol actualizado exitosamente.')
            return redirect('apps.empleados:listar_roles')
    else:
        form = RolEmpleadoForm(instance=rol)

    return render(request, 'empleados/roles/form_rol.html', {
        'form': form,
        'rol': rol,
        'titulo': 'Editar Rol'
    })

@login_required
def eliminar_rol(request, pk):
    if not request.user.is_superuser:
        messages.error(request, 'Solo los administradores principales pueden gestionar roles.')
        return redirect('apps.empleados:listar_roles')

    if request.method == 'POST':
        rol = get_object_or_404(RolEmpleado, pk=pk)
        if rol.empleados.exists():
            messages.error(request, 'No se puede eliminar el rol porque tiene empleados asignados.')
        else:
            rol.delete()
            messages.success(request, 'Rol eliminado exitosamente.')
        return redirect('apps.empleados:listar_roles')
    return HttpResponseNotAllowed(['POST'])
