from django.urls import path

from . import views

app_name = 'apps.configuracion'

urlpatterns = [
    path('', views.configuracion, name='configuracion'),
    path('probar-correo/', views.probar_correo, name='probar_correo'),
]
