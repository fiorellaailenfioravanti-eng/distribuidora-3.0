"""
Genera los borradores de hojas de ruta de los próximos días (RF-17, A-D5).

Pensado para correr cada 15 días (Task Scheduler / cron):

    python manage.py generar_borradores_reparto --settings=distribuidora.settings.local
    python manage.py generar_borradores_reparto --desde 2026-11-01 --dias 15

Las hojas quedan en Borrador: el administrador las revisa, agrega clientes
frecuentes si corresponde y las confirma (decisión D2).
"""
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError

from apps.logistica.services import generar_borradores_periodo


class Command(BaseCommand):
    help = 'Crea borradores de hojas de ruta por zona para los próximos días (default 15). Idempotente.'

    def add_arguments(self, parser):
        parser.add_argument('--desde', help='Fecha inicial AAAA-MM-DD (default: hoy).')
        parser.add_argument('--dias', type=int, default=15, help='Cantidad de días del período (default: 15).')

    def handle(self, *args, **options):
        desde = None
        if options['desde']:
            try:
                desde = datetime.strptime(options['desde'], '%Y-%m-%d').date()
            except ValueError:
                raise CommandError('La fecha debe tener el formato AAAA-MM-DD.')
        if options['dias'] < 1:
            raise CommandError('--dias debe ser al menos 1.')

        hojas = generar_borradores_periodo(desde=desde, dias=options['dias'])
        for hoja in hojas:
            self.stdout.write(f'  Hoja #{hoja.id_ruta} · {hoja.fecha:%d/%m/%Y} · {hoja.zona} · {hoja.total_paradas()} paradas')
        self.stdout.write(self.style.SUCCESS(f'{len(hojas)} borradores creados.'))
