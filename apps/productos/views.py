from django.shortcuts import render, redirect
#para hacer la paginación 
from django.core.paginator import Paginator
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm
#Decoradores para permisos (opcional)

#para añadir permisos desde el backend
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404 # Agrega get_object_or_404 aquí
from django.contrib import messages
from django.db.models import ProtectedError
from apps.permisos.roles import es_admin_o_vendedor

#CRUD
#Aca empeiza Read

def listar_productos(request):
    listar_productos = Producto.objects.filter(activo=True).order_by('nombre')
    #esto es para filtrar por categoria
    parametro_categoria = request.GET.get('categoria',"").strip()
    #filtrar por categoria
    if parametro_categoria:
        listar_productos = listar_productos.filter(categoria__nombre__icontains=parametro_categoria)

    paginator = Paginator(listar_productos, 6) # Mostrar 6 productos por página
    page_number = request.GET.get('page') # Obtener el número de página de la solicitud
    page_obj = paginator.get_page(page_number) # Obtener los productos para la página actual
    
    #obtener todos los productos mediante contexto
    contexto = {
        'productos': page_obj,
        'categorias': Categoria.objects.all(),
        'categoria_actual': parametro_categoria # Útil para mantener el filtro en los links
    }
    return render(request, 'productos/listar_productos.html', contexto)

@login_required
@user_passes_test(es_admin_o_vendedor, login_url='/')
def listar_productos_admin(request):
    listar_productos = Producto.objects.order_by('nombre')
    parametro_categoria = request.GET.get('categoria',"").strip()
    
    if parametro_categoria:
        listar_productos = listar_productos.filter(categoria__nombre__icontains=parametro_categoria)

    paginator = Paginator(listar_productos, 20) # Mostrar más productos en tabla
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    contexto = {
        'productos': page_obj,
        'categorias': Categoria.objects.all(),
        'categoria_actual': parametro_categoria
    }
    return render(request, 'productos/listar_productos_admin.html', contexto)

# Create your views here.


def ver_producto(request, pk):
    """Detalle de un producto; los inactivos sólo los ve el personal."""
    filtros = {} if es_admin_o_vendedor(request.user) else {'activo': True}
    producto = get_object_or_404(Producto, id_producto=pk, **filtros)
    return render(request, 'productos/ver_producto.html', {'producto': producto})

#Aca termina Read   
    


#Create
#MI DECORADOR SERIA ESTE PARA QUE VERIFIQUE SI ES VENDEDOR
@login_required
@user_passes_test(es_admin_o_vendedor, login_url='/')
def crear_producto(request):   
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('apps.productos:listar_productos_admin')
    else:
        form = ProductoForm()   
    return render(request, 'productos/crear_producto.html', {'form': form})


@login_required
@user_passes_test(es_admin_o_vendedor, login_url='/')
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('apps.productos:listar_productos_admin')
    else:
        form = CategoriaForm()
    return render(request, 'productos/crear_categoria.html', {'form': form})


#Update
@login_required
@user_passes_test(es_admin_o_vendedor, login_url='/')
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, id_producto=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('apps.productos:listar_productos_admin')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/editar_producto.html', {'form': form, 'producto': producto})





#Delete 
@login_required
@user_passes_test(es_admin_o_vendedor, login_url='/')
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
