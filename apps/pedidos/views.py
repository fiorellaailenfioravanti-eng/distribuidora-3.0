import logging

import mercadopago
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .models import Pedido, DetallePedido, PagoPedido, MetodoPago
from .forms import CheckoutForm
from .services import (
    aplicar_pago_mercadopago,
    consultar_pago_mercadopago,
    firma_webhook_valida,
    pago_en_curso,
)
from apps.carrito.models import Carrito
from apps.clientes.models import Cliente
from apps.permisos.roles import (
    es_admin_o_vendedor,
    puede_ver_nota_seguridad,
)


# Token de MercadoPago. En desarrollo puede ir vacío: el checkout con QR
# informa al usuario y el resto de los métodos de pago siguen operativos.
MERCADOPAGO_ACCESS_TOKEN = getattr(settings, 'MERCADOPAGO_ACCESS_TOKEN', '') or ''

MERCADOPAGO_WEBHOOK_SECRET = getattr(settings, 'MERCADOPAGO_WEBHOOK_SECRET', '') or ''

logger = logging.getLogger(__name__)


@login_required
def checkout(request):
    """Pantalla de selección de dirección y método de pago antes de confirmar."""
    if es_admin_o_vendedor(request.user):
        messages.info(request, "Los usuarios administradores y vendedores gestionan los pedidos desde la consola.")
        return redirect('apps.pedidos:listar_pedidos')

    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.items.all()

    if not items.exists():
        messages.warning(request, "Tu carrito está vacío. Añade productos antes de realizar un pedido.")
        return redirect('apps.productos:listar_productos')

    # Obtener o crear perfil de cliente del usuario
    cliente, _ = Cliente.objects.get_or_create(
        usuario=request.user,
        defaults={
            'nombre': request.user.first_name or request.user.username,
            'apellido': request.user.last_name or '',
            'email_contacto': request.user.email
        }
    )

    direcciones = cliente.direcciones.all()
    if not direcciones.exists():
        messages.warning(request, "Debes agregar al menos una dirección de entrega antes de finalizar tu pedido.")
        return redirect(reverse('apps.clientes:agregar_direccion', kwargs={'pk': cliente.pk}) + '?next=' + reverse('apps.pedidos:checkout'))

    # El catálogo de métodos de pago se mantiene por migración de datos
    # (0003_sembrar_metodos_pago). Los métodos ofrecidos en la web los filtra
    # `CheckoutForm` sin modificar la base.
    form = CheckoutForm(request.POST or None, cliente=cliente)

    contexto = {
        'carrito': carrito,
        'items': items,
        'total_precio': carrito.total_precio(),
        'cliente': cliente,
        'direcciones': direcciones,
        'form': form,
        'cvu_cuenta': '0000003100037733165809',
    }
    return render(request, 'pedidos/checkout.html', contexto)


@login_required
@transaction.atomic
def confirmar_pedido(request):
    """Procesa y confirma el pedido descontando stock e iniciando el flujo de pago."""
    if request.method != 'POST':
        return redirect('apps.pedidos:checkout')

    carrito = get_object_or_404(Carrito, usuario=request.user)
    items = carrito.items.select_related('producto').all()

    if not items.exists():
        messages.error(request, "No hay productos en el carrito.")
        return redirect('apps.productos:listar_productos')

    cliente = get_object_or_404(Cliente, usuario=request.user)
    form = CheckoutForm(request.POST, cliente=cliente)

    if not form.is_valid():
        messages.error(request, "Por favor completa todos los campos requeridos correctamente.")
        return redirect('apps.pedidos:checkout')

    direccion = form.cleaned_data['direccion_entrega']
    metodo_pago = form.cleaned_data['metodo_pago']
    notas = form.cleaned_data['notas_cliente']

    # 1. Validar Stock atómicamente de todos los ítems
    for item in items:
        if item.producto.stock < item.cantidad:
            messages.error(
                request,
                f"Lo sentimos, no hay stock suficiente de '{item.producto.nombre}'. "
                f"Disponibles: {item.producto.stock}, en tu carrito: {item.cantidad}."
            )
            return redirect('apps.carrito:ver_carrito')

    # 2. Crear Pedido (estado inicial dependiendo del método)
    from apps.logistica.services import fecha_estimada_para_direccion
    total_pedido = carrito.total_precio()
    pedido = Pedido.objects.create(
        cliente=cliente,
        direccion_entrega=direccion,
        metodo_pago=metodo_pago,
        total=total_pedido,
        notas_cliente=notas,
        estado='Pendiente',
        origen='WEB',
        fecha_estimada_entrega=fecha_estimada_para_direccion(direccion),
    )

    # 3. Crear DetallePedido. El stock NO se descuenta aquí: el descuento
    #    ocurre en logística al cargar el camión (confirmar la hoja de ruta),
    #    de modo que el regreso devuelva los sobrantes sin contar dos veces.
    for item in items:
        DetallePedido.objects.create(
            pedido=pedido,
            producto=item.producto,
            precio_unitario=item.producto.precio,
            cantidad=item.cantidad,
            subtotal=item.subtotal()
        )

    # 4. Vaciar Carrito
    carrito.items.all().delete()

    # 5. Lógica según el método de pago elegido
    if metodo_pago.codigo in ['MERCADOPAGO', 'PAGO_VIRTUAL']:
        preference_id = ''
        init_point = ''
        try:
            sdk = mercadopago.SDK(MERCADOPAGO_ACCESS_TOKEN)
            mp_items = []
            for detalle in pedido.detalles.all():
                mp_items.append({
                    "title": detalle.producto.nombre,
                    "quantity": int(detalle.cantidad),
                    "unit_price": float(detalle.precio_unitario),
                    "currency_id": "ARS"
                })

            base_url = request.build_absolute_uri('/')[:-1]
            success_url = base_url + reverse('apps.pedidos:pago_exitoso')
            failure_url = base_url + reverse('apps.pedidos:pago_fallido')
            pending_url = base_url + reverse('apps.pedidos:pago_pendiente')

            preference_data = {
                "items": mp_items,
                "payer": {
                    "name": cliente.nombre or request.user.first_name or "Cliente",
                    "surname": cliente.apellido or request.user.last_name or "Distribuidora",
                    "email": cliente.email_display() or request.user.email or "cliente@ejemplo.com"
                },
                "back_urls": {
                    "success": success_url,
                    "failure": failure_url,
                    "pending": pending_url
                },
                "auto_return": "approved",
                "external_reference": str(pedido.id_pedido)
            }

            preference_response = sdk.preference().create(preference_data)
            response_data = preference_response.get("response", {})
            preference_id = response_data.get("id", "")
            init_point = response_data.get("init_point") or response_data.get("sandbox_init_point")
        except Exception:
            logger.exception('No se pudo crear la preferencia de MercadoPago del pedido %s.', pedido.pk)

        PagoPedido.objects.create(
            pedido=pedido,
            monto=pedido.total,
            metodo_pago=metodo_pago,
            mercadopago_preference_id=preference_id,
            estado_pago='Pendiente'
        )

        if init_point:
            return redirect(init_point)
        messages.warning(
            request,
            f"Tu pedido #{pedido.id_pedido} quedó registrado, pero no pudimos iniciar el pago online. "
            "Podés abonarlo al recibirlo o reintentar más tarde."
        )
        return redirect('apps.pedidos:detalle_pedido', pk=pedido.id_pedido)

    else:
        # Pago en efectivo / contra entrega
        PagoPedido.objects.create(
            pedido=pedido,
            monto=pedido.total,
            metodo_pago=metodo_pago,
            estado_pago='Pendiente'
        )
        messages.success(request, f"¡Gracias por tu compra! Tu pedido #{pedido.id_pedido} ha sido registrado correctamente.")
        return redirect('apps.pedidos:detalle_pedido', pk=pedido.id_pedido)


@login_required
def pago_exitoso(request):
    """Callback de MercadoPago al volver del checkout (H-18).

    Los parámetros de la URL los controla el navegador, así que no se usan para
    aprobar nada: sólo se verifica que el pedido sea del usuario y, si hay
    `payment_id`, se consulta el estado real a la API de MercadoPago.
    """
    external_reference = request.GET.get('external_reference')
    payment_id = request.GET.get('payment_id')

    pedido = None
    if external_reference and external_reference.isdigit():
        pedido = Pedido.objects.filter(
            id_pedido=external_reference, cliente__usuario=request.user
        ).first()
    if pedido is None:
        messages.info(request, "Recibimos tu regreso desde MercadoPago. Revisá el estado en Mis pedidos.")
        return redirect('apps.pedidos:mis_pedidos')

    if payment_id and MERCADOPAGO_ACCESS_TOKEN:
        datos = consultar_pago_mercadopago(mercadopago.SDK(MERCADOPAGO_ACCESS_TOKEN), payment_id)
        if str(datos.get('external_reference')) == str(pedido.id_pedido):
            aplicar_pago_mercadopago(
                pedido, payment_id, datos.get('status'), datos.get('transaction_amount')
            )
            pedido.refresh_from_db()

    if pedido.esta_pagado():
        messages.success(request, f"¡Pago verificado! Tu pedido #{pedido.id_pedido} está confirmado.")
    else:
        messages.info(
            request,
            f"Estamos verificando el pago del pedido #{pedido.id_pedido}. "
            "Se confirmará en cuanto MercadoPago lo acredite."
        )
    return redirect('apps.pedidos:detalle_pedido', pk=pedido.id_pedido)


@login_required
def pago_pendiente(request):
    """Callback de MercadoPago cuando el pago queda pendiente de acreditación."""
    external_reference = request.GET.get('external_reference')
    if external_reference:
        try:
            pedido = Pedido.objects.get(id_pedido=external_reference)
            messages.warning(request, f"El pago de tu pedido #{pedido.id_pedido} está pendiente de acreditación. Te avisaremos una vez que MercadoPago lo procese.")
            return redirect('apps.pedidos:detalle_pedido', pk=pedido.id_pedido)
        except Pedido.DoesNotExist:
            pass
    messages.warning(request, "El pago está pendiente de procesamiento.")
    return redirect('apps.pedidos:mis_pedidos')


@login_required
def pago_fallido(request):
    """Callback de MercadoPago cuando el pago es rechazado o cancelado."""
    external_reference = request.GET.get('external_reference')
    if external_reference:
        try:
            pedido = Pedido.objects.get(id_pedido=external_reference)
            messages.error(request, f"El pago para el pedido #{pedido.id_pedido} no pudo procesarse. Puedes intentar nuevamente o cambiar el medio de pago.")
            return redirect('apps.pedidos:detalle_pedido', pk=pedido.id_pedido)
        except Pedido.DoesNotExist:
            pass
    messages.error(request, "No se pudo completar el pago en MercadoPago.")
    return redirect('apps.pedidos:mis_pedidos')


@csrf_exempt
def webhook_mercadopago(request):
    """Notificaciones de MercadoPago (H-21).

    1. Valida la firma `x-signature` con `MERCADOPAGO_WEBHOOK_SECRET`.
    2. Consulta el pago a la API (no confía en el cuerpo de la notificación).
    3. Aplica el estado controlando que el monto cubra lo esperado.
    """
    if request.method != 'POST':
        return HttpResponse(status=405)

    topic = request.GET.get('type') or request.GET.get('topic')
    resource_id = request.GET.get('data.id') or request.GET.get('id')

    if not firma_webhook_valida(
        MERCADOPAGO_WEBHOOK_SECRET,
        request.headers.get('x-signature', ''),
        request.headers.get('x-request-id', ''),
        resource_id,
    ):
        logger.warning('Webhook de MercadoPago con firma inválida (recurso %s).', resource_id)
        return HttpResponse(status=403)

    if topic != 'payment' or not resource_id or not MERCADOPAGO_ACCESS_TOKEN:
        return HttpResponse(status=200)

    datos = consultar_pago_mercadopago(mercadopago.SDK(MERCADOPAGO_ACCESS_TOKEN), resource_id)
    referencia = str(datos.get('external_reference') or '')
    if not referencia.isdigit():
        return HttpResponse(status=200)

    pedido = Pedido.objects.filter(id_pedido=referencia).first()
    if pedido is not None:
        aplicar_pago_mercadopago(
            pedido, resource_id, datos.get('status'), datos.get('transaction_amount')
        )
    return HttpResponse(status=200)


@login_required
def detalle_pedido(request, pk):
    """Muestra el detalle completo de un pedido."""
    pedido = get_object_or_404(Pedido, pk=pk)

    # Permitir ver si es el cliente dueño del pedido o si es Vendedor/Admin
    if not (request.user.is_superuser or es_admin_o_vendedor(request.user)):
        if not (pedido.cliente and pedido.cliente.usuario == request.user):
            messages.error(request, "No tienes permiso para ver este pedido.")
            return redirect('apps.pedidos:mis_pedidos')

    contexto = {
        'pedido': pedido,
        'detalles': pedido.detalles.select_related('producto').all(),
        'pagos': pedido.pagos.all(),
        # RNF-02: la nota de seguridad se evalúa sobre la dirección concreta
        # del pedido, no sobre el rol del usuario.
        'puede_ver_nota_seguridad': puede_ver_nota_seguridad(
            request.user, pedido.direccion_entrega
        ),
    }
    return render(request, 'pedidos/detalle_pedido.html', contexto)


@login_required
def mis_pedidos(request):
    """Listado de compras/pedidos realizas por el cliente logueado."""
    if es_admin_o_vendedor(request.user):
        messages.info(request, "Los usuarios administradores y vendedores gestionan la totalidad de pedidos de la distribuidora.")
        return redirect('apps.pedidos:listar_pedidos')

    try:
        cliente = request.user.perfil_cliente
        pedidos = Pedido.objects.filter(cliente=cliente).prefetch_related('detalles__producto')
    except AttributeError:
        pedidos = Pedido.objects.none()

    contexto = {
        'pedidos': pedidos
    }
    return render(request, 'pedidos/mis_pedidos.html', contexto)


@login_required
@user_passes_test(es_admin_o_vendedor)
def listar_pedidos(request):
    """Panel de administración/vendedor para gestionar todos los pedidos recibidos."""
    pedidos = Pedido.objects.all().select_related('cliente', 'direccion_entrega', 'metodo_pago').prefetch_related('detalles__producto', 'pagos')

    # Filtro opcional por estado de pedido
    estado_filtro = request.GET.get('estado')
    if estado_filtro:
        pedidos = pedidos.filter(estado=estado_filtro)

    # Filtro opcional por estado de pago
    pago_filtro = request.GET.get('pago_estado')
    if pago_filtro:
        pedidos = pedidos.filter(pagos__estado_pago=pago_filtro).distinct()

    contexto = {
        'pedidos': pedidos,
        'estado_filtro': estado_filtro,
        'pago_filtro': pago_filtro,
        'estados_choices': Pedido._meta.get_field('estado').choices
    }
    return render(request, 'pedidos/listar_pedidos.html', contexto)


@login_required
@user_passes_test(es_admin_o_vendedor)
def cambiar_estado_pedido(request, pk):
    """Permite al staff actualizar el estado de un pedido."""
    if request.method == 'POST':
        pedido = get_object_or_404(Pedido, pk=pk)
        nuevo_estado = request.POST.get('estado')
        if nuevo_estado in dict(Pedido._meta.get_field('estado').choices):
            pedido.estado = nuevo_estado
            pedido.save()
            messages.success(request, f"Estado del Pedido #{pedido.id_pedido} actualizado a '{nuevo_estado}'.")
        else:
            messages.error(request, "Estado no válido.")

    return redirect(request.META.get('HTTP_REFERER') or 'apps.pedidos:listar_pedidos')


@login_required
@user_passes_test(es_admin_o_vendedor)
def cambiar_estado_pago(request, pk):
    """Permite al staff actualizar el estado del pago de un pedido (ej. de Pendiente a Aprobado)."""
    if request.method == 'POST':
        pedido = get_object_or_404(Pedido, pk=pk)
        nuevo_pago_estado = request.POST.get('estado_pago')
        if nuevo_pago_estado in ['Pendiente', 'Aprobado', 'Rechazado']:
            pago = pago_en_curso(pedido)
            pago.estado_pago = nuevo_pago_estado
            pago.save()

            if nuevo_pago_estado == 'Aprobado' and pedido.estado == 'Pendiente':
                pedido.estado = 'Confirmado'
                pedido.save()

            messages.success(request, f"Estado del pago del Pedido #{pedido.id_pedido} actualizado a '{nuevo_pago_estado}'.")
        else:
            messages.error(request, "Estado de pago no válido.")

    return redirect(request.META.get('HTTP_REFERER') or 'apps.pedidos:listar_pedidos')


@login_required
def pago_qr(request, pk):
    """Pantalla interactiva de pago con Código QR de MercadoPago y Deep Link a la App Móvil."""
    pedido = get_object_or_404(Pedido, pk=pk, cliente__usuario=request.user)
    pago = pedido.pagos.last()
    pref_id = pago.mercadopago_preference_id if pago else ''

    if pref_id:
        init_point = f"https://www.mercadopago.com.ar/checkout/v1/redirect?pref_id={pref_id}"
        app_deep_link = f"mercadopago://checkout/v1/redirect?pref_id={pref_id}"
        qr_data = init_point
    else:
        init_point = "https://www.mercadopago.com.ar/"
        app_deep_link = "mercadopago://"
        qr_data = "https://www.mercadopago.com.ar/"

    import urllib.parse
    qr_data_encoded = urllib.parse.quote(qr_data)
    qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=280x280&data={qr_data_encoded}"

    contexto = {
        'pedido': pedido,
        'pago': pago,
        'app_deep_link': app_deep_link,
        'web_init_point': init_point,
        'qr_url': qr_url,
    }
    return render(request, 'pedidos/pago_qr.html', contexto)


@login_required
def confirmar_pago_qr(request, pk):
    """El cliente avisa que ya pagó por QR (H-19, decisión A-D2).

    No aprueba el pago: lo deja `Pendiente` para que lo confirme el webhook de
    MercadoPago o un Vendedor desde la gestión de pedidos.
    """
    pedido = get_object_or_404(Pedido, pk=pk, cliente__usuario=request.user)
    if request.method != 'POST':
        return redirect('apps.pedidos:pago_qr', pk=pedido.id_pedido)

    pago = pago_en_curso(pedido)
    if pago.estado_pago != 'Aprobado':
        pago.mercadopago_status = pago.mercadopago_status or 'informado_por_cliente'
        pago.save(update_fields=['mercadopago_status'])

    messages.info(
        request,
        f"Gracias. Vamos a verificar el pago del pedido #{pedido.id_pedido} y te avisaremos al confirmarlo."
    )
    return redirect('apps.pedidos:detalle_pedido', pk=pedido.id_pedido)