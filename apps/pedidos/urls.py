from django.urls import path
from . import views

app_name = 'apps.pedidos'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('confirmar/', views.confirmar_pedido, name='confirmar_pedido'),
    path('pago/exitoso/', views.pago_exitoso, name='pago_exitoso'),
    path('pago/pendiente/', views.pago_pendiente, name='pago_pendiente'),
    path('pago/fallido/', views.pago_fallido, name='pago_fallido'),
    path('webhook/mercadopago/', views.webhook_mercadopago, name='webhook_mercadopago'),
    path('<int:pk>/pago-qr/', views.pago_qr, name='pago_qr'),
    path('<int:pk>/confirmar-qr/', views.confirmar_pago_qr, name='confirmar_pago_qr'),
    path('mis-pedidos/', views.mis_pedidos, name='mis_pedidos'),
    path('gestion/', views.listar_pedidos, name='listar_pedidos'),
    path('<int:pk>/', views.detalle_pedido, name='detalle_pedido'),
    path('<int:pk>/cambiar-estado/', views.cambiar_estado_pedido, name='cambiar_estado_pedido'),
    path('<int:pk>/cambiar-estado-pago/', views.cambiar_estado_pago, name='cambiar_estado_pago'),
]
