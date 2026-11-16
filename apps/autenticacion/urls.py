from django.urls import path

from .views import (
    cerrar_sesion, ingresar_usuario, perfil_usuario, recuperar_codigo, recuperar_contrasena,
    recuperar_listo, recuperar_nueva, recuperar_reenviar, registrar_usuario,
)

app_name = 'apps.autenticacion'

urlpatterns = [
    path('registrar/', registrar_usuario, name='registrar'),
    path('ingresar/', ingresar_usuario, name='ingresar'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('perfil/', perfil_usuario, name='perfil'),

    # Recuperación de contraseña con código temporal por email (recuperacion.py).
    path('recuperar/', recuperar_contrasena, name='recuperar'),
    path('recuperar/codigo/', recuperar_codigo, name='recuperar_codigo'),
    path('recuperar/reenviar/', recuperar_reenviar, name='recuperar_reenviar'),
    path('recuperar/nueva/', recuperar_nueva, name='recuperar_nueva'),
    path('recuperar/listo/', recuperar_listo, name='recuperar_listo'),
]
