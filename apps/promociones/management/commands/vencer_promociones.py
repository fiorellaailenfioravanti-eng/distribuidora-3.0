"""
Vence los packs prepagos cuya fecha de caducidad ya pasó (RF-10).

Correr una vez por día (Task Scheduler / cron), junto a `generar_cargos_abonos`:

    python manage.py vencer_promociones --settings=distribuidora.settings.local
"""
from django.core.management.base import BaseCommand

from apps.promociones.services import vencer_promociones


class Command(BaseCommand):
    help = 'Marca como vencidos (saldo 0) los packs prepagos con más de 30 días corridos. Idempotente.'

    def handle(self, *args, **options):
        vencidas = vencer_promociones()
        self.stdout.write(self.style.SUCCESS(f'{vencidas} compras de promoción vencidas.'))
