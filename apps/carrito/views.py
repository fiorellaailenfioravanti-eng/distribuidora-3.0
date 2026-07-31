from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Carrito, ItemCarrito
from apps.productos.models import Producto
from django.urls import reverse
from django.contrib import messages


# Create your views here.
def es_staff_or_admin(user):
    return user.is_superuser or user.groups.filter(name='Vendedor').exists()


@login_required
def agregar_al_carrito(request, producto_id):
    if es_staff_or_admin(request.user):
        messages.info(request, "Los usuarios administradores y vendedores gestionan la tienda y no realizan compras desde el carrito.")
        return redirect('dashboard')

    producto = get_object_or_404(Producto, id_producto=producto_id)
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    item_carrito, creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)

    # Verificamos si la cantidad actual en el carrito + 1 supera el stock disponible
    nueva_cantidad = item_carrito.cantidad + (0 if creado else 1)
    
    if producto.stock >= nueva_cantidad:
        if not creado:
            item_carrito.cantidad += 1
            item_carrito.save()
        messages.success(request, f"{producto.nombre} se añadió al carrito.")
    else:
        messages.error(request, f"Lo sentimos, no hay suficiente stock de {producto.nombre}. (Máximo: {producto.stock})")
        # Si acababa de ser creado pero no hay stock, lo borramos
        if creado:
            item_carrito.delete()
    
    referer = request.META.get('HTTP_REFERER')
    if referer and 'producto' in referer:
        return redirect('apps.productos:ver_producto', pk=producto.id_producto)
    return redirect('apps.productos:listar_productos')


@login_required
def ver_carrito(request):
    if es_staff_or_admin(request.user):
        messages.info(request, "Los usuarios administradores y vendedores gestionan los pedidos desde la consola.")
        return redirect('dashboard')

    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    contexto = {
        'carrito': carrito,
        'items': carrito.items.all(),
        'total_precio': carrito.total_precio(),
    }
    return render(request, 'carrito/ver_carrito.html', contexto)

@login_required
def eliminar_del_carrito(request, item_id):
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
    carrito = get_object_or_404(Carrito, usuario=request.user)
    carrito.items.all().delete()
    return redirect('apps.carrito:ver_carrito')

