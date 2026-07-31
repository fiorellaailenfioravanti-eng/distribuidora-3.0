import unicodedata
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Cliente, TelefonoContacto, DireccionEntrega
from .forms  import (ClienteForm, ClienteSinCuentaForm, AltaClienteConCuentaForm, TelefonoContactoForm,
                     DireccionEntregaForm, BuscarClienteForm, EditarMiPerfilForm)
from apps.pedidos.models import Pedido


# ─────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────
def es_admin_o_vendedor(user):
    return user.is_superuser or user.groups.filter(name='Vendedor').exists()


def es_dueno_o_staff(user, cliente):
    return es_admin_o_vendedor(user) or (cliente and cliente.usuario == user)


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
    pedidos = cliente.pedidos.select_related('metodo_pago').prefetch_related('detalles__producto', 'pagos').all()

    form_tel = TelefonoContactoForm()
    form_dir = DireccionEntregaForm(is_staff_or_admin=True)

    # Determinar si el usuario puede ver desc_seguridad (RF-03)
    puede_ver_seguridad = es_admin_o_vendedor(request.user) or \
                          request.user.groups.filter(name='Repartidor').exists()

    return render(request, 'clientes/ver_cliente.html', {
        'cliente':            cliente,
        'telefonos':          telefonos,
        'direcciones':        direcciones,
        'pedidos':            pedidos,
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
    cliente = get_object_or_404(Cliente, pk=pk)
    if not es_dueno_o_staff(request.user, cliente):
        messages.error(request, 'Sin permiso para agregar teléfonos a este perfil.')
        return redirect('inicio')

    if request.method == 'POST':
        form = TelefonoContactoForm(request.POST)
        if form.is_valid():
            tel = form.save(commit=False)
            tel.cliente = cliente
            tel.save()
            messages.success(request, f'Teléfono {tel.numero} agregado.')
        else:
            messages.error(request, 'Error al agregar el teléfono. Revisá los datos.')

    if cliente.usuario == request.user and not es_admin_o_vendedor(request.user):
        return redirect('apps.clientes:mi_perfil')
    return redirect('apps.clientes:ver_cliente', pk=pk)


@login_required
def eliminar_telefono(request, pk):
    tel = get_object_or_404(TelefonoContacto, pk=pk)
    cliente = tel.cliente

    if not es_dueno_o_staff(request.user, cliente):
        messages.error(request, 'Sin permiso.')
        return redirect('inicio')

    if request.method == 'POST':
        if cliente.cantidad_telefonos() <= 1:
            messages.error(request, 'Debes tener al menos 1 teléfono registrado.')
        else:
            tel.delete()
            messages.success(request, 'Teléfono eliminado.')

    if cliente.usuario == request.user and not es_admin_o_vendedor(request.user):
        return redirect('apps.clientes:mi_perfil')
    return redirect('apps.clientes:ver_cliente', pk=cliente.pk)


# ─────────────────────────────────────────────────────────────
# DIRECCIONES
# ─────────────────────────────────────────────────────────────
@login_required
def agregar_direccion(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if not es_dueno_o_staff(request.user, cliente):
        messages.error(request, 'Sin permiso para agregar direcciones a este perfil.')
        return redirect('inicio')

    # Regla de Negocio: Cada cliente solo puede tener 1 dirección de entrega.
    # Si ya posee una registrada, se redirige a editar esa única dirección.
    direccion_existente = cliente.direcciones.first()
    if direccion_existente:
        messages.info(request, 'Ya tienes un domicilio registrado. Puedes editar tus datos de entrega a continuación.')
        url_editar = reverse('apps.clientes:editar_direccion', kwargs={'pk': direccion_existente.pk})
        next_param = request.GET.get('next') or request.POST.get('next')
        if next_param:
            url_editar += f"?next={next_param}"
        return redirect(url_editar)

    next_url = request.GET.get('next') or request.POST.get('next') or ''

    is_staff = es_admin_o_vendedor(request.user)

    if request.method == 'POST':
        form = DireccionEntregaForm(request.POST, is_staff_or_admin=is_staff)
        if form.is_valid():
            dir_ = form.save(commit=False)
            dir_.cliente = cliente
            # Asignar Zona 1 por defecto si no se especificó
            if not dir_.zona:
                from apps.logistica.models import Zona
                zona_default, _ = Zona.objects.get_or_create(nombre='Zona 1')
                dir_.zona = zona_default
            dir_.es_principal = True
            dir_.save()
            messages.success(request, f'Dirección "{dir_}" agregada con éxito.')

            if next_url:
                return redirect(next_url)
            if cliente.usuario == request.user and not es_admin_o_vendedor(request.user):
                return redirect('apps.clientes:mi_perfil')
            return redirect('apps.clientes:ver_cliente', pk=pk)
        else:
            messages.error(request, 'Error al agregar la dirección. Revisá los campos.')
    else:
        form = DireccionEntregaForm(is_staff_or_admin=is_staff)

    return render(request, 'clientes/agregar_direccion.html', {
        'form': form,
        'cliente': cliente,
        'next': next_url,
    })


@login_required
def editar_direccion(request, pk):
    direccion  = get_object_or_404(DireccionEntrega, pk=pk)
    cliente    = direccion.cliente
    is_staff   = es_admin_o_vendedor(request.user)

    if not es_dueno_o_staff(request.user, cliente):
        messages.error(request, 'Sin permiso.')
        return redirect('inicio')

    if request.method == 'POST':
        form = DireccionEntregaForm(request.POST, instance=direccion, is_staff_or_admin=is_staff)
        if form.is_valid():
            dir_ = form.save(commit=False)
            if not dir_.zona:
                from apps.logistica.models import Zona
                zona_default, _ = Zona.objects.get_or_create(nombre='Zona 1')
                dir_.zona = zona_default
            dir_.save()
            messages.success(request, 'Dirección actualizada.')
            if cliente.usuario == request.user and not es_admin_o_vendedor(request.user):
                return redirect('apps.clientes:mi_perfil')
            return redirect('apps.clientes:ver_cliente', pk=cliente.pk)
    else:
        form = DireccionEntregaForm(instance=direccion, is_staff_or_admin=is_staff)

    return render(request, 'clientes/editar_direccion.html', {
        'form':      form,
        'direccion': direccion,
        'cliente':   cliente,
    })


@login_required
def eliminar_direccion(request, pk):
    direccion  = get_object_or_404(DireccionEntrega, pk=pk)
    cliente    = direccion.cliente

    if not es_dueno_o_staff(request.user, cliente):
        messages.error(request, 'Sin permiso.')
        return redirect('inicio')

    if request.method == 'POST':
        direccion.delete()
        messages.success(request, 'Dirección eliminada.')

    if cliente.usuario == request.user and not es_admin_o_vendedor(request.user):
        return redirect('apps.clientes:mi_perfil')
    return redirect('apps.clientes:ver_cliente', pk=cliente.pk)


# ─────────────────────────────────────────────────────────────
# MI PERFIL (vista del propio cliente)
# ─────────────────────────────────────────────────────────────
@login_required
def mi_perfil_cliente(request):
    """El cliente ve sus propios datos sin información sensible."""
    try:
        cliente = request.user.perfil_cliente
    except Cliente.DoesNotExist:
        cliente, _ = Cliente.objects.get_or_create(
            usuario=request.user,
            defaults={
                'nombre': request.user.first_name or request.user.username,
                'apellido': request.user.last_name or '',
                'email_contacto': request.user.email
            }
        )

    telefonos   = cliente.telefonos.all()
    direcciones = cliente.direcciones.select_related('zona').all()
    pedidos     = Pedido.objects.filter(cliente=cliente).select_related('metodo_pago').prefetch_related('detalles__producto')

    return render(request, 'clientes/mi_perfil_cliente.html', {
        'cliente':     cliente,
        'telefonos':   telefonos,
        'direcciones': direcciones,
        'pedidos':     pedidos,
    })


@login_required
def editar_mi_perfil(request):
    """Permite al cliente logueado modificar sus datos personales y foto de perfil."""
    try:
        cliente = request.user.perfil_cliente
    except Cliente.DoesNotExist:
        cliente, _ = Cliente.objects.get_or_create(
            usuario=request.user,
            defaults={
                'nombre': request.user.first_name or request.user.username,
                'apellido': request.user.last_name or '',
                'email_contacto': request.user.email
            }
        )

    if request.method == 'POST':
        form = EditarMiPerfilForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name  = form.cleaned_data['last_name']
            user.email      = form.cleaned_data['email']

            if form.cleaned_data.get('eliminar_foto'):
                user.imagen_perfil = 'usuarios/default.jpg'
            elif request.FILES.get('imagen_perfil'):
                user.imagen_perfil = request.FILES['imagen_perfil']

            user.save()

            cliente.nombre = user.first_name
            cliente.apellido = user.last_name
            cliente.email_contacto = user.email
            cliente.dni = form.cleaned_data.get('dni')
            cliente.fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento')
            cliente.save()

            messages.success(request, '¡Tus datos de perfil han sido actualizados con éxito!')
            return redirect('apps.clientes:mi_perfil')
        else:
            messages.error(request, 'Por favor revisá los datos ingresados.')
    else:
        form = EditarMiPerfilForm(initial={
            'first_name': request.user.first_name,
            'last_name':  request.user.last_name,
            'email':      request.user.email,
            'dni':        cliente.dni,
            'fecha_nacimiento': cliente.fecha_nacimiento,
        })

    return render(request, 'clientes/editar_mi_perfil.html', {
        'form': form,
        'cliente': cliente
    })

