from decimal import Decimal

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from apps.clientes.models import Cliente


# ────────────────────────────────────────────────
# TIPOS DE MOVIMIENTO
# ────────────────────────────────────────────────
TIPOS_MOVIMIENTO = [
    ('Cargo', 'Cargo (deuda)'),
    ('Pago',  'Pago / Abono'),
]


# ────────────────────────────────────────────────
# SEMAFORIZACIÓN DE MOROSIDAD — RF-14
#    🟡 al inicio del mes · 🟠 a los 10 días · 🔴 a los 15 días
# ────────────────────────────────────────────────
DIAS_NARANJA = 10
DIAS_ROJO    = 15

NIVELES_MOROSIDAD = {
    'al-dia': {
        'etiqueta': 'Al día',
        'clase':    'success',
        'color':    '#16a34a',
        'icono':    'fa-circle-check',
    },
    'amarillo': {
        'etiqueta': 'En plazo',
        'clase':    'warning',
        'color':    '#d97706',
        'icono':    'fa-circle',
    },
    'naranja': {
        'etiqueta': 'Atrasado (10 días)',
        'clase':    'warning',
        'color':    '#ea580c',
        'icono':    'fa-triangle-exclamation',
    },
    'rojo': {
        'etiqueta': 'Moroso (15 días)',
        'clase':    'danger',
        'color':    '#dc2626',
        'icono':    'fa-circle-exclamation',
    },
}


# ────────────────────────────────────────────────
# 1. CUENTA CORRIENTE  — RF-14
#    Cada cliente tiene una única cuenta con su saldo de fiado.
# ────────────────────────────────────────────────
class CuentaCorriente(models.Model):
    id_cuenta      = models.AutoField(primary_key=True)
    cliente        = models.OneToOneField(
        Cliente,
        on_delete=models.CASCADE,
        related_name='cuenta_corriente',
        verbose_name='Cliente'
    )
    saldo          = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name='Saldo',
        help_text='Positivo = el cliente debe; negativo = saldo a favor.'
    )
    limite_credito = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name='Límite de crédito',
        help_text='0 = sin límite definido.'
    )
    activa         = models.BooleanField(default=True, verbose_name='Activa')
    fecha_apertura = models.DateField(auto_now_add=True, verbose_name='Fecha de apertura')

    class Meta:
        verbose_name        = 'Cuenta corriente'
        verbose_name_plural = 'Cuentas corrientes'

    def __str__(self):
        return f"Cuenta de {self.cliente.nombre_completo()} (${self.saldo})"

    # ── Cálculos ───────────────────────────────────────────────
    def total_cargos(self):
        return self.movimientos.filter(tipo='Cargo').aggregate(
            t=models.Sum('monto')
        )['t'] or Decimal('0.00')

    def total_pagos(self):
        return self.movimientos.filter(tipo='Pago').aggregate(
            t=models.Sum('monto')
        )['t'] or Decimal('0.00')

    def calcular_saldo(self):
        return self.total_cargos() - self.total_pagos()

    def recalcular_saldo(self):
        self.saldo = self.calcular_saldo()
        self.save(update_fields=['saldo'])
        return self.saldo

    def permite_fiado(self):
        """RF-05: solo los clientes habilitados pueden tener deuda."""
        return self.cliente.permite_fiado

    # ── Semaforización (RF-14) ─────────────────────────────────
    def dias_de_atraso(self):
        """Días transcurridos desde el cargo más antiguo con saldo pendiente."""
        primer = self.movimientos.filter(tipo='Cargo').order_by('fecha').first()
        if primer is None:
            return 0
        fecha_cargo = timezone.localtime(primer.fecha).date()
        return (timezone.localdate() - fecha_cargo).days

    def nivel_morosidad(self):
        """Clave del semáforo: 'al-dia' | 'amarillo' | 'naranja' | 'rojo'."""
        if self.saldo <= 0:
            return 'al-dia'
        dias = self.dias_de_atraso()
        if dias >= DIAS_ROJO:
            return 'rojo'
        if dias >= DIAS_NARANJA:
            return 'naranja'
        return 'amarillo'

    def estado_morosidad(self):
        """Diccionario con etiqueta, clase Bootstrap, color e ícono del semáforo."""
        return NIVELES_MOROSIDAD[self.nivel_morosidad()]

    def tiene_deuda(self):
        return self.saldo > 0

    def excede_limite(self, monto_adicional=Decimal('0.00')):
        if not self.limite_credito:
            return False
        return (self.saldo + Decimal(monto_adicional)) > self.limite_credito


# ────────────────────────────────────────────────
# 2. MOVIMIENTO DE CUENTA  — RF-14
#    Cargo (deuda) o Pago. Puede originarse en un pedido o en un abono.
# ────────────────────────────────────────────────
class MovimientoCuenta(models.Model):
    id_movimiento  = models.AutoField(primary_key=True)
    cuenta         = models.ForeignKey(
        CuentaCorriente,
        on_delete=models.CASCADE,
        related_name='movimientos',
        verbose_name='Cuenta'
    )
    tipo           = models.CharField(
        max_length=10,
        choices=TIPOS_MOVIMIENTO,
        verbose_name='Tipo'
    )
    monto          = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Monto')
    descripcion    = models.CharField(max_length=200, blank=True, verbose_name='Descripción')
    fecha          = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    fecha_vencimiento = models.DateField(
        null=True,
        blank=True,
        verbose_name='Fecha de vencimiento',
        help_text='Fecha a partir de la cual el cargo se considera vencido.'
    )
    pedido         = models.ForeignKey(
        'pedidos.Pedido',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='movimientos_cuenta',
        verbose_name='Pedido'
    )
    abono          = models.ForeignKey(
        'abonos.Abono',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='movimientos_cuenta',
        verbose_name='Abono'
    )

    class Meta:
        ordering            = ['-fecha']
        verbose_name        = 'Movimiento de cuenta'
        verbose_name_plural = 'Movimientos de cuenta'

    def __str__(self):
        signo = '+' if self.tipo == 'Cargo' else '-'
        return f"{signo}${self.monto} ({self.cuenta.cliente.nombre_completo()})"

    def clean(self):
        # RF-05: un cargo a cuenta corriente exige fiado habilitado.
        if self.tipo == 'Cargo' and self.cuenta_id:
            if not self.cuenta.cliente.permite_fiado:
                raise ValidationError({
                    'tipo': 'El cliente no tiene fiado habilitado (RF-05). '
                            'Cambialo a Premium o activá "permite fiado".'
                })

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.cuenta.recalcular_saldo()

    def delete(self, *args, **kwargs):
        cuenta = self.cuenta
        super().delete(*args, **kwargs)
        cuenta.recalcular_saldo()
