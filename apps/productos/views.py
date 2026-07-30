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
#validar grupos a los que pertenece el usuario
#esto seria lo mismo que el filtro en el frontend que se implemento en distribuidora/grupos.py
def es_vendedor_o_admin(user):
    return user.is_superuser or user.groups.filter(name='Vendedor').exists()
#CRUD
#Aca empeiza Read

def listar_productos(request):
    listar_productos = Producto.objects.all()
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

@user_passes_test(es_vendedor_o_admin)
def listar_productos_admin(request):
    listar_productos = Producto.objects.all()
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
    try:
        #obtener detalles de un producto específico mediante contexto
        producto = Producto.objects.get(id_producto=pk)
        contexto = {
            'producto': producto
        }
        return render(request, 'productos/ver_producto.html', contexto)
    
    except Producto.DoesNotExist:
        return render(request, 'productos/ver_producto.html', {'producto': None})

#Aca termina Read   
    


#Create
#MI DECORADOR SERIA ESTE PARA QUE VERIFIQUE SI ES VENDEDOR
@user_passes_test(es_vendedor_o_admin)
#este seria para comprar o añadir a lista de deseos
#abajo le estoy diciendo que debe ser administrador o vendedor para crear productos
# @permission_required('apps.productos.add_producto', raise_exception=True) #lo ultimo devuelve al usuario a login en caso de error
def crear_producto(request):   
    
    
    if request.method == 'POST':
        #post recibe información del formulario
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('apps.productos:listar_productos_admin')

    else:
        #get 
        form = ProductoForm()   
        return render(request, 'productos/crear_producto.html', {'form': form})
    
@user_passes_test(es_vendedor_o_admin)
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('apps.productos:listar_productos')
    else:
        form = CategoriaForm()
    return render(request, 'productos/crear_categoria.html', {'form': form})

#Update
@user_passes_test(es_vendedor_o_admin)
def editar_producto(request, pk):
    producto = Producto.objects.get(id_producto=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('apps.productos:listar_productos_admin')
    else:
        form = ProductoForm(instance=producto)
        return render(request, 'productos/editar_producto.html', {'form': form, 'producto': producto})





#Delete 
@user_passes_test(es_vendedor_o_admin)
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, id_producto=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('apps.productos:listar_productos_admin')
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})