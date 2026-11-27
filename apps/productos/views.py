"""Catálogo: tienda pública, inventario del panel y ABM de categorías."""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from apps.permisos.roles import puede, requiere
from .forms import CategoriaForm, EnvaseForm, ProductoForm, bidones_retornables
from .models import Categoria, Producto


def agotados_al_final(productos):
    """Anota el stock disponible y ordena con stock primero y los agotados al final
    (dentro de cada grupo, por nombre)."""
    from django.db.models import Case, IntegerField, Value, When
    from apps.pedidos.services import con_stock_disponible
    return con_stock_disponible(productos).annotate(
        agotado=Case(When(disponible__gt=0, then=Value(0)), default=Value(1), output_field=IntegerField())
    ).order_by('agotado', 'nombre')


def _filtrar_por_categoria(request, productos):
    categoria = request.GET.get('categoria', '').strip()
    if categoria:
        productos = productos.filter(categoria__nombre__icontains=categoria).distinct()
    return productos, categoria


# ─────────────────────────────────────────────────────────────
# PRODUCTOS
# ─────────────────────────────────────────────────────────────
# Categoría propia del catálogo para las promociones prepagas (RF-09). No es una
# `Categoria` de productos: al elegirla se muestran sólo las promociones activas.
CATEGORIA_PROMOCIONES = 'Promociones'


def listar_productos(request):
    from apps.promociones.models import Promocion
    promociones = Promocion.objects.filter(activa=True, producto__activo=True).select_related('producto')
    categoria_actual = request.GET.get('categoria', '').strip()
    if categoria_actual == CATEGORIA_PROMOCIONES:
        # Las promociones se compran desde su categoría, como tarjetas.
        productos = Producto.objects.none()
    else:
        productos, categoria_actual = _filtrar_por_categoria(request, Producto.objects.filter(activo=True))
        productos = agotados_al_final(productos)
    return render(request, 'productos/listar_productos.html', {
        'productos': Paginator(productos, 6).get_page(request.GET.get('page')),
        'promociones': promociones if categoria_actual == CATEGORIA_PROMOCIONES else [],
        'cantidad_promociones': promociones.count(),
        'categoria_promociones': CATEGORIA_PROMOCIONES,
        'categorias': Categoria.objects.vigentes().order_by('nombre'),
        'categoria_actual': categoria_actual,
    })


@login_required
@requiere('ver_inventario')
def listar_productos_admin(request):
    productos, categoria_actual = _filtrar_por_categoria(
        request, Producto.objects.filter(activo=True).prefetch_related('categoria').order_by('nombre'))
    from apps.pedidos.services import con_stock_disponible
    productos = con_stock_disponible(productos)
    return render(request, 'productos/listar_productos_admin.html', {
        'productos': Paginator(productos, 20).get_page(request.GET.get('page')),
        'eliminados': Producto.objects.filter(activo=False).prefetch_related('categoria').order_by('nombre'),
        'categorias': Categoria.objects.vigentes().order_by('nombre'),
        'categoria_actual': categoria_actual,
    })


def ver_producto(request, pk):
    """Detalle de un producto; los inactivos sólo los ve el personal."""
    filtros = {} if puede(request.user, 'ver_inventario') else {'activo': True}
    from apps.pedidos.services import con_stock_disponible
    producto = get_object_or_404(con_stock_disponible(Producto.objects.all()), id_producto=pk, **filtros)
    return render(request, 'productos/ver_producto.html', {'producto': producto})


@login_required
@requiere('gestionar_productos')
def crear_producto(request):
    form = ProductoForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        producto = form.save()
        messages.success(request, f'Producto "{producto.nombre}" creado.')
        return redirect('apps.productos:listar_productos_admin')
    return render(request, 'productos/crear_producto.html', {'form': form})


@login_required
@requiere('gestionar_productos')
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, id_producto=pk)
    form = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'Producto "{producto.nombre}" actualizado.')
        return redirect('apps.productos:listar_productos_admin')
    return render(request, 'productos/editar_producto.html', {'form': form, 'producto': producto})


@login_required
@requiere('gestionar_productos')
def eliminar_producto(request, pk):
    """«Eliminar» no borra: desactiva el producto (deja de verse en la tienda y
    no se puede comprar) y lo pasa a la lista de eliminados, desde donde se restaura.
    Así se conservan los pedidos, el stock y el historial que lo usan."""
    producto = get_object_or_404(Producto, id_producto=pk)
    if request.method == 'POST':
        producto.activo = False
        producto.save(update_fields=['activo'])
        messages.success(request, f'«{producto.nombre}» se eliminó de la tienda. '
                                  'Lo podés restaurar desde «Productos eliminados».')
        return redirect('apps.productos:listar_productos_admin')
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})


@login_required
@requiere('gestionar_productos')
def restaurar_producto(request, pk):
    producto = get_object_or_404(Producto, id_producto=pk)
    if request.method == 'POST':
        producto.activo = True
        producto.save(update_fields=['activo'])
        messages.success(request, f'«{producto.nombre}» volvió a la tienda.')
    return redirect('apps.productos:listar_productos_admin')


# ─────────────────────────────────────────────────────────────
# ENVASES ASOCIADOS
# ─────────────────────────────────────────────────────────────
@login_required
@requiere('gestionar_productos')
def envases(request):
    """Envases vacíos, bidones sin envase y mini alta para generar uno y asociarlo."""
    bidon = request.GET.get('bidon', '')
    form = EnvaseForm(request.POST or None,
                      initial={'bidones': [bidon]} if bidon.isdigit() else None)
    if request.method == 'POST' and form.is_valid():
        envase = form.save()
        asociados = len(form.cleaned_data['bidones'])
        messages.success(request, f'Envase «{envase.nombre}» generado'
                                  + (f' y asociado a {asociados} bidón(es).' if asociados else '.'))
        return redirect('apps.productos:envases')
    bidones = bidones_retornables()
    todos = Producto.objects.filter(es_envase=True).prefetch_related('productos_que_lo_usan').order_by('nombre')
    return render(request, 'productos/envases.html', {
        'form': form,
        'envases': todos.filter(activo=True),
        'eliminados': todos.filter(activo=False),
        'sin_envase': [b for b in bidones if b.envase_id is None],
    })


@login_required
@requiere('gestionar_productos')
def eliminar_envase(request, pk):
    """Baja lógica de un envase: sale de «Envases asociados» y de «Stock de bidones».
    No se permite mientras un bidón activo lo use (la planta lo necesita para recargar)."""
    envase = get_object_or_404(Producto, id_producto=pk, es_envase=True)
    if request.method == 'POST':
        en_uso = list(envase.productos_que_lo_usan.filter(activo=True).values_list('nombre', flat=True))
        if en_uso:
            messages.error(request, f'«{envase.nombre}» lo usan: {", ".join(en_uso)}. '
                                    'Asociales otro envase antes de eliminarlo.')
        else:
            envase.activo = False
            envase.save(update_fields=['activo'])
            messages.success(request, f'Envase «{envase.nombre}» eliminado. '
                                      'Lo podés restaurar desde «Envases eliminados».')
    return redirect('apps.productos:envases')


@login_required
@requiere('gestionar_productos')
def restaurar_envase(request, pk):
    envase = get_object_or_404(Producto, id_producto=pk, es_envase=True)
    if request.method == 'POST':
        envase.activo = True
        envase.save(update_fields=['activo'])
        messages.success(request, f'Envase «{envase.nombre}» restaurado.')
    return redirect('apps.productos:envases')


# ─────────────────────────────────────────────────────────────
# CATEGORÍAS
# ─────────────────────────────────────────────────────────────
@login_required
@requiere('gestionar_categorias')
def listar_categorias(request):
    """Listado con alta en la misma pantalla."""
    form = CategoriaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        categoria = form.save()
        messages.success(request, f'Categoría "{categoria.nombre}" creada.')
        return redirect('apps.productos:listar_categorias')
    con_cantidad = Categoria.objects.annotate(cantidad_productos=Count('producto')).order_by('nombre')
    return render(request, 'productos/listar_categorias.html', {
        'categorias': con_cantidad.filter(eliminada=False),
        'eliminadas': con_cantidad.filter(eliminada=True),
        'form': form,
    })


@login_required
@requiere('gestionar_categorias')
def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        categoria = form.save()
        messages.success(request, f'Categoría "{categoria.nombre}" creada.')
        return redirect('apps.productos:listar_categorias')
    return render(request, 'productos/crear_categoria.html', {'form': form})


@login_required
@requiere('gestionar_categorias')
def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'Categoría "{categoria.nombre}" actualizada.')
        return redirect('apps.productos:listar_categorias')
    return render(request, 'productos/crear_categoria.html', {'form': form, 'categoria': categoria})


@login_required
@requiere('gestionar_categorias')
def eliminar_categoria(request, pk):
    """Baja lógica: deja de verse en la tienda y para elegir; sus productos no cambian.
    Se restaura desde «Categorías eliminadas»."""
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.eliminada = True
        categoria.save(update_fields=['eliminada'])
        messages.success(request, f'Categoría "{categoria.nombre}" eliminada. '
                                  'La podés restaurar desde «Categorías eliminadas».')
    return redirect('apps.productos:listar_categorias')


@login_required
@requiere('gestionar_categorias')
def restaurar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.eliminada = False
        categoria.save(update_fields=['eliminada'])
        messages.success(request, f'Categoría "{categoria.nombre}" restaurada.')
    return redirect('apps.productos:listar_categorias')
