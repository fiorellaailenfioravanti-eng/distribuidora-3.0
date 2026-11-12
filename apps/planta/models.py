"""Planta de recarga: cuántos bidones se llenaron cada día.

Una `RecargaBidones` por día (se puede corregir durante ese día). Cada
`DetalleRecarga` suma al stock del bidón lleno y descuenta del stock de su
envase vacío (`Producto.envase`); la lógica vive en `services.py`.
"""
from django.conf import settings
from django.db import models


class RecargaBidones(models.Model):
    fecha = models.DateField(unique=True, verbose_name='Fecha')
    registrada_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='recargas_registradas',
        verbose_name='Registrada por',
    )
    actualizada = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    observaciones = models.CharField(max_length=200, blank=True, verbose_name='Observaciones')

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Recarga de bidones'
        verbose_name_plural = 'Recargas de bidones'

    def __str__(self):
        return f'Recarga del {self.fecha:%d/%m/%Y}'

    def total(self):
        return sum(d.cantidad for d in self.detalles.all())

    def resumen(self):
        """«5 × 20 L primera marca · 2 × 10 L segunda marca» (sólo lo recargado)."""
        return ' · '.join(f'{d.cantidad} × {d.producto.nombre.replace("Bidón ", "")}'
                          for d in self.detalles.all() if d.cantidad)


class DetalleRecarga(models.Model):
    recarga = models.ForeignKey(RecargaBidones, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(
        'productos.Producto', on_delete=models.PROTECT, related_name='recargas',
        verbose_name='Bidón recargado',
    )
    cantidad = models.PositiveIntegerField(default=0, verbose_name='Cantidad')

    class Meta:
        ordering = ['producto__nombre']
        unique_together = [('recarga', 'producto')]
        verbose_name = 'Detalle de recarga'
        verbose_name_plural = 'Detalles de recarga'

    def __str__(self):
        return f'{self.cantidad} × {self.producto}'
