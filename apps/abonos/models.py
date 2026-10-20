import calendar
from datetime import date
from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from apps.clientes.models import Cliente
from apps.productos.models import Producto


# ────────────────────────────────────────────────
# ESTADOS DEL ABONO
# ────────────────────────────────────────────────
ESTADOS_ABONO = [
    ('Activo',     'Activo'),
    ('Suspendido', 'Suspendido'),
    ('Finalizado', 'Finalizado'),
]


# ────────────────────────────────────────────────
# BENEFICIO PREMIUM — RF-05
#    Los clientes Premium acceden a un costo mensual preferencial.
# ────────────────────────────────────────────────
DESCUENTO_PREMIUM = Decimal('0.10')  # 10 %


class Abono(models.Model):
    id_abono          = models.AutoField(primary_key=True)
    cliente           = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='abonos',
        verbose_name='Cliente'
    )
    producto          = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name='abonos',
        verbose_name='Producto alquilado',
        help_text='Dispenser frío/calor u otro equipo en alquiler.'
    )
    fecha_inicio      = models.DateField(verbose_name='Inicio del contrato')
    fecha_fin         = models.DateField(
        null=True,
        blank=True,
        verbose_name='Fin del contrato'
    )
    costo_mensual     = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))],
        verbose_name='Costo mensual'
    )
    dia_facturacion   = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(28)],
        verbose_name='Día de facturación',
        help_text='Día del mes en que se genera el cargo (1-28).'
    )
    estado            = models.CharField(
        max_length=12,
        choices=ESTADOS_ABONO,
        default='Activo',
        verbose_name='Estado'
    )
    ultima_facturacion = models.DateField(
        null=True,
        blank=True,
        verbose_name='Última facturación'
    )
    observaciones     = models.TextField(blank=True, verbose_name='Observaciones')
    fecha_creacion    = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering            = ['-fecha_inicio', 'cliente__apellido']
        verbose_name        = 'Abono'
        verbose_name_plural = 'Abonos'

    def __str__(self):
        return f"Abono #{self.id_abono} — {self.cliente.nombre_completo()} / {self.producto.nombre}"

    # ── Estado ─────────────────────────────────────────────────
    def esta_activo(self):
        return self.estado == 'Activo'

    def vencido(self, referencia=None):
        referencia = referencia or date.today()
        return self.fecha_fin is not None and self.fecha_fin < referencia

    @property
    def esta_vencido(self):
        return self.vencido()

    # ── Costo (RF-05) ──────────────────────────────────────────
    def costo_para_cliente(self):
        """Costo mensual aplicando el descuento Premium si corresponde."""
        if self.cliente.es_premium():
            return (self.costo_mensual * (Decimal('1') - DESCUENTO_PREMIUM)).quantize(Decimal('0.01'))
        return self.costo_mensual

    # ── Facturación ────────────────────────────────────────────
    def _dia_del_mes(self, anio, mes):
        ultimo_dia = calendar.monthrange(anio, mes)[1]
        return min(self.dia_facturacion, ultimo_dia)

    def fecha_facturacion_del_mes(self, anio, mes):
        return date(anio, mes, self._dia_del_mes(anio, mes))

    def debe_facturarse_en(self, anio, mes):
        """True si el abono activo corresponde facturarse en ese mes."""
        if not self.esta_activo():
            return False
        fecha = self.fecha_facturacion_del_mes(anio, mes)
        if fecha < self.fecha_inicio:
            return False
        if self.fecha_fin is not None and fecha > self.fecha_fin:
            return False
        if self.ultima_facturacion is not None:
            if (self.ultima_facturacion.year, self.ultima_facturacion.month) == (anio, mes):
                return False
        return True
