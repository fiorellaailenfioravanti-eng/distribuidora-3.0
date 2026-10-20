"""Rutas raíz del proyecto: cada app expone las suyas bajo su prefijo."""
from django.contrib import admin
from django.urls import path, include
from .views import inicio, resumen_dashboard
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('dashboard/', resumen_dashboard, name='dashboard'),
    path('productos/', include('apps.productos.urls')),
    path('auth/',include('apps.autenticacion.urls')),
    path('carrito/', include('apps.carrito.urls')),
    path('buscador/', include('apps.buscador.urls')),
    path('logistica/', include('apps.logistica.urls')),
    path('clientes/', include('apps.clientes.urls')),
    path('pedidos/', include('apps.pedidos.urls')),
    path('empleados/', include('apps.empleados.urls')),
    path('cuentas/', include('apps.cuentas.urls')),
    path('abonos/', include('apps.abonos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
