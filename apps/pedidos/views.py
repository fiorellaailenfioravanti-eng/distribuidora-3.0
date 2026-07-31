import json
import mercadopago
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .models import Pedido, DetallePedido, PagoPedido, MetodoPago
from .forms import CheckoutForm
from apps.carrito.models import Carrito
from apps.clientes.models import Cliente


# Token de prueba de MercadoPago por defecto (Sandbox / Test Token)
MERCADOPAGO_ACCESS_TOKEN = getattr(
    settings,
    'MERCADOPAGO_ACCESS_TOKEN',
    'APP_USR-7837096695275811-073008-0dbcaef7331562b0833116df163a8a30-244301549'
)


def es_vendedor_o_admin(user):
    return user.is_superuser or user.groups.filter(name='Vendedor').exists()


@login_required
def checkout(request):
    """Pantalla de selección de dirección y método de pago antes de confirmar."""
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

    metodos_pago = MetodoPago.objects.filter(activo=True)
    if not metodos_pago.exists():
        # Crear métodos por defecto si no existen
        MetodoPago.objects.get_or_create(
            codigo='MERCADOPAGO',
            defaults={'nombre': 'MercadoPago / Tarjeta / Transferencia (Automático)', 'descripcion': 'Pago seguro online en tiempo real'}
        )
        MetodoPago.objects.get_or_create(
            codigo='EFECTIVO',
            defaults={'nombre': 'Efectivo en Entrega', 'descripcion': 'Abonas en efectivo al recibir el pedido'}
        )

    form = CheckoutForm(request.POST or None, cliente=cliente)

    contexto = {
        'carrito': carrito,
        'items': items,
        'total_precio': carrito.total_precio(),
        'cliente': cliente,
        'direcciones': direcciones,
        'form': form,
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

    # 2. Crear Pedido
    total_pedido = carrito.total_precio()
    pedido = Pedido.objects.create(
        cliente=cliente,
        direccion_entrega=direccion,
        metodo_pago=metodo_pago,
        total=total_pedido,
        notas_cliente=notas,
        estado='Pendiente'
    )

    # 3. Crear DetallePedido y Descontar Stock
    for item in items:
        DetallePedido.objects.create(
            pedido=pedido,
            producto=item.producto,
            precio_unitario=item.producto.precio,
            cantidad=item.cantidad,
            subtotal=item.subtotal()
        )
        # Descontar del stock del producto
        item.producto.stock -= item.cantidad
        item.producto.save()

    # 4. Vaciar Carrito
    carrito.items.all().delete()

    # 5. Lógica según el método de pago
    if metodo_pago.codigo in ['MERCADOPAGO', 'PAGO_VIRTUAL']:
        try:
            sdk = mercadopago.SDK(MERCADOPAGO_ACCESS_TOKEN)

            # Construir ítems para la preferencia de MercadoPago
            mp_items = []
            for detalle in pedido.detalles.all():
                mp_items.append({
                    "title": detalle.producto.nombre,
                    "quantity": detalle.cantidad,
                    "unit_price": float(detalle.precio_unitario),
                    "currency_id": "ARS"
                })

            base_url = request.build_absolute_uri('/')[:-1]
            success_url = base_url + reverse('apps.pedidos:pago_exitoso')
            failure_url = base_url + reverse('apps.pedidos:pago_fallido')
            pending_url = base_url + reverse('apps.pedidos:pago_pendiente')
            webhook_url = base_url + reverse('apps.pedidos:webhook_mercadopago')

            preference_data = {
                "items": mp_items,
                "payer": {
                    "name": cliente.nombre or request.user.first_name,
                    "surname": cliente.apellido or request.user.last_name,
                    "email": cliente.email_display() or request.user.email
                },
                "back_urls": {
                    "success": success_url,
                    "failure": failure_url,
                    "pending": pending_url
                },
                "auto_return": "approved",
                "external_reference": str(pedido.id_pedido),
                "notification_url": webhook_url
            }

            preference_response = sdk.preference().create(preference_data)
            preference = preference_response.get("response", {})
            preference_id = preference.get("id")

            # Crear PagoPedido inicial
            PagoPedido.objects.create(
                pedido=pedido,
                monto=pedido.total,
                metodo_pago=metodo_pago,
                mercadopago_preference_id=preference_id or '',
                estado_pago='Pendiente'
            )

            init_point = preference.get("init_point") or preference.get("sandbox_init_point")
            if init_point:
                messages.info(request, "Redirigiendo a la pasarela segura de MercadoPago para abonar tu pedido...")
                return redirect(init_point)
            else:
                messages.warning(request, f"Pedido #{pedido.id_pedido} registrado, pero no se pudo generar el enlace automático de MercadoPago. Podrás gestionar el pago desde el detalle.")
                return redirect('apps.pedidos:detalle_pedido', pk=pedido.id_pedido)

        except Exception as e:
            # Si falla la llamada a la API de MP, dejamos el pedido creado en Pendiente para no perderlo
            PagoPedido.objects.create(
                pedido=pedido,
                monto=pedido.total,
                metodo_pago=metodo_pago,
                estado_pago='Pendiente'
            )
            messages.warning(request, f"Pedido #{pedido.id_pedido} registrado correctamente. Ocurrió un detalle al conectar con MercadoPago: {e}")
            return redirect('apps.pedidos:detalle_pedido', pk=pedido.id_pedido)

    else:
        # Pago en efectivo o contra entrega
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
    """Callback retornado por MercadoPago cuando el pago es aprobado."""
    payment_id = request.GET.get('payment_id')
    status = request.GET.get('status')
    external_reference = request.GET.get('external_reference')

    if external_reference:
        try:
            pedido = Pedido.objects.get(id_pedido=external_reference)
            pago = pedido.pagos.last()
            if not pago:
                pago = PagoPedido.objects.create(
                    pedido=pedido,
                    monto=pedido.total,
                    metodo_pago=pedido.metodo_pago
                )

            pago.mercadopago_payment_id = payment_id or ''
            pago.mercadopago_status = status or 'approved'
            pago.estado_pago = 'Aprobado'
            pago.save()

            pedido.estado = 'Confirmado'
            pedido.save()

            messages.success(request, f"¡Excelente! El pago de MercadoPago fue verificado con éxito. Pedido #{pedido.id_pedido} confirmado.")
            return redirect('apps.pedidos:detalle_pedido', pk=pedido.id_pedido)
        except Pedido.DoesNotExist:
            pass

    messages.success(request, "Pago completado con éxito.")
    return redirect('apps.pedidos:mis_pedidos')


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
    """Webhook automático que escucha actualizaciones de estado desde MercadoPago."""
    if request.method == 'POST':
        try:
            topic = request.GET.get('type') or request.GET.get('topic')
            resource_id = request.GET.get('data.id') or request.GET.get('id')

            if topic == 'payment' and resource_id:
                sdk = mercadopago.SDK(MERCADOPAGO_ACCESS_TOKEN)
                payment_info = sdk.payment().get(resource_id)
                response = payment_info.get("response", {})

                external_reference = response.get("external_reference")
                status = response.get("status")

                if external_reference and status:
                    pedido = Pedido.objects.filter(id_pedido=external_reference).first()
                    if pedido:
                        pago = pedido.pagos.last()
                        if not pago:
                            pago = PagoPedido.objects.create(
                                pedido=pedido,
                                monto=pedido.total,
                                metodo_pago=pedido.metodo_pago
                            )

                        pago.mercadopago_payment_id = str(resource_id)
                        pago.mercadopago_status = status

                        if status == 'approved':
                            pago.estado_pago = 'Aprobado'
                            pedido.estado = 'Confirmado'
                        elif status in ['rejected', 'cancelled']:
                            pago.estado_pago = 'Rechazado'
                        pago.save()
                        pedido.save()

            return HttpResponse(status=200)
        except Exception as e:
            return HttpResponse(status=500)

    return HttpResponse(status=405)


@login_required
def detalle_pedido(request, pk):
    """Muestra el detalle completo de un pedido."""
    pedido = get_object_or_404(Pedido, pk=pk)

    # Permitir ver si es el cliente dueño del pedido o si es Vendedor/Admin
    if not (request.user.is_superuser or es_vendedor_o_admin(request.user)):
        if not (pedido.cliente and pedido.cliente.usuario == request.user):
            messages.error(request, "No tienes permiso para ver este pedido.")
            return redirect('apps.pedidos:mis_pedidos')

    contexto = {
        'pedido': pedido,
        'detalles': pedido.detalles.select_related('producto').all(),
        'pagos': pedido.pagos.all(),
    }
    return render(request, 'pedidos/detalle_pedido.html', contexto)


@login_required
def mis_pedidos(request):
    """Listado de compras/pedidos realizas por el cliente logueado."""
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
@user_passes_test(es_vendedor_o_admin)
def listar_pedidos(request):
    """Panel de administración/vendedor para gestionar todos los pedidos recibidos."""
    pedidos = Pedido.objects.all().select_related('cliente', 'direccion_entrega', 'metodo_pago').prefetch_related('detalles__producto', 'pagos')

    # Filtro opcional por estado
    estado_filtro = request.GET.get('estado')
    if estado_filtro:
        pedidos = pedidos.filter(estado=estado_filtro)

    contexto = {
        'pedidos': pedidos,
        'estado_filtro': estado_filtro,
        'estados_choices': Pedido._meta.get_field('estado').choices
    }
    return render(request, 'pedidos/listar_pedidos.html', contexto)


@login_required
@user_passes_test(es_vendedor_o_admin)
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
