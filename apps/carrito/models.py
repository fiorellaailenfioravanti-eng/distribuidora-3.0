from django.db import models
from django.conf import settings
from apps.productos.models import Producto

# Create your models here.
class Carrito(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='carrito')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Carrito de {self.usuario.username}"
    
    def total_items(self):
        #devuelve la cantidad total de items en el carrito
        return sum(item.cantidad for item in self.items.all())
    
    def total_precio(self):
        #devuelve el precio total del carrito
        return sum(item.subtotal() for item in self.items.all())
    

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('carrito', 'producto')

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
    
    def subtotal(self):
        #devuelve el subtotal del item en el carrito
        return self.cantidad * self.producto.precio