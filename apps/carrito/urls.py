from django.urls import path
from .views import ver_carrito, agregar_al_carrito, eliminar_del_carrito,vaciar_carrito

app_name = 'apps.carrito'
urlpatterns = [
    path('', ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),  
    path('eliminar/<int:item_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('vaciar/', vaciar_carrito, name='vaciar_carrito'),
    
]