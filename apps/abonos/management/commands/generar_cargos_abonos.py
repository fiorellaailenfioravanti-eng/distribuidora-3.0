from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.abonos.services import generar_cargos_mensuales


class Command(BaseCommand):
    help = 'Genera los cargos mensuales de los abonos activos en las cuentas corrientes.'

    def add_arguments(self, parser):
        parser.add_argument('--anio', type=int, default=None, help='Año a facturar (por defecto, el actual).')
        parser.add_argument('--mes', type=int, default=None, help='Mes a facturar 1-12 (por defecto, el actual).')

    def handle(self, *args, **options):
        hoy = timezone.localdate()
        anio = options['anio'] or hoy.year
        mes = options['mes'] or hoy.month

        generados, omitidos = generar_cargos_mensuales(anio=anio, mes=mes)

        self.stdout.write(self.style.SUCCESS(
            f'Facturación {mes:02d}/{anio}: {len(generados)} cargo(s) generado(s).'
        ))
        for abono in generados:
            self.stdout.write(
                f"  + Abono #{abono.id_abono} — {abono.cliente.nombre_completo()} "
                f"(${abono.costo_para_cliente()})"
            )
        if omitidos:
            self.stdout.write(self.style.WARNING(
                f'  {len(omitidos)} abono(s) omitido(s) por falta de fiado (RF-05):'
            ))
            for abono in omitidos:
                self.stdout.write(f"  - Abono #{abono.id_abono} — {abono.cliente.nombre_completo()}")
