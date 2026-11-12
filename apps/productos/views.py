"""Catálogo: tienda pública, inventario del panel y ABM de categorías."""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count, ProtectedError
from django.shortcuts import get_object_or_404, redirect, render

from apps.permisos.roles import puede, requiere
from .forms import CategoriaForm, ProductoForm
from .models import Categoria, Producto


def _filtrar_por_categoria(request, productos):
    categoria = request.GET.get('categoria', '').strip()
    if categoria:
        productos = productos.filter(categoria__nombre__icontains=categoria).distinct()
    return productos, categoria


# ─────────────────────────────────────────────────────────────
# PRODUCTOS
# ─────────────────────────────────────────────────────────────
def listar_productos(request):
    productos, categoria_actual = _filtrar_por_categoria(
        request, Producto.objects.filter(activo=True).order_by('nombre'))
    return render(request, 'productos/listar_productos.html', {
        'productos': Paginator(productos, 6).get_page(request.GET.get('page')),
        'categorias': Categoria.objects.order_by('nombre'),
        'categoria_actual': categoria_actual,
    })


@login_required
@requiere('ver_inventario')
def listar_productos_admin(request):
    productos, categoria_actual = _filtrar_por_categoria(
        request, Producto.objects.prefetch_related('categoria').order_by('nombre'))
    return render(request, 'productos/listar_productos_admin.html', {
        'productos': Paginator(productos, 20).get_page(request.GET.get('page')),
        'categorias': Categoria.objects.order_by('nombre'),
        'categoria_actual': categoria_actual,
    })


def ver_producto(request, pk):
    """Detalle de un producto; los inactivos sólo los ve el personal."""
    filtros = {} if puede(request.user, 'ver_inventario') else {'activo': True}
    producto = get_object_or_404(Producto, id_producto=pk, **filtros)
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
    """Borra el producto; si ya tiene pedidos (PROTECT), lo desactiva (H-27)."""
    producto = get_object_or_404(Producto, id_producto=pk)
    if request.method == 'POST':
        try:
            producto.delete()
            messages.success(request, f'Producto "{producto.nombre}" eliminado.')
        except ProtectedError:
            producto.activo = False
            producto.save(update_fields=['activo'])
            messages.warning(
                request,
                f'"{producto.nombre}" tiene pedidos registrados y no se puede borrar: '
                'se desactivó y ya no aparece en la tienda.'
            )
        return redirect('apps.productos:listar_productos_admin')
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})


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
    categorias = Categoria.objects.annotate(cantidad_productos=Count('producto')).order_by('nombre')
    return render(request, 'productos/listar_categorias.html', {'categorias': categorias, 'form': form})


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
    """Sólo se borran categorías vacías, para no dejar productos sin clasificar."""
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        en_uso = categoria.producto_set.count()
        if en_uso:
            messages.error(
                request,
                f'"{categoria.nombre}" tiene {en_uso} producto(s). Pasalos a otra categoría antes de borrarla.'
            )
        else:
            categoria.delete()
            messages.success(request, f'Categoría "{categoria.nombre}" eliminada.')
    return redirect('apps.productos:listar_categorias')
