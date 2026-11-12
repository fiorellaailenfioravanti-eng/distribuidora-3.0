from django.urls import path

from . import views

app_name = 'apps.planta'
urlpatterns = [
    path('recarga/', views.recarga_diaria, name='recarga_diaria'),
    path('stock/', views.stock_bidones, name='stock_bidones'),
]
