from django.contrib import admin

from .models import Abono


@admin.register(Abono)
class AbonoAdmin(admin.ModelAdmin):
    list_display  = ('id_abono', 'cliente', 'producto', 'fecha_inicio', 'costo_mensual',
                     'dia_facturacion', 'estado', 'ultima_facturacion')
    list_filter   = ('estado',)
    search_fields = ('cliente__nombre', 'cliente__apellido', 'producto__nombre')
    date_hierarchy = 'fecha_inicio'
