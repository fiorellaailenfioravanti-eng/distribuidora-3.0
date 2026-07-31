from django.urls import path
from . import views

app_name = 'apps.logistica'

urlpatterns = [
    # ── Hojas de Ruta ──────────────────────────────────────────
    path('',                             views.listar_rutas,            name='listar_rutas'),
    path('nueva/',                       views.crear_ruta,              name='crear_ruta'),
    path('<int:pk>/',                    views.ver_ruta,                name='ver_ruta'),
    path('<int:pk>/editar/',             views.editar_ruta,             name='editar_ruta'),
    path('<int:pk>/imprimir/',           views.imprimir_ruta,           name='imprimir_ruta'),

    # ── Paradas ────────────────────────────────────────────────
    path('<int:pk>/parada/agregar/',     views.agregar_parada,          name='agregar_parada'),
    path('parada/<int:pk>/eliminar/',    views.eliminar_parada,         name='eliminar_parada'),
    path('parada/<int:pk>/estado/',      views.actualizar_estado_entrega, name='actualizar_estado_entrega'),

    # ── Vista repartidor ───────────────────────────────────────
    path('mi-ruta/',                     views.mi_ruta_hoy,             name='mi_ruta_hoy'),

    # ── Zonas ──────────────────────────────────────────────────
    path('zonas/',                       views.listar_zonas,            name='listar_zonas'),
    path('zonas/<int:pk>/editar/',       views.editar_zona,             name='editar_zona'),
    path('zonas/<int:pk>/eliminar/',     views.eliminar_zona,           name='eliminar_zona'),
    path('zonas/asignar/',               views.direcciones_sin_zona,    name='direcciones_sin_zona'),

    # ── Camiones ───────────────────────────────────────────────
    path('camiones/',                    views.listar_camiones,         name='listar_camiones'),
    path('camiones/<str:pk>/editar/',    views.editar_camion,           name='editar_camion'),
    path('camiones/<str:pk>/eliminar/',  views.eliminar_camion,         name='eliminar_camion'),
]
