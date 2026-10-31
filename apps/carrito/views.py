from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Carrito, ItemCarrito
from apps.productos.models import Producto
from django.urls import reverse
from django.contrib import messages
from distribuidora.utils import redirigir_a_origen
from apps.permisos.views import solo_clientes


@login_required
def agregar_al_carrito(request, producto_id):
    if (fuera := solo_clientes(request)) is not None:
        return fuera

    producto = get_object_or_404(Producto, id_producto=producto_id, activo=True)
    if request.method != 'POST':
        # Agregar modifica datos: sólo por POST (H-31).
        return redirect('apps.productos:ver_producto', pk=producto.id_producto)
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    item_carrito, creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)

    try:
        cantidad_a_agregar = int(request.POST.get('cantidad', '1'))
    except ValueError:
        cantidad_a_agregar = 1
            
    if cantidad_a_agregar <= 0:
        cantidad_a_agregar = 1

    # Verificamos si la cantidad actual en el carrito + agregada supera el stock disponible
    cantidad_previa = 0 if creado else item_carrito.cantidad
    nueva_cantidad = cantidad_previa + cantidad_a_agregar
    
    from apps.pedidos.services import stock_disponible
    disponible = stock_disponible(producto)
    if disponible >= nueva_cantidad:
        item_carrito.cantidad = nueva_cantidad
        item_carrito.save()
        messages.success(request, f"{producto.nombre} se añadió al carrito.")
    else:
        messages.error(request, f"Lo sentimos, no hay suficiente stock de {producto.nombre}. (Máximo: {max(disponible, 0)})")
        # Si acababa de ser creado pero no hay stock, lo borramos
        if creado:
            item_carrito.delete()
    
    return redirigir_a_origen(request, 'apps.productos:listar_productos')


@login_required
def ver_carrito(request):
    if (fuera := solo_clientes(request)) is not None:
        return fuera

    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    contexto = {
        'carrito': carrito,
        'items': carrito.items.all(),
        'total_precio': carrito.total_precio(),
    }
    return render(request, 'carrito/ver_carrito.html', contexto)

@login_required
def eliminar_del_carrito(request, item_id):
    if (fuera := solo_clientes(request)) is not None:
        return fuera
    if request.method != 'POST':
        return redirect('apps.carrito:ver_carrito')
    carrito= get_object_or_404(Carrito, usuario=request.user)
    item = carrito.items.filter(id=item_id).first()
   
    if item:
        if item.cantidad > 1:
            # Si hay más de uno, restamos 1 a la cantidad
            item.cantidad -= 1
            item.save()
            messages.info(request, f"Se quitó una unidad de {item.producto.nombre}.")
        else:
            # Si solo queda uno, eliminamos el registro por completo
            item.delete()
            messages.warning(request, f"{item.producto.nombre} fue eliminado del carrito.")
    
    return redirect('apps.carrito:ver_carrito')

@login_required
def vaciar_carrito(request):
    if (fuera := solo_clientes(request)) is not None:
        return fuera
    if request.method != 'POST':
        return redirect('apps.carrito:ver_carrito')
    carrito = get_object_or_404(Carrito, usuario=request.user)
    carrito.items.all().delete()
    return redirect('apps.carrito:ver_carrito')

