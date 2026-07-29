import unicodedata
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Cliente, TelefonoContacto, DireccionEntrega
from .forms  import (ClienteForm, ClienteSinCuentaForm, AltaClienteConCuentaForm, TelefonoContactoForm,
                     DireccionEntregaForm, BuscarClienteForm)


# ─────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────
def es_admin_o_vendedor(user):
    return user.is_superuser or user.groups.filter(name='Vendedor').exists()


def _normalizar(texto):
    """Elimina tildes y pasa a minúsculas para búsqueda tolerante."""
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto.lower())
        if unicodedata.category(c) != 'Mn'
    )


# ─────────────────────────────────────────────────────────────
# LISTAR CLIENTES
# ─────────────────────────────────────────────────────────────
@login_required
def listar_clientes(request):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para acceder a esta sección.')
        return redirect('inicio')

    form    = BuscarClienteForm(request.GET)
    clientes = Cliente.objects.select_related('usuario').all()

    q    = request.GET.get('q', '').strip()
    tipo = request.GET.get('tipo', '').strip()

    if q:
        q_norm = _normalizar(q)
        clientes = [
            c for c in clientes
            if q_norm in _normalizar(c.usuario.get_full_name())
            or q_norm in _normalizar(c.usuario.username)
            or q_norm in _normalizar(c.usuario.email)
            or (c.dni and q_norm in _normalizar(c.dni))
        ]
    else:
        clientes = list(clientes)

    if tipo:
        clientes = [c for c in clientes if c.tipo_cliente == tipo]

    paginator = Paginator(clientes, 10)
    page_obj  = paginator.get_page(request.GET.get('page'))

    return render(request, 'clientes/listar_clientes.html', {
        'clientes': page_obj,
        'form': form,
        'q': q,
        'tipo': tipo,
    })


# ─────────────────────────────────────────────────────────────
# VER FICHA DE CLIENTE
# ─────────────────────────────────────────────────────────────
@login_required
def ver_cliente(request, pk):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para ver esta ficha.')
        return redirect('inicio')

    cliente  = get_object_or_404(Cliente, pk=pk)
    telefonos = cliente.telefonos.all()
    direcciones = cliente.direcciones.select_related('zona').all()

    form_tel = TelefonoContactoForm()
    form_dir = DireccionEntregaForm()

    # Determinar si el usuario puede ver desc_seguridad (RF-03)
    puede_ver_seguridad = es_admin_o_vendedor(request.user) or \
                          request.user.groups.filter(name='Repartidor').exists()

    return render(request, 'clientes/ver_cliente.html', {
        'cliente':            cliente,
        'telefonos':          telefonos,
        'direcciones':        direcciones,
        'form_tel':           form_tel,
        'form_dir':           form_dir,
        'puede_ver_seguridad': puede_ver_seguridad,
    })


# ─────────────────────────────────────────────────────────────
# CREAR CLIENTE MANUAL
# ─────────────────────────────────────────────────────────────
def guardar_telefonos_dinamicos(request, cliente):
    """Procesa los arrays telefono_numero[] y telefono_relacion[] del POST y crea los objetos TelefonoContacto."""
    numeros = request.POST.getlist('telefono_numero[]')
    relaciones = request.POST.getlist('telefono_relacion[]')
    
    hay_principal = False
    for i, numero in enumerate(numeros):
        numero = numero.strip()
        if numero:
            relacion = relaciones[i].strip() if i < len(relaciones) else 'Otro'
            es_principal = not hay_principal
            hay_principal = True
            TelefonoContacto.objects.create(
                cliente=cliente,
                numero=numero,
                desc_relacion=relacion or 'Otro',
                es_principal=es_principal
            )

@login_required
def crear_cliente(request):
    """
    Selector: muestra las dos opciones de alta de cliente.
    Admin/Vendedor pueden crear clientes con o sin cuenta web.
    """
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para crear clientes.')
        return redirect('apps.clientes:listar_clientes')

    return render(request, 'clientes/crear_cliente.html')


@login_required
def crear_cliente_sin_cuenta(request):
    """
    Alta de cliente sin cuenta de acceso web.
    Solo Admin/Vendedor. El cliente solo existe en la base de datos
    para gestionar pedidos físicos/telefónicos.
    """
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para crear clientes.')
        return redirect('apps.clientes:listar_clientes')

    if request.method == 'POST':
        form = ClienteSinCuentaForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            # Sin usuario vinculado
            cliente.usuario = None
            cliente.save()
            guardar_telefonos_dinamicos(request, cliente)
            messages.success(
                request,
                f'Cliente "{cliente.nombre_completo()}" creado correctamente (sin cuenta web).'
            )
            return redirect('apps.clientes:ver_cliente', pk=cliente.pk)
    else:
        form = ClienteSinCuentaForm()

    return render(request, 'clientes/crear_cliente_sin_cuenta.html', {'form': form})


@login_required
def crear_cliente_con_cuenta(request):
    """
    Alta de cliente con cuenta de acceso web.
    Usa el formulario que integra datos de usuario y cliente.
    """
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para crear clientes.')
        return redirect('apps.clientes:listar_clientes')

    if request.method == 'POST':
        form_usuario = AltaClienteConCuentaForm(request.POST, request.FILES)
        if form_usuario.is_valid():
            usuario = form_usuario.save()
            # La señal post_save crea el Cliente automáticamente y el form lo actualiza
            try:
                cliente = usuario.perfil_cliente
                guardar_telefonos_dinamicos(request, cliente)
                messages.success(
                    request,
                    f'Cliente "{cliente.nombre_completo()}" creado con cuenta web.'
                )
                return redirect('apps.clientes:ver_cliente', pk=cliente.pk)
            except Cliente.DoesNotExist:
                messages.error(request, 'Error al crear el perfil de cliente.')
    else:
        form_usuario = AltaClienteConCuentaForm()

    return render(request, 'clientes/crear_cliente_con_cuenta.html', {'form_usuario': form_usuario})


# ─────────────────────────────────────────────────────────────
# EDITAR CLIENTE (perfil de negocio)
# ─────────────────────────────────────────────────────────────
@login_required
def editar_cliente(request, pk):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para editar clientes.')
        return redirect('apps.clientes:listar_clientes')

    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos del cliente actualizados.')
            return redirect('apps.clientes:ver_cliente', pk=cliente.pk)
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'clientes/editar_cliente.html', {
        'form':    form,
        'cliente': cliente,
    })


# ─────────────────────────────────────────────────────────────
# CAMBIAR TIPO DE CLIENTE (Normal ↔ Premium)
# ─────────────────────────────────────────────────────────────
@login_required
def cambiar_tipo_cliente(request, pk):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'No tenés permiso para cambiar el tipo de cliente.')
        return redirect('apps.clientes:listar_clientes')

    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        nuevo_tipo = request.POST.get('tipo_cliente')
        if nuevo_tipo in ('Normal', 'Premium'):
            cliente.tipo_cliente = nuevo_tipo
            cliente.save()
            messages.success(
                request,
                f'Cliente actualizado a {nuevo_tipo}.'
                + (' Fiado habilitado.' if nuevo_tipo == 'Premium' else '')
            )
        else:
            messages.error(request, 'Tipo de cliente inválido.')

    return redirect('apps.clientes:ver_cliente', pk=pk)


# ─────────────────────────────────────────────────────────────
# TELÉFONOS
# ─────────────────────────────────────────────────────────────
@login_required
def agregar_telefono(request, pk):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'Sin permiso.')
        return redirect('apps.clientes:listar_clientes')

    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        form = TelefonoContactoForm(request.POST)
        if form.is_valid():
            tel = form.save(commit=False)
            tel.cliente = cliente
            tel.save()
            messages.success(request, f'Teléfono {tel.numero} agregado.')
        else:
            messages.error(request, 'Error al agregar el teléfono. Revisá los datos.')

    return redirect('apps.clientes:ver_cliente', pk=pk)


@login_required
def eliminar_telefono(request, pk):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'Sin permiso.')
        return redirect('apps.clientes:listar_clientes')

    tel        = get_object_or_404(TelefonoContacto, pk=pk)
    cliente_pk = tel.cliente.pk

    if request.method == 'POST':
        # No permitir eliminar si quedarían menos de 1 teléfono
        if tel.cliente.cantidad_telefonos() <= 1:
            messages.error(request, 'El cliente debe tener al menos 1 teléfono registrado.')
        else:
            tel.delete()
            messages.success(request, 'Teléfono eliminado.')

    return redirect('apps.clientes:ver_cliente', pk=cliente_pk)


# ─────────────────────────────────────────────────────────────
# DIRECCIONES
# ─────────────────────────────────────────────────────────────
@login_required
def agregar_direccion(request, pk):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'Sin permiso.')
        return redirect('apps.clientes:listar_clientes')

    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        form = DireccionEntregaForm(request.POST)
        if form.is_valid():
            dir_ = form.save(commit=False)
            dir_.cliente = cliente
            dir_.save()
            messages.success(request, f'Dirección "{dir_}" agregada.')
        else:
            messages.error(request, 'Error al agregar la dirección.')

    return redirect('apps.clientes:ver_cliente', pk=pk)


@login_required
def editar_direccion(request, pk):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'Sin permiso.')
        return redirect('apps.clientes:listar_clientes')

    direccion  = get_object_or_404(DireccionEntrega, pk=pk)
    cliente_pk = direccion.cliente.pk

    if request.method == 'POST':
        form = DireccionEntregaForm(request.POST, instance=direccion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dirección actualizada.')
            return redirect('apps.clientes:ver_cliente', pk=cliente_pk)
    else:
        form = DireccionEntregaForm(instance=direccion)

    return render(request, 'clientes/editar_direccion.html', {
        'form':      form,
        'direccion': direccion,
        'cliente':   direccion.cliente,
    })


@login_required
def eliminar_direccion(request, pk):
    if not es_admin_o_vendedor(request.user):
        messages.error(request, 'Sin permiso.')
        return redirect('apps.clientes:listar_clientes')

    direccion  = get_object_or_404(DireccionEntrega, pk=pk)
    cliente_pk = direccion.cliente.pk

    if request.method == 'POST':
        direccion.delete()
        messages.success(request, 'Dirección eliminada.')

    return redirect('apps.clientes:ver_cliente', pk=cliente_pk)


# ─────────────────────────────────────────────────────────────
# MI PERFIL (vista del propio cliente)
# ─────────────────────────────────────────────────────────────
@login_required
def mi_perfil_cliente(request):
    """El cliente ve sus propios datos sin información sensible."""
    try:
        cliente = request.user.perfil_cliente
    except Cliente.DoesNotExist:
        messages.info(request, 'No tenés un perfil de cliente asociado aún.')
        return redirect('inicio')

    telefonos   = cliente.telefonos.all()
    # Las direcciones se muestran SIN desc_seguridad para el propio cliente
    direcciones = cliente.direcciones.select_related('zona').all()

    return render(request, 'clientes/mi_perfil_cliente.html', {
        'cliente':    cliente,
        'telefonos':  telefonos,
        'direcciones': direcciones,
    })
