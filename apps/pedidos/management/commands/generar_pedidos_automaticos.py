"""
Genera los pedidos de reposición automática que vencen hoy (RF-18).

Correr una vez por día (Task Scheduler / cron), antes de planificar el reparto:

    python manage.py generar_pedidos_automaticos --settings=distribuidora.settings.local
"""
from django.core.management.base import BaseCommand

from apps.pedidos.services import generar_pedidos_automaticos


class Command(BaseCommand):
    help = 'Crea el pedido de cada suscripción de reposición cuya fecha llegó. Idempotente.'

    def handle(self, *args, **options):
        pedidos = generar_pedidos_automaticos()
        for pedido in pedidos:
            self.stdout.write(f'  Pedido #{pedido.pk} · {pedido.cliente.nombre_completo()} · ${pedido.total}')
        self.stdout.write(self.style.SUCCESS(f'{len(pedidos)} pedidos automáticos generados.'))
