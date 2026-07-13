from django.urls import path
from .views import buscar_productos
app_name = 'apps.buscador'
urlpatterns = [
    path('', buscar_productos, name='buscar_productos'),
]