from django.contrib import admin

from .models import CompraPromocion, ConsumoPromocion, Promocion


@admin.register(Promocion)
class PromocionAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'producto', 'cant_paga', 'cant_lleva', 'precio', 'dias_validez', 'activa')
    list_filter   = ('activa',)
    search_fields = ('nombre', 'producto__nombre')


class ConsumoPromocionInline(admin.TabularInline):
    model = ConsumoPromocion
    extra = 0
    readonly_fields = ('pedido', 'cantidad', 'fecha')
    can_delete = False


@admin.register(CompraPromocion)
class CompraPromocionAdmin(admin.ModelAdmin):
    list_display  = ('cliente', 'promocion', 'fecha_compra', 'fecha_caducidad', 'unid_restantes', 'unid_totales', 'estado')
    list_filter   = ('estado', 'promocion')
    search_fields = ('cliente__nombre', 'cliente__apellido')
    readonly_fields = ('pedido',)
    inlines = [ConsumoPromocionInline]
