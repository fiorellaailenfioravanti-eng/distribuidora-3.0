from django.contrib import admin
from .models import Zona, Barrio, RolEmpleado, Empleado, Camion, RutaReparto, HojaRuta, DetalleHojaRuta


@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
    list_display  = ('id_zona', 'nombre', 'descripcion')
    search_fields = ('nombre',)


@admin.register(Barrio)
class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'zona')
    list_filter = ('ciudad', 'zona')
    search_fields = ('nombre',)


@admin.register(RolEmpleado)
class RolEmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id_rol', 'descripcion')


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display  = ('id_empleado', 'usuario', 'rol', 'activo')
    list_filter   = ('rol', 'activo')
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__last_name')


@admin.register(Camion)
class CamionAdmin(admin.ModelAdmin):
    list_display = ('patente', 'descripcion', 'activo')
    list_filter  = ('activo',)


@admin.register(RutaReparto)
class RutaRepartoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'zona', 'dia_semana', 'empleado_default')
    list_filter = ('dia_semana', 'zona')
    search_fields = ('nombre',)


class DetalleHojaRutaInline(admin.TabularInline):
    model  = DetalleHojaRuta
    extra  = 1
    fields = ('orden', 'cliente_nombre', 'direccion_entrega', 'direccion_texto', 'pedido_ref', 'estado', 'nota_entrega', 'hora_registro')
    readonly_fields = ('hora_registro',)
    ordering = ('orden',)


@admin.register(HojaRuta)
class HojaRutaAdmin(admin.ModelAdmin):
    list_display   = ('id_ruta', 'fecha', 'empleado', 'camion', 'ruta_reparto', 'estado',
                      'total_paradas', 'paradas_entregadas', 'porcentaje_completado')
    list_filter    = ('estado', 'ruta_reparto__zona', 'fecha')
    search_fields  = ('empleado__usuario__username', 'ruta_reparto__nombre')
    date_hierarchy = 'fecha'
    inlines        = [DetalleHojaRutaInline]
    readonly_fields = ('creado_por',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.creado_por = request.user
        super().save_model(request, obj, form, change)


@admin.register(DetalleHojaRuta)
class DetalleHojaRutaAdmin(admin.ModelAdmin):
    list_display  = ('id_detalle', 'hoja_ruta', 'orden', 'cliente_nombre',
                     'direccion_texto', 'estado', 'hora_registro')
    list_filter   = ('estado', 'hoja_ruta__ruta_reparto__zona')
    search_fields = ('cliente_nombre', 'pedido_ref', 'direccion_texto')
    readonly_fields = ('hora_registro',)
