"""
Promociones prepagas (RF-09) con caducidad a 30 días corridos (RF-10).

- `Promocion`: la oferta del catálogo, p. ej. «Paga 3, lleva 4» de un producto.
- `CompraPromocion`: el pack que compró un cliente. Paga `cant_paga` unidades y
  recibe un saldo de `cant_lleva` unidades que retira en entregas parciales
  hasta la fecha de caducidad.
- `ConsumoPromocion`: cada entrega que usó parte del saldo.
"""
from datetime import timedelta
from decimal import Decimal

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

DIAS_VALIDEZ_DEFAULT = 30  # RF-10: 30 días corridos

ESTADOS_COMPRA = [
    ('Vigente', 'Vigente'),
    ('Agotada', 'Agotada'),
    ('Vencida', 'Vencida'),
]


class Promocion(models.Model):
    id_promocion = models.AutoField(primary_key=True)
    nombre       = models.CharField(max_length=120, verbose_name='Nombre', help_text='Ej: Paga 3, lleva 4 — Bidón 20 L')
    producto     = models.ForeignKey(
        'productos.Producto',
        on_delete=models.PROTECT,
        related_name='promociones',
        verbose_name='Producto'
    )
    cant_paga    = models.PositiveSmallIntegerField(default=3, verbose_name='Unidades que paga')
    cant_lleva   = models.PositiveSmallIntegerField(default=4, verbose_name='Unidades que lleva')
    precio       = models.DecimalField(
        max_digits=12, decimal_places=2,
        verbose_name='Precio del pack',
        help_text='Lo que paga el cliente por el pack completo.'
    )
    dias_validez = models.PositiveSmallIntegerField(
        default=DIAS_VALIDEZ_DEFAULT,
        verbose_name='Días de validez',
        help_text='Días corridos desde la compra para retirar las unidades (RF-10).'
    )
    activa       = models.BooleanField(default=True, verbose_name='Activa')
    descripcion  = models.TextField(blank=True, verbose_name='Descripción')

    class Meta:
        ordering = ['-activa', 'nombre']
        verbose_name = 'Promoción'
        verbose_name_plural = 'Promociones'

    def __str__(self):
        return self.nombre

    def clean(self):
        if self.cant_paga and self.cant_lleva and self.cant_lleva <= self.cant_paga:
            raise ValidationError({'cant_lleva': 'Debe llevar más unidades de las que paga.'})
        if self.precio is not None and self.precio <= 0:
            raise ValidationError({'precio': 'El precio debe ser mayor a cero.'})

    def unidades_bonificadas(self):
        return self.cant_lleva - self.cant_paga

    def precio_por_unidad(self):
        if not self.cant_lleva:
            return self.precio
        return (self.precio / self.cant_lleva).quantize(Decimal('0.01'))


class CompraPromocion(models.Model):
    id_compra       = models.AutoField(primary_key=True)
    cliente         = models.ForeignKey(
        'clientes.Cliente',
        on_delete=models.CASCADE,
        related_name='compras_promocion',
        verbose_name='Cliente'
    )
    promocion       = models.ForeignKey(
        Promocion,
        on_delete=models.PROTECT,
        related_name='compras',
        verbose_name='Promoción'
    )
    pedido          = models.ForeignKey(
        'pedidos.Pedido',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='compras_promocion',
        verbose_name='Pedido con el que se pagó'
    )
    fecha_compra    = models.DateField(default=timezone.localdate, verbose_name='Fecha de compra')
    fecha_caducidad = models.DateField(verbose_name='Vence', help_text='Último día en que se puede usar el saldo.')
    unid_totales    = models.PositiveSmallIntegerField(verbose_name='Unidades totales')
    unid_restantes  = models.PositiveSmallIntegerField(verbose_name='Unidades restantes')
    estado          = models.CharField(max_length=10, choices=ESTADOS_COMPRA, default='Vigente', verbose_name='Estado')

    class Meta:
        ordering = ['fecha_caducidad', 'id_compra']
        verbose_name = 'Compra de promoción'
        verbose_name_plural = 'Compras de promociones'

    def __str__(self):
        return f'{self.promocion} — {self.cliente.nombre_completo()} ({self.unid_restantes}/{self.unid_totales})'

    def save(self, *args, **kwargs):
        if not self.fecha_caducidad:
            self.fecha_caducidad = self.fecha_compra + timedelta(days=self.promocion.dias_validez)
        super().save(*args, **kwargs)

    @property
    def producto(self):
        return self.promocion.producto

    def esta_vigente(self, fecha=None):
        fecha = fecha or timezone.localdate()
        return self.estado == 'Vigente' and self.unid_restantes > 0 and fecha <= self.fecha_caducidad

    def dias_restantes(self, fecha=None):
        fecha = fecha or timezone.localdate()
        return (self.fecha_caducidad - fecha).days


class ConsumoPromocion(models.Model):
    id_consumo = models.AutoField(primary_key=True)
    compra     = models.ForeignKey(CompraPromocion, on_delete=models.CASCADE, related_name='consumos')
    pedido     = models.ForeignKey(
        'pedidos.Pedido',
        on_delete=models.CASCADE,
        related_name='consumos_promocion',
        verbose_name='Pedido que usó el saldo'
    )
    cantidad   = models.PositiveSmallIntegerField(verbose_name='Unidades usadas')
    fecha      = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Consumo de promoción'
        verbose_name_plural = 'Consumos de promociones'

    def __str__(self):
        return f'{self.cantidad} u. de {self.compra.promocion} en pedido #{self.pedido_id}'
