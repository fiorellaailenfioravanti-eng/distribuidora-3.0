from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse

from .models import Cliente


class BuscarClientesTests(TestCase):
    """H-22: la búsqueda no rompe con clientes sin cuenta y tolera tildes."""

    def setUp(self):
        Usuario = get_user_model()
        self.vendedor = Usuario.objects.create_user('vend', 'v@x.com', 'Agua-Lluvia-2026')
        self.vendedor.groups.add(Group.objects.get(name='Vendedor'))
        self.sin_cuenta = Cliente.objects.create(nombre='Ramón', apellido='Gutiérrez', dni='20111222')
        self.client.force_login(self.vendedor)

    def _buscar(self, q):
        respuesta = self.client.get(reverse('apps.clientes:listar_clientes'), {'q': q})
        self.assertEqual(respuesta.status_code, 200)
        return list(respuesta.context['clientes'])

    def test_encuentra_cliente_sin_cuenta_por_nombre_sin_tildes(self):
        self.assertIn(self.sin_cuenta, self._buscar('ramon gutierrez'))

    def test_encuentra_por_dni(self):
        self.assertIn(self.sin_cuenta, self._buscar('20111222'))

    def test_encuentra_cliente_con_cuenta_por_usuario(self):
        cliente_web = self.vendedor.perfil_cliente
        self.assertIn(cliente_web, self._buscar('vend'))


class AgregarDireccionTests(TestCase):
    def test_cliente_con_direccion_puede_agregar_otra_sin_500(self):
        """Antes daba NameError (`reverse` sin importar); con A-D4 muestra el formulario."""
        from .models import DireccionEntrega
        Usuario = get_user_model()
        vendedor = Usuario.objects.create_user('vend', 'v@x.com', 'Agua-Lluvia-2026')
        vendedor.groups.add(Group.objects.get(name='Vendedor'))
        cliente = Cliente.objects.create(nombre='Ana', apellido='Paz')
        direccion = DireccionEntrega.objects.create(cliente=cliente, calle='Mitre', altura='10')
        self.client.force_login(vendedor)
        respuesta = self.client.get(reverse('apps.clientes:agregar_direccion', args=[cliente.pk]))
        self.assertEqual(respuesta.status_code, 200)
        self.assertFalse(respuesta.context['form'].initial['es_principal'])


class VariasDireccionesTests(TestCase):
    """RF-03 (decisión A-D4): un cliente puede tener varias direcciones."""

    def setUp(self):
        Usuario = get_user_model()
        self.usuario = Usuario.objects.create_user('ana', 'ana@x.com', 'Agua-Lluvia-2026')
        self.cliente = self.usuario.perfil_cliente
        self.client.force_login(self.usuario)
        self.url = reverse('apps.clientes:agregar_direccion', args=[self.cliente.pk])
        from apps.logistica.models import Barrio, Zona
        self.barrio = Barrio.objects.create(nombre='Centro', ciudad='Resistencia',
                                            zona=Zona.objects.create(nombre='Centro', dias_reparto='0'))

    def _agregar(self, calle, url=None, **extra):
        return self.client.post(url or self.url, {'calle': calle, 'altura': '100', 'ciudad': 'Resistencia',
                                                  'barrio': self.barrio.pk, **extra})

    def test_agrega_una_segunda_direccion(self):
        self._agregar('Mitre')
        self._agregar('Belgrano')
        self.assertEqual(self.cliente.direcciones.count(), 2)

    def test_la_primera_es_principal_y_la_segunda_solo_si_se_marca(self):
        self._agregar('Mitre')
        self._agregar('Belgrano')
        self.assertEqual(self.cliente.direcciones.get(es_principal=True).calle, 'Mitre')
        self._agregar('Urquiza', es_principal='on')
        self.assertEqual(self.cliente.direcciones.get(es_principal=True).calle, 'Urquiza')

    def test_next_externo_se_ignora(self):
        respuesta = self._agregar('Mitre', url=self.url + '?next=https://sitio-malicioso.example/')
        self.assertEqual(respuesta.status_code, 302)
        self.assertNotIn('sitio-malicioso', respuesta.url)


class FiadoPremiumYExcepcionTests(TestCase):
    """RF-05 (decisión A-D6): Premium siempre; Normal sólo como excepción manual."""

    def test_bajar_de_premium_quita_el_fiado(self):
        cliente = Cliente.objects.create(nombre='Ex', apellido='Premium', tipo_cliente='Premium')
        cliente.tipo_cliente = 'Normal'
        cliente.save()
        self.assertFalse(cliente.permite_fiado)

    def test_excepcion_manual_se_conserva(self):
        cliente = Cliente.objects.create(nombre='Nor', apellido='Mal')
        cliente.permite_fiado = True
        cliente.save()
        cliente.notas_internas = 'cliente de confianza'
        cliente.save()
        cliente.refresh_from_db()
        self.assertTrue(cliente.permite_fiado)


class HistorialBidonesTests(TestCase):
    """RF-08: historial de envases y saldo derivado."""

    def setUp(self):
        from datetime import date
        from apps.logistica.models import DetalleHojaRuta, HojaRuta
        self.cliente = Cliente.objects.create(nombre='Ana', apellido='Paz')
        hoja = HojaRuta.objects.create(fecha=date(2026, 10, 20))
        self.parada = DetalleHojaRuta.objects.create(hoja_ruta=hoja, cliente=self.cliente, orden=1, cantidad_bidones=3)

    def test_entrega_registra_prestamo_y_devolucion_sin_duplicar(self):
        from apps.logistica.services import registrar_entrega
        registrar_entrega(self.parada, 'Entregado', envases_retirados=2)
        registrar_entrega(self.parada, 'Entregado', envases_retirados=2)
        self.cliente.refresh_from_db()
        self.assertEqual(self.cliente.bidones_prestados, 1)
        self.assertEqual(self.cliente.movimientos_bidon.count(), 2)

    def test_devolucion_manual_no_deja_saldo_negativo(self):
        from django.core.exceptions import ValidationError
        from .services import registrar_movimiento_bidon
        registrar_movimiento_bidon(self.cliente, 'Prestamo', 2)
        with self.assertRaises(ValidationError):
            registrar_movimiento_bidon(self.cliente, 'Devolucion', 3)
        registrar_movimiento_bidon(self.cliente, 'Ajuste', -1, nota='Conteo físico')
        self.cliente.refresh_from_db()
        self.assertEqual(self.cliente.bidones_prestados, 1)
