from django.urls import path
from .views import listar_productos, listar_productos_admin, crear_producto, ver_producto, editar_producto, eliminar_producto, crear_categoria

app_name = 'apps.productos'
urlpatterns = [
    # Aquí puedes agregar las rutas específicas de la aplicación 'productos'
    # CRUD
    # C = Crear producto 
    path('crear/', crear_producto, name='crear_producto'),
    path('categoria/crear/', crear_categoria, name='crear_categoria'),

    # R = Leer productos
    path('', listar_productos, name='listar_productos'),
    path('admin-panel/', listar_productos_admin, name='listar_productos_admin'),
    path('producto/<int:pk>', ver_producto, name='ver_producto'),

    # U = Actualizar producto
    path('editar/<int:pk>', editar_producto, name='editar_producto'),

    # D = Eliminar producto
    path('eliminar/<int:pk>', eliminar_producto, name='eliminar_producto'),
]