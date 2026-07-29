from django.contrib import admin
from .models import Zona, RolEmpleado, Empleado, Camion, HojaRuta, DetalleHojaRuta


@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
    list_display  = ('id_zona', 'nombre', 'descripcion')
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


class DetalleHojaRutaInline(admin.TabularInline):
    model  = DetalleHojaRuta
    extra  = 1
    fields = ('orden', 'cliente_nombre', 'direccion', 'pedido_ref', 'estado', 'nota_entrega', 'hora_registro')
    readonly_fields = ('hora_registro',)
    ordering = ('orden',)


@admin.register(HojaRuta)
class HojaRutaAdmin(admin.ModelAdmin):
    list_display   = ('id_ruta', 'fecha', 'empleado', 'camion', 'zona', 'estado',
                      'total_paradas', 'paradas_entregadas', 'porcentaje_completado')
    list_filter    = ('estado', 'zona', 'fecha')
    search_fields  = ('empleado__usuario__username', 'zona__nombre')
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
                     'direccion', 'estado', 'hora_registro')
    list_filter   = ('estado', 'hoja_ruta__zona')
    search_fields = ('cliente_nombre', 'pedido_ref', 'direccion')
    readonly_fields = ('hora_registro',)
