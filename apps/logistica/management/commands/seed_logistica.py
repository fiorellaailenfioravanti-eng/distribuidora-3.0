from decimal import Decimal

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from django.db import transaction

from apps.clientes.models import Cliente, DireccionEntrega
from apps.empleados.models import Empleado, RolEmpleado
from apps.logistica.models import Barrio, Camion, Zona
from apps.pedidos.models import DetallePedido, MetodoPago, Pedido
from apps.productos.models import Categoria, Producto

User = get_user_model()


class Command(BaseCommand):
    help = 'Seed de demostración para logística (zonas, camiones, repartidor, envases, clientes frecuentes, pedido agendable). Idempotente.'

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Iniciando seed_logistica...'))

        Group.objects.get_or_create(name='Vendedor')
        g_repartidor, _ = Group.objects.get_or_create(name='Repartidor')

        u_rep, _ = User.objects.get_or_create(
            username='repartidor.demo',
            defaults={
                'first_name': 'Repartidor',
                'last_name': 'Demo',
                'email': 'repartidor.demo@distribuidora.local',
                'is_active': True,
            },
        )
        if not u_rep.has_usable_password():
            u_rep.set_password('demo123')
            u_rep.save()
        u_rep.groups.add(g_repartidor)

        rol_rep, _ = RolEmpleado.objects.get_or_create(
            nombre='Repartidor',
            defaults={'descripcion': 'Repartidor de entregas', 'grupo_permisos': 'Repartidor'},
        )
        if rol_rep.grupo_permisos != 'Repartidor':
            rol_rep.grupo_permisos = 'Repartidor'
            rol_rep.save(update_fields=['grupo_permisos'])

        Empleado.objects.get_or_create(
            usuario=u_rep,
            defaults={
                'nombre': 'Repartidor',
                'apellido': 'Demo',
                'dni': '12345678',
                'celular': '+5491144444444',
                'email': 'repartidor.demo@distribuidora.local',
                'rol': rol_rep,
                'activo': True,
            },
        )

        zona_norte, _ = Zona.objects.get_or_create(
            nombre='Norte',
            defaults={'dias_reparto': ['Lunes', 'Miércoles', 'Viernes']},
        )
        Zona.objects.get_or_create(
            nombre='Sur',
            defaults={'dias_reparto': ['Martes', 'Jueves']},
        )

        Camion.objects.get_or_create(
            patente='ABC123',
            defaults={
                'marca': 'Iveco',
                'modelo': 'Daily',
                'capacidad_kg': Decimal('2000.00'),
                'capacidad_botellones': 500,
                'activo': True,
            },
        )
        Camion.objects.get_or_create(
            patente='DEF456',
            defaults={
                'marca': 'Mercedes',
                'modelo': 'Sprinter',
                'capacidad_kg': Decimal('1500.00'),
                'capacidad_botellones': 400,
                'activo': True,
            },
        )

        cat_gaseosas, _ = Categoria.objects.get_or_create(nombre='Gaseosas')
        cat_envases, _ = Categoria.objects.get_or_create(nombre='Envases')

        prod_soda, _ = Producto.objects.get_or_create(
            nombre='Soda 2L',
            defaults={
                'descripcion': 'Botella retornable 2L',
                'precio': Decimal('800.00'),
                'stock': 1000,
                'es_retornable': True,
                'es_envase': False,
            },
        )
        if cat_gaseosas not in prod_soda.categoria.all():
            prod_soda.categoria.add(cat_gaseosas)

        prod_agua, _ = Producto.objects.get_or_create(
            nombre='Agua 2L',
            defaults={
                'descripcion': 'Botella retornable 2L',
                'precio': Decimal('700.00'),
                'stock': 1000,
                'es_retornable': True,
                'es_envase': False,
            },
        )
        if cat_gaseosas not in prod_agua.categoria.all():
            prod_agua.categoria.add(cat_gaseosas)

        envase_2l, _ = Producto.objects.get_or_create(
            nombre='Envase 2L',
            defaults={
                'descripcion': 'Envase retornable',
                'precio': Decimal('0.00'),
                'stock': 1000,
                'es_retornable': True,
                'es_envase': True,
            },
        )
        if cat_envases not in envase_2l.categoria.all():
            envase_2l.categoria.add(cat_envases)

        cli_frecuente, _ = Cliente.objects.get_or_create(
            email_contacto='cliente.frecuente@demo.local',
            defaults={
                'nombre': 'Cliente',
                'apellido': 'Frecuente',
                'tipo_registro': 'WEB',
                'es_frecuente': True,
                'cantidad_recurrente_default': 2,
            },
        )

        barrio_norte, _ = Barrio.objects.get_or_create(nombre='Norte', defaults={'zona': zona_norte})

        dir_frec, _ = DireccionEntrega.objects.get_or_create(
            cliente=cli_frecuente,
            calle='Av. Demo 123',
            defaults={
                'ciudad': 'Buenos Aires',
                'barrio': barrio_norte,
            },
        )

        mp_efectivo, _ = MetodoPago.objects.get_or_create(
            nombre='Efectivo en Entrega',
            defaults={'descripcion': 'Pago en efectivo al recibir el pedido'},
        )

        pedido, created_p = Pedido.objects.get_or_create(
            cliente=cli_frecuente,
            estado='Pendiente',
            origen='WEB',
            defaults={
                'direccion_entrega': dir_frec,
                'metodo_pago': mp_efectivo,
                'total': Decimal('1600.00'),
                'notas_cliente': 'Pedido demo logística',
            },
        )
        if created_p or not pedido.detalles.exists():
            DetallePedido.objects.get_or_create(
                pedido=pedido,
                producto=prod_soda,
                defaults={'cantidad': 2, 'precio_unitario': prod_soda.precio, 'subtotal': prod_soda.precio * 2},
            )
            if hasattr(pedido, 'recalcular_total'):
                pedido.recalcular_total()
                pedido.save()

        self.stdout.write(
            self.style.SUCCESS(
                f'Seed completado: zonas={Zona.objects.count()}, camiones={Camion.objects.count()}, '
                f'empleados={Empleado.objects.count()}, clientes={Cliente.objects.count()}, '
                f'pedidos={Pedido.objects.count()}, productos={Producto.objects.count()}'
            )
        )
