from django.urls import path
from . import views

app_name = 'apps.abonos'

urlpatterns = [
    path('',                     views.listar_abonos,       name='listar_abonos'),
    path('nuevo/',               views.crear_abono,         name='crear_abono'),
    path('generar-cargos/',      views.generar_cargos,      name='generar_cargos'),
    path('<int:pk>/',            views.ver_abono,           name='ver_abono'),
    path('<int:pk>/editar/',     views.editar_abono,        name='editar_abono'),
    path('<int:pk>/estado/',     views.cambiar_estado_abono, name='cambiar_estado_abono'),
]
