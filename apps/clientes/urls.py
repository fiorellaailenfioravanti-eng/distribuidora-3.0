from django.urls import path
from . import views

app_name = 'apps.clientes'

urlpatterns = [
    # ── Panel de clientes ──────────────────────────────────────
    path('',                              views.listar_clientes,         name='listar_clientes'),

    # Selector de tipo de alta
    path('nuevo/',                        views.crear_cliente,            name='crear_cliente'),
    # Alta sin cuenta web (solo Admin/Vendedor)
    path('nuevo/sin-cuenta/',             views.crear_cliente_sin_cuenta, name='crear_sin_cuenta'),
    # Alta con cuenta web (genera usuario + cliente)
    path('nuevo/con-cuenta/',             views.crear_cliente_con_cuenta, name='crear_con_cuenta'),

    path('<int:pk>/',                     views.ver_cliente,              name='ver_cliente'),
    path('<int:pk>/editar/',              views.editar_cliente,           name='editar_cliente'),
    path('<int:pk>/tipo/',                views.cambiar_tipo_cliente,     name='cambiar_tipo'),

    # ── Teléfonos ──────────────────────────────────────────────
    path('<int:pk>/telefono/nuevo/',      views.agregar_telefono,         name='agregar_telefono'),
    path('telefono/<int:pk>/eliminar/',   views.eliminar_telefono,        name='eliminar_telefono'),

    # ── Direcciones ────────────────────────────────────────────
    path('<int:pk>/direccion/nueva/',     views.agregar_direccion,        name='agregar_direccion'),
    path('direccion/<int:pk>/editar/',    views.editar_direccion,         name='editar_direccion'),
    path('direccion/<int:pk>/eliminar/',  views.eliminar_direccion,       name='eliminar_direccion'),

    # ── Perfil propio del cliente ──────────────────────────────
    path('mi-perfil/',                    views.mi_perfil_cliente,        name='mi_perfil'),
    path('mi-perfil/editar/',             views.editar_mi_perfil,         name='editar_mi_perfil'),
]
