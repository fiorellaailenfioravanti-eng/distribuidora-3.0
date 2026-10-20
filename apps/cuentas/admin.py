from django.contrib import admin

from .models import CuentaCorriente, MovimientoCuenta


class MovimientoCuentaInline(admin.TabularInline):
    model   = MovimientoCuenta
    extra   = 0
    fields  = ('tipo', 'monto', 'descripcion', 'fecha_vencimiento', 'pedido', 'abono')
    readonly_fields = ('fecha',)


@admin.register(CuentaCorriente)
class CuentaCorrienteAdmin(admin.ModelAdmin):
    list_display  = ('id_cuenta', 'cliente', 'saldo', 'limite_credito', 'activa', 'fecha_apertura')
    list_filter   = ('activa',)
    search_fields = ('cliente__nombre', 'cliente__apellido', 'cliente__usuario__username')
    inlines       = [MovimientoCuentaInline]
    readonly_fields = ('saldo',)


@admin.register(MovimientoCuenta)
class MovimientoCuentaAdmin(admin.ModelAdmin):
    list_display  = ('id_movimiento', 'cuenta', 'tipo', 'monto', 'descripcion', 'fecha')
    list_filter   = ('tipo', 'fecha')
    search_fields = ('cuenta__cliente__nombre', 'cuenta__cliente__apellido', 'descripcion')
    date_hierarchy = 'fecha'
