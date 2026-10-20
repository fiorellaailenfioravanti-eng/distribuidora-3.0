from django.urls import path
from . import views

app_name = 'apps.cuentas'

urlpatterns = [
    path('',                            views.listar_cuentas,    name='listar_cuentas'),
    path('<int:pk>/',                   views.ver_cuenta,        name='ver_cuenta'),
    path('cliente/<int:cliente_pk>/',   views.cuenta_de_cliente, name='cuenta_de_cliente'),
    path('<int:pk>/cargo/',             views.registrar_cargo,   name='registrar_cargo'),
    path('<int:pk>/pago/',              views.registrar_pago,    name='registrar_pago'),
]
