from django.urls import path
from .views import registrar_usuario, ingresar_usuario, cerrar_sesion, perfil_usuario

app_name = 'apps.autenticacion'

urlpatterns = [    # Aquí puedes agregar las rutas de autenticación
    path('registrar/', registrar_usuario, name='registrar'),
    path('ingresar/', ingresar_usuario, name='ingresar'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('perfil/', perfil_usuario, name='perfil'),  # Nueva ruta para el perfil de usuario
]
 