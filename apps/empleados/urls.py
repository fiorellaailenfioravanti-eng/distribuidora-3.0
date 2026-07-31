from django.urls import path
from . import views

app_name = 'apps.empleados'

urlpatterns = [
    path('', views.listar_empleados, name='listar_empleados'),
    path('nuevo/', views.crear_empleado, name='crear_empleado'),
    path('<int:pk>/', views.ver_empleado, name='ver_empleado'),
    path('<int:pk>/editar/', views.editar_empleado, name='editar_empleado'),
    path('<int:pk>/estado/', views.cambiar_estado_empleado, name='cambiar_estado'),
    path('<int:pk>/eliminar/', views.eliminar_empleado, name='eliminar_empleado'),
    path('roles/', views.listar_roles, name='listar_roles'),
    path('roles/nuevo/', views.crear_rol, name='crear_rol'),
    path('roles/<int:pk>/editar/', views.editar_rol, name='editar_rol'),
    path('roles/<int:pk>/eliminar/', views.eliminar_rol, name='eliminar_rol'),
]
