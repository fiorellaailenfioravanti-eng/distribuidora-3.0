from django.contrib import admin
from .models import Cliente, TelefonoContacto, DireccionEntrega


class TelefonoContactoInline(admin.TabularInline):
    model   = TelefonoContacto
    extra   = 1
    fields  = ('numero', 'desc_relacion', 'es_principal')


class DireccionEntregaInline(admin.TabularInline):
    model   = DireccionEntrega
    extra   = 1
    fields  = ('calle', 'altura', 'piso_depto', 'zona', 'desc_seguridad', 'coordenadas', 'es_principal')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display   = ('nombre_completo', 'usuario', 'tipo_cliente', 'bidones_prestados',
                      'permite_fiado', 'cantidad_telefonos', 'cantidad_direcciones',
                      'tiene_datos_completos', 'fecha_alta')
    list_filter    = ('tipo_cliente', 'permite_fiado')
    search_fields  = ('usuario__username', 'usuario__first_name',
                      'usuario__last_name', 'usuario__email', 'dni')
    readonly_fields = ('fecha_alta',)
    inlines        = [TelefonoContactoInline, DireccionEntregaInline]

    fieldsets = (
        ('Datos de autenticación', {
            'fields': ('usuario',)
        }),
        ('Datos personales', {
            'fields': ('dni', 'fecha_nacimiento')
        }),
        ('Clasificación comercial', {
            'fields': ('tipo_cliente', 'permite_fiado', 'bidones_prestados')
        }),
        ('Notas internas', {
            'fields': ('notas_internas',),
            'classes': ('collapse',),
        }),
        ('Metadata', {
            'fields': ('fecha_alta',),
            'classes': ('collapse',),
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('usuario')


@admin.register(TelefonoContacto)
class TelefonoContactoAdmin(admin.ModelAdmin):
    list_display  = ('cliente', 'numero', 'desc_relacion', 'es_principal')
    list_filter   = ('es_principal',)
    search_fields = ('cliente__usuario__username', 'numero')


@admin.register(DireccionEntrega)
class DireccionEntregaAdmin(admin.ModelAdmin):
    list_display  = ('cliente', 'calle', 'altura', 'piso_depto', 'zona', 'es_principal')
    list_filter   = ('zona', 'es_principal')
    search_fields = ('cliente__usuario__username', 'calle')
