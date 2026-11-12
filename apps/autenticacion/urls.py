from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from .forms import RecuperarContrasenaForm, NuevaContrasenaForm
from .views import registrar_usuario, ingresar_usuario, cerrar_sesion, perfil_usuario

app_name = 'apps.autenticacion'

urlpatterns = [
    path('registrar/', registrar_usuario, name='registrar'),
    path('ingresar/', ingresar_usuario, name='ingresar'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('perfil/', perfil_usuario, name='perfil'),

    # Recuperación de contraseña por email (vistas de Django con templates propios).
    path('recuperar/', auth_views.PasswordResetView.as_view(
        form_class=RecuperarContrasenaForm,
        template_name='autenticacion/recuperar_contrasena.html',
        email_template_name='autenticacion/email_recuperar_contrasena.txt',
        subject_template_name='autenticacion/email_recuperar_asunto.txt',
        success_url=reverse_lazy('apps.autenticacion:recuperar_enviado'),
    ), name='recuperar'),
    path('recuperar/enviado/', auth_views.PasswordResetDoneView.as_view(
        template_name='autenticacion/recuperar_enviado.html',
    ), name='recuperar_enviado'),
    path('recuperar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        form_class=NuevaContrasenaForm,
        template_name='autenticacion/recuperar_nueva.html',
        success_url=reverse_lazy('apps.autenticacion:recuperar_listo'),
    ), name='recuperar_confirmar'),
    path('recuperar/listo/', auth_views.PasswordResetCompleteView.as_view(
        template_name='autenticacion/recuperar_listo.html',
    ), name='recuperar_listo'),
]
