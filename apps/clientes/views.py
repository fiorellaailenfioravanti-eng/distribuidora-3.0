from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils.http import url_has_allowed_host_and_scheme, urlencode

from .models import Cliente, TelefonoContacto, DireccionEntrega
from .forms  import (ClienteForm, ClienteSinCuentaForm, AltaClienteConCuentaForm, TelefonoContactoForm,
                     DireccionEntregaForm, BuscarClienteForm, EditarMiPerfilForm, MovimientoBidonForm)
from apps.autenticacion.models import Usuario
from apps.pedidos.models import Pedido
from django.core.exceptions import ValidationError

from distribuidora.utils import errores_en_texto, normalizar_texto
from apps.promociones.forms import VenderPromocionForm
from apps.promociones.services import compras_vigentes
from . import services as servicios_clientes
from apps.permisos.views import solo_clientes
from apps.permisos.roles import puede, puede_ver_nota_seguridad, requiere


# ─────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────
def _contexto_suscripcion(cliente):
    """Pedido automático de reposición (RF-18) para la ficha y «Mi perfil»."""
    from apps.pedidos.forms import SuscripcionForm
    from apps.pedidos.models import SuscripcionReposicion
    suscripcion = SuscripcionReposicion.objects.filter(cliente=cliente).select_related('ultimo_pedido').first()
    return {'suscripcion': suscripcion, 'form_suscripcion': SuscripcionForm(instance=suscripcion, cliente=cliente)}


def es_dueno_o_staff(user, cliente):
    return puede(user, 'registrar_clientes') or (cliente and cliente.usuario == user)


# ─────────────────────────────────────────────────────────────
# LISTAR CLIENTES
# ─────────────────────────────────────────────────────────────
def _texto_buscable(cliente):
    partes = [cliente.nombre, cliente.apellido, cliente.dni, cliente.email_contacto]
    if cliente.usuario is not None:
        u = cliente.usuario
        partes += [u.get_full_name(), u.username, u.email]
    return normalizar_texto(' '.join(p for p in partes if p))


def _valor(cliente, atributo):
    valor = getattr(cliente, atributo)
    return valor() if callable(valor) else valor


# Columnas ordenables del directorio: clave de la URL → valor de cada cliente.
# Se ordena en Python (la lista ya se filtra así) y antes de paginar, para que
# el orden abarque a todos los clientes y no sólo a la página visible.
ORDEN_CLIENTES = {
    'cliente':    lambda c: normalizar_texto(_valor(c, 'nombre_completo') or ''),
    'email':      lambda c: normalizar_texto(_valor(c, 'email_display') or '~'),
    'dni':        lambda c: (c.dni or '').zfill(15) if c.dni else '~',
    'tipo':       lambda c: c.tipo_cliente or '',
    'telefonos':  lambda c: _valor(c, 'cantidad_telefonos') or 0,
    'domicilios': lambda c: _valor(c, 'cantidad_direcciones') or 0,
    'bidones':    lambda c: c.bidones_prestados or 0,
    'alta':       lambda c: c.fecha_alta.isoformat() if c.fecha_alta else '',
}


def _columnas_ordenables(q, tipo, orden, direccion):
    """URL e ícono de cada encabezado: un clic ordena A→Z, otro invierte."""
    columnas = {}
    for clave in ORDEN_CLIENTES:
        activa = clave == orden
        siguiente = 'desc' if activa and direccion == 'asc' else 'asc'
        columnas[clave] = {
            'url': '?' + urlencode({'q': q, 'tipo': tipo, 'orden': clave, 'dir': siguiente}),
            'dir': direccion if activa else '',
        }
    return columnas


@login_required
def listar_clientes(request):
    if not puede(request.user, 'ver_clientes'):
        messages.error(request, 'No tenés permiso para acceder a esta sección.')
        return redirect('inicio')

    form    = BuscarClienteForm(request.GET)
    clientes = Cliente.objects.select_related('usuario').filter(eliminado=False)
    eliminados = Cliente.objects.select_related('usuario').filter(eliminado=True)

    q    = request.GET.get('q', '').strip()
    tipo = request.GET.get('tipo', '').strip()

    if q:
        # Filtro en Python para tolerar tildes (SQLite no lo hace). Incluye a
        # los clientes sin cuenta web, que no tienen `usuario` (H-22).
        q_norm = normalizar_texto(q)
        clientes = [c for c in clientes if q_norm in _texto_buscable(c)]
    else:
        clientes = list(clientes)

    if tipo:
        clientes = [c for c in clientes if c.tipo_cliente == tipo]

    orden = request.GET.get('orden', '')
    direccion = 'desc' if request.GET.get('dir') == 'desc' else 'asc'
    if orden in ORDEN_CLIENTES:
        clientes.sort(key=ORDEN_CLIENTES[orden], reverse=direccion == 'desc')
    else:
        orden = ''

    paginator = Paginator(clientes, 10)
    page_obj  = paginator.get_page(request.GET.get('page'))

    return render(request, 'clientes/listar_clientes.html', {
        'clientes': page_obj,
        'form': form,
        'q': q,
        'tipo': tipo,
        'columnas': _columnas_ordenables(q, tipo, orden, direccion),
        'eliminados': eliminados,
        # Para que la paginación conserve filtros y orden
        'filtros_qs': urlencode({'q': q, 'tipo': tipo, 'orden': orden, 'dir': direccion if orden else ''}),
    })


# ─────────────────────────────────────────────────────────────
# VER FICHA DE CLIENTE
# ─────────────────────────────────────────────────────────────
@login_required
def ver_cliente(request, pk):
    if not puede(request.user, 'ver_clientes'):
        messages.error(request, 'No tenés permiso para ver esta ficha.')
        return redirect('inicio')

    cliente  = get_object_or_404(Cliente, pk=pk)
    telefonos = cliente.telefonos.all()
    direcciones = cliente.direcciones.select_related('barrio__zona').all()
    pedidos = cliente.pedidos.select_related('metodo_pago').prefetch_related('detalles__producto', 'pagos').all()

    form_tel = TelefonoContactoForm()
    movimientos_bidon = cliente.movimientos_bidon.select_related('registrado_por', 'pedido')[:15]

    # RNF-02: la nota de seguridad se calcula por DIRECCIÓN, no por usuario.
    # Esta ficha solo la abre personal con poder de escritura; el repartidor
    # recibe la nota de sus paradas en las vistas de logística (mi_ruta_hoy,
    # ver_ruta e imprimir_ruta), no en la ficha completa del cliente.
    es_personal = puede(request.user, 'ver_clientes')

    # El formulario de alta/edición de dirección incluye el campo de nota de
    # seguridad, que es información sensible (RNF-02). Solo se expone al
    # personal interno; al cliente se le oculta el campo.
    form_dir = DireccionEntregaForm(is_staff_or_admin=True)

    return render(request, 'clientes/ver_cliente.html', {
        'cliente':             cliente,
        'telefonos':           telefonos,
        'direcciones':         direcciones,
        'telefonos_eliminados':   TelefonoContacto.todos.filter(cliente=cliente, eliminado=True),
        'direcciones_eliminadas': DireccionEntrega.todos.filter(cliente=cliente, eliminado=True),
        'pedidos':             pedidos,
        'form_tel':            form_tel,
        'form_dir':            form_dir,
        'form_bidon':          MovimientoBidonForm(),
        'form_promocion':      VenderPromocionForm(),
        'compras_promocion':   cliente.compras_promocion.select_related('promocion').order_by('-fecha_compra', '-id_compra')[:10],
        'saldos_promocion':    compras_vigentes(cliente),
        **_contexto_suscripcion(cliente),
        'movimientos_bidon':   movimientos_bidon,
        'es_personal':         es_personal,
        # Lista de IDs de dirección cuya nota de seguridad puede ver este usuario.
        'direcciones_con_nota_visible': [
            direccion.pk for direccion in direcciones
            if puede_ver_nota_seguridad(request.user, direccion)
        ],
    })


# ─────────────────────────────────────────────────────────────
# CREAR CLIENTE MANUAL
# ─────────────────────────────────────────────────────────────

@login_required
def crear_cliente(request):
    """
    Selector: muestra las dos opciones de alta de cliente.
    Admin/Vendedor pueden crear clientes con o sin cuenta web.
    """
    if not puede(request.user, 'registrar_clientes'):
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
    if not puede(request.user, 'registrar_clientes'):
        messages.error(request, 'No tenés permiso para crear clientes.')
        return redirect('apps.clientes:listar_clientes')

    telefonos, errores_telefonos = None, []
    if request.method == 'POST':
        form = ClienteSinCuentaForm(request.POST)
        telefonos, errores_telefonos = servicios_clientes.leer_telefonos(request.POST)
        if form.is_valid() and not errores_telefonos:
            cliente = form.save(commit=False)
            # Sin usuario vinculado
            cliente.usuario = None
            cliente.save()
            servicios_clientes.guardar_telefonos(cliente, telefonos)
            messages.success(
                request,
                f'Cliente "{cliente.nombre_completo()}" creado correctamente (sin cuenta web).'
            )
            return redirect('apps.clientes:ver_cliente', pk=cliente.pk)
    else:
        form = ClienteSinCuentaForm()

    return render(request, 'clientes/crear_cliente_sin_cuenta.html', {
        'form': form, 'telefonos': telefonos, 'errores_telefonos': errores_telefonos})


@login_required
def crear_cliente_con_cuenta(request):
    """
    Alta de cliente con cuenta de acceso web.
    Usa el formulario que integra datos de usuario y cliente.
    """
    if not puede(request.user, 'registrar_clientes'):
        messages.error(request, 'No tenés permiso para crear clientes.')
        return redirect('apps.clientes:listar_clientes')

    telefonos, errores_telefonos = None, []
    if request.method == 'POST':
        form_usuario = AltaClienteConCuentaForm(request.POST, request.FILES)
        telefonos, errores_telefonos = servicios_clientes.leer_telefonos(request.POST)
        if form_usuario.is_valid() and not errores_telefonos:
            usuario = form_usuario.save()
            # La señal post_save crea el Cliente automáticamente y el form lo actualiza
            try:
                cliente = usuario.perfil_cliente
                servicios_clientes.guardar_telefonos(cliente, telefonos)
                messages.success(
                    request,
                    f'Cliente "{cliente.nombre_completo()}" creado con cuenta web.'
                )
                return redirect('apps.clientes:ver_cliente', pk=cliente.pk)
            except Cliente.DoesNotExist:
                messages.error(request, 'Error al crear el perfil de cliente.')
    else:
        form_usuario = AltaClienteConCuentaForm()

    return render(request, 'clientes/crear_cliente_con_cuenta.html', {
        'form_usuario': form_usuario, 'telefonos': telefonos, 'errores_telefonos': errores_telefonos})


# ─────────────────────────────────────────────────────────────
# ELIMINAR / RESTAURAR CLIENTE (baja lógica, como los productos)
# ─────────────────────────────────────────────────────────────
@login_required
def eliminar_cliente(request, pk):
    """«Eliminar» no borra: oculta al cliente, lo saca de los listados para
    elegir clientes y bloquea su acceso web. Pedidos, cuenta e historial quedan."""
    if not puede(request.user, 'registrar_clientes'):
        messages.error(request, 'No tenés permiso para eliminar clientes.')
        return redirect('apps.clientes:listar_clientes')
    if request.method != 'POST':
        return redirect('apps.clientes:ver_cliente', pk=pk)
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.dar_de_baja()
    messages.success(request, f'«{cliente.nombre_completo()}» se eliminó. '
                              'Lo podés restaurar desde «Clientes eliminados».')
    return redirect('apps.clientes:listar_clientes')


@login_required
def restaurar_cliente(request, pk):
    if not puede(request.user, 'registrar_clientes'):
        messages.error(request, 'No tenés permiso para restaurar clientes.')
        return redirect('apps.clientes:listar_clientes')
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, pk=pk)
        cliente.restaurar()
        messages.success(request, f'«{cliente.nombre_completo()}» volvió al directorio.')
    return redirect('apps.clientes:listar_clientes')


# ─────────────────────────────────────────────────────────────
# EDITAR CLIENTE (perfil de negocio)
# ─────────────────────────────────────────────────────────────
@login_required
def editar_cliente(request, pk):
    if not puede(request.user, 'registrar_clientes'):
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
    if not puede(request.user, 'cambiar_tipo_cliente'):
        messages.error(request, 'No tenés permiso para cambiar el tipo de cliente.')
        return redirect('apps.clientes:listar_clientes')

    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        nuevo_tipo = request.POST.get('tipo_cliente')
        if nuevo_tipo in ('Normal', 'Premium'):
            tenia_fiado = cliente.permite_fiado
            cliente.tipo_cliente = nuevo_tipo
            cliente.save()
            aviso = ''
            if cliente.permite_fiado and not tenia_fiado:
                aviso = ' Fiado habilitado.'
            elif tenia_fiado and not cliente.permite_fiado:
                aviso = ' Se quitó el fiado.'
            messages.success(request, f'Cliente actualizado a {nuevo_tipo}.{aviso}')
        else:
            messages.error(request, 'Tipo de cliente inválido.')

    return redirect('apps.clientes:ver_cliente', pk=pk)


# ─────────────────────────────────────────────────────────────
# ENVASES (RF-08)
# ─────────────────────────────────────────────────────────────
@login_required
def registrar_movimiento_bidon(request, pk):
    """Devolución, préstamo, venta o ajuste de envases cargado por el personal."""
    if not puede(request.user, 'registrar_envases'):
        messages.error(request, 'No tenés permiso para registrar envases.')
        return redirect('inicio')
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method != 'POST':
        return redirect('apps.clientes:ver_cliente', pk=pk)

    form = MovimientoBidonForm(request.POST)
    if form.is_valid():
        try:
            movimiento = servicios_clientes.registrar_movimiento_bidon(
                cliente, form.cleaned_data['tipo'], form.cleaned_data['cantidad'],
                usuario=request.user, nota=form.cleaned_data['nota'],
            )
            messages.success(
                request,
                f'{movimiento.get_tipo_display()} registrado. '
                f'Saldo de envases: {movimiento.cliente.bidones_prestados}.'
            )
        except ValidationError as error:
            messages.error(request, ' '.join(error.messages))
    else:
        messages.error(request, f'No se registró el movimiento: {errores_en_texto(form)}')
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
        form = TelefonoContactoForm(request.POST, cliente=cliente)
        if form.is_valid():
            tel = form.save(commit=False)
            tel.cliente = cliente
            tel.save()
            messages.success(request, f'Teléfono {tel.numero} agregado.')
        else:
            messages.error(request, f'No se agregó el teléfono: {errores_en_texto(form)}')

    if cliente.usuario == request.user and not puede(request.user, 'registrar_clientes'):
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
            tel.dar_de_baja()
            messages.success(request, 'Teléfono eliminado.')

    if cliente.usuario == request.user and not puede(request.user, 'registrar_clientes'):
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

    # RF-03 (decisión A-D4): el cliente puede tener varias direcciones; en el
    # checkout elige a cuál se le entrega.
    next_url = request.GET.get('next') or request.POST.get('next') or ''
    if next_url and not url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
        next_url = ''

    is_staff = puede(request.user, 'registrar_clientes')

    if request.method == 'POST':
        form = DireccionEntregaForm(request.POST, is_staff_or_admin=is_staff)
        if form.is_valid():
            dir_ = form.save(commit=False)
            dir_.cliente = cliente
            # Asignar Zona 1 (Pendiente de Asignación) al barrio si no posee una zona definida
            if dir_.barrio and not dir_.barrio.zona:
                from apps.logistica.models import Zona
                zona_default, _ = Zona.objects.get_or_create(
                    nombre='Zona 1 (Pendiente de Asignación)',
                    defaults={'ciudad': 'Resistencia', 'descripcion': 'Zona por defecto asignada a nuevos domicilios hasta su revisión'}
                )
                dir_.barrio.zona = zona_default
                dir_.barrio.save()
            # La primera dirección siempre es la principal; las siguientes, si se marcó.
            if not cliente.direcciones.exists():
                dir_.es_principal = True
            dir_.save()
            messages.success(request, f'Dirección "{dir_}" agregada con éxito.')

            if next_url:
                return redirect(next_url)
            if cliente.usuario == request.user and not puede(request.user, 'registrar_clientes'):
                return redirect('apps.clientes:mi_perfil')
            return redirect('apps.clientes:ver_cliente', pk=pk)
        else:
            messages.error(request, 'Error al agregar la dirección. Revisá los campos.')
    else:
        form = DireccionEntregaForm(is_staff_or_admin=is_staff)
        # Sólo la primera dirección se sugiere como principal.
        form.initial['es_principal'] = not cliente.direcciones.exists()

    return render(request, 'clientes/agregar_direccion.html', {
        'form': form,
        'cliente': cliente,
        'next': next_url,
    })


@login_required
def editar_direccion(request, pk):
    direccion  = get_object_or_404(DireccionEntrega, pk=pk)
    cliente    = direccion.cliente
    is_staff   = puede(request.user, 'registrar_clientes')

    if not es_dueno_o_staff(request.user, cliente):
        messages.error(request, 'Sin permiso.')
        return redirect('inicio')

    if request.method == 'POST':
        form = DireccionEntregaForm(request.POST, instance=direccion, is_staff_or_admin=is_staff)
        if form.is_valid():
            dir_ = form.save(commit=False)
            if dir_.barrio and not dir_.barrio.zona:
                from apps.logistica.models import Zona
                zona_default, _ = Zona.objects.get_or_create(
                    nombre='Zona 1 (Pendiente de Asignación)',
                    defaults={'ciudad': 'Resistencia', 'descripcion': 'Zona por defecto asignada a nuevos domicilios hasta su revisión'}
                )
                dir_.barrio.zona = zona_default
                dir_.barrio.save()
            dir_.save()
            messages.success(request, 'Dirección actualizada.')
            if cliente.usuario == request.user and not puede(request.user, 'registrar_clientes'):
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
        direccion.dar_de_baja()
        messages.success(request, 'Dirección eliminada.')

    if cliente.usuario == request.user and not puede(request.user, 'registrar_clientes'):
        return redirect('apps.clientes:mi_perfil')
    return redirect('apps.clientes:ver_cliente', pk=cliente.pk)


@login_required
def restaurar_telefono(request, pk):
    tel = get_object_or_404(TelefonoContacto.todos, pk=pk)
    if not puede(request.user, 'registrar_clientes'):
        messages.error(request, 'Sin permiso.')
        return redirect('inicio')
    if request.method == 'POST':
        tel.eliminado = False
        tel.save(update_fields=['eliminado'])
        messages.success(request, 'Teléfono restaurado.')
    return redirect('apps.clientes:ver_cliente', pk=tel.cliente_id)


@login_required
def restaurar_direccion(request, pk):
    direccion = get_object_or_404(DireccionEntrega.todos, pk=pk)
    if not puede(request.user, 'registrar_clientes'):
        messages.error(request, 'Sin permiso.')
        return redirect('inicio')
    if request.method == 'POST':
        direccion.eliminado = False
        direccion.save(update_fields=['eliminado'])
        messages.success(request, 'Dirección restaurada.')
    return redirect('apps.clientes:ver_cliente', pk=direccion.cliente_id)


# ─────────────────────────────────────────────────────────────
# MI PERFIL (vista del propio cliente)
# ─────────────────────────────────────────────────────────────
@login_required
def mi_perfil_cliente(request):
    """El cliente ve sus propios datos sin información sensible."""
    if (fuera := solo_clientes(request)) is not None:
        return fuera
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
    direcciones = cliente.direcciones.select_related('barrio__zona').all()
    pedidos     = Pedido.objects.filter(cliente=cliente).select_related('metodo_pago').prefetch_related('detalles__producto')

    return render(request, 'clientes/mi_perfil_cliente.html', {
        'cliente':     cliente,
        'telefonos':   telefonos,
        'direcciones': direcciones,
        'pedidos':     pedidos,
        'saldos_promocion': compras_vigentes(cliente),
        **_contexto_suscripcion(cliente),
    })


@login_required
def editar_mi_perfil(request):
    """Permite al cliente logueado modificar sus datos personales y foto de perfil."""
    if (fuera := solo_clientes(request)) is not None:
        return fuera
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

    user = request.user
    principal = cliente.telefonos.order_by('-es_principal', 'pk').first()
    form_perfil = EditarMiPerfilForm(initial={'celular': principal.numero if principal else user.celular1})
    form_password = PasswordChangeForm(user)
    for campo in form_password.fields.values():
        campo.widget.attrs['class'] = 'form-control'

    if request.method == 'POST' and 'form_password' in request.POST:
        form_password = PasswordChangeForm(user, request.POST)
        for campo in form_password.fields.values():
            campo.widget.attrs['class'] = 'form-control'
        if form_password.is_valid():
            form_password.save()
            update_session_auth_hash(request, form_password.user)
            messages.success(request, 'Tu contraseña se cambió correctamente.')
            return redirect('apps.clientes:mi_perfil')
        messages.error(request, 'No se pudo cambiar la contraseña: revisá los campos marcados.')

    elif request.method == 'POST':
        form_perfil = EditarMiPerfilForm(request.POST, request.FILES)
        if form_perfil.is_valid():
            datos = form_perfil.cleaned_data
            if datos.get('eliminar_foto'):
                user.imagen_perfil = Usuario._meta.get_field('imagen_perfil').get_default()
            elif datos.get('imagen_perfil'):
                user.imagen_perfil = datos['imagen_perfil']
            celular = datos.get('celular')
            if celular:
                user.celular1 = celular
                if principal:
                    principal.numero = celular
                    principal.save(update_fields=['numero'])
                else:
                    TelefonoContacto.objects.create(cliente=cliente, numero=celular,
                                                    desc_relacion='Titular', es_principal=True)
            user.save()
            messages.success(request, 'Tus datos de perfil se actualizaron.')
            return redirect('apps.clientes:mi_perfil')
        messages.error(request, f'No se guardaron los cambios: {errores_en_texto(form_perfil)}')

    return render(request, 'clientes/editar_mi_perfil.html', {
        'form_perfil': form_perfil,
        'form_password': form_password,
        'cliente': cliente,
    })

