from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombre', 'descripcion')
    search_fields = ('nombre',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'precio', 'stock', 'fecha_creacion', 'fecha_actualizacion')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'descripcion')
    filter_horizontal = ('categoria',)
    
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)