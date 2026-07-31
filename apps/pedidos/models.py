from django.db import models
from apps.clientes.models import Cliente, DireccionEntrega
from apps.productos.models import Producto


ESTADOS_PEDIDO = [
    ('Pendiente',   'Pendiente'),
    ('Confirmado',  'Confirmado'),
    ('En Camino',   'En Camino'),
    ('Entregado',   'Entregado'),
    ('Cancelado',   'Cancelado'),
]

ESTADOS_PAGO = [
    ('Pendiente', 'Pendiente de Verificación / Cobro'),
    ('Aprobado',  'Aprobado / Pagado'),
    ('Rechazado', 'Rechazado'),
]


class MetodoPago(models.Model):
    id_metodo   = models.AutoField(primary_key=True)
    nombre      = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    codigo      = models.CharField(max_length=50, unique=True, help_text="Ej: EFECTIVO, MERCADOPAGO")
    activo      = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Método de Pago'
        verbose_name_plural = 'Métodos de Pago'

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    id_pedido          = models.AutoField(primary_key=True)
    cliente            = models.ForeignKey(
        Cliente,
        on_delete=models.SET_NULL,
        null=True,
        related_name='pedidos',
        verbose_name='Cliente'
    )
    direccion_entrega  = models.ForeignKey(
        DireccionEntrega,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='pedidos',
        verbose_name='Dirección de entrega'
    )
    fecha_pedido       = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de pedido')
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado             = models.CharField(
        max_length=20,
        choices=ESTADOS_PEDIDO,
        default='Pendiente',
        verbose_name='Estado del pedido'
    )
    metodo_pago        = models.ForeignKey(
        MetodoPago,
        on_delete=models.PROTECT,
        related_name='pedidos',
        verbose_name='Método de pago'
    )
    total              = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    notas_cliente      = models.TextField(blank=True, verbose_name='Notas de entrega')

    class Meta:
        ordering = ['-fecha_pedido']
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        cliente_str = self.cliente.nombre_completo() if self.cliente else "Cliente anónimo"
        return f"Pedido #{self.id_pedido} — {cliente_str} (${self.total})"

    def cantidad_items(self):
        return sum(item.cantidad for item in self.detalles.all())

    def esta_pagado(self):
        return self.pagos.filter(estado_pago='Aprobado').exists()


class DetallePedido(models.Model):
    id_detalle      = models.AutoField(primary_key=True)
    pedido          = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='detalles'
    )
    producto        = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name='detalles_pedido'
    )
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad        = models.PositiveIntegerField(default=1)
    subtotal        = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = 'Detalle de Pedido'
        verbose_name_plural = 'Detalles de Pedido'

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} (${self.subtotal})"


class PagoPedido(models.Model):
    id_pago                    = models.AutoField(primary_key=True)
    pedido                     = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='pagos'
    )
    monto                      = models.DecimalField(max_digits=12, decimal_places=2)
    metodo_pago                = models.ForeignKey(
        MetodoPago,
        on_delete=models.PROTECT
    )
    fecha                      = models.DateTimeField(auto_now_add=True)
    referencia_comprobante     = models.CharField(max_length=100, blank=True)
    mercadopago_payment_id     = models.CharField(max_length=100, blank=True)
    mercadopago_preference_id  = models.CharField(max_length=100, blank=True)
    mercadopago_status         = models.CharField(max_length=50, blank=True)
    tarjeta_ultimos_4          = models.CharField(max_length=4, blank=True, verbose_name='Últimos 4 dígitos tarjeta')
    tarjeta_titular            = models.CharField(max_length=100, blank=True, verbose_name='Titular de la tarjeta')
    estado_pago                = models.CharField(
        max_length=30,
        choices=ESTADOS_PAGO,
        default='Pendiente'
    )

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Pago de Pedido'
        verbose_name_plural = 'Pagos de Pedidos'

    def __str__(self):
        return f"Pago #{self.id_pago} — Pedido #{self.pedido.id_pedido} (${self.monto}) [{self.estado_pago}]"
