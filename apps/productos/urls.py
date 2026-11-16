from django.urls import path

from . import views

app_name = 'apps.productos'
urlpatterns = [
    # Tienda
    path('', views.listar_productos, name='listar_productos'),
    path('producto/<int:pk>', views.ver_producto, name='ver_producto'),

    # Inventario (panel)
    path('admin-panel/', views.listar_productos_admin, name='listar_productos_admin'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('editar/<int:pk>', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>', views.eliminar_producto, name='eliminar_producto'),
    path('restaurar/<int:pk>', views.restaurar_producto, name='restaurar_producto'),

    # Envases asociados (panel)
    path('envases/', views.envases, name='envases'),
    path('envases/<int:pk>/eliminar/', views.eliminar_envase, name='eliminar_envase'),
    path('envases/<int:pk>/restaurar/', views.restaurar_envase, name='restaurar_envase'),

    # Categorías (panel)
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categoria/crear/', views.crear_categoria, name='crear_categoria'),
    path('categoria/<int:pk>/editar/', views.editar_categoria, name='editar_categoria'),
    path('categoria/<int:pk>/eliminar/', views.eliminar_categoria, name='eliminar_categoria'),
    path('categoria/<int:pk>/restaurar/', views.restaurar_categoria, name='restaurar_categoria'),
]
