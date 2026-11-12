from django.contrib import admin

from .models import DetalleRecarga, RecargaBidones


class DetalleRecargaInline(admin.TabularInline):
    model = DetalleRecarga
    extra = 0
    readonly_fields = ('producto', 'cantidad')
    can_delete = False


@admin.register(RecargaBidones)
class RecargaBidonesAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'registrada_por', 'actualizada')
    inlines = [DetalleRecargaInline]
    readonly_fields = ('fecha', 'registrada_por', 'actualizada')
