from django.urls import path

from . import views

app_name = 'apps.promociones'

urlpatterns = [
    path('',                              views.listar_promociones, name='listar_promociones'),
    path('nueva/',                        views.crear_promocion,    name='crear_promocion'),
    path('<int:pk>/editar/',              views.editar_promocion,   name='editar_promocion'),
    path('vender/<int:cliente_pk>/',      views.vender_promocion,   name='vender_promocion'),
]
