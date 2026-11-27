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
        # Cantidad de unidades en el carrito (productos y packs de promoción)
        return (sum(item.cantidad for item in self.items.all())
                + sum(p.cantidad for p in self.promociones.all()))

    def total_precio(self):
        # Precio total del carrito: productos + packs de promoción
        return (sum(item.subtotal() for item in self.items.all())
                + sum(p.subtotal() for p in self.promociones.all()))

    def esta_vacio(self):
        return not self.items.exists() and not self.promociones.exists()

    def vaciar(self):
        self.items.all().delete()
        self.promociones.all().delete()


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


class PromocionCarrito(models.Model):
    """Pack de promoción prepaga en el carrito (RF-09). Al confirmar el pedido se
    paga el precio del pack y el cliente recibe el saldo de unidades."""
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='promociones')
    promocion = models.ForeignKey('promociones.Promocion', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1, verbose_name='Packs')

    class Meta:
        unique_together = ('carrito', 'promocion')

    def __str__(self):
        return f"{self.cantidad} x {self.promocion.nombre}"

    def subtotal(self):
        return self.cantidad * self.promocion.precio

    def unidades(self):
        """Unidades de saldo que suma al comprarla."""
        return self.cantidad * self.promocion.cant_lleva
