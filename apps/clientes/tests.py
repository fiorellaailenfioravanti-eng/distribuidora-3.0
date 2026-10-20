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
    def test_cliente_con_direccion_redirige_a_editar_sin_500(self):
        """`reverse` no estaba importado: la vista daba NameError."""
        from .models import DireccionEntrega
        Usuario = get_user_model()
        vendedor = Usuario.objects.create_user('vend', 'v@x.com', 'Agua-Lluvia-2026')
        vendedor.groups.add(Group.objects.get(name='Vendedor'))
        cliente = Cliente.objects.create(nombre='Ana', apellido='Paz')
        direccion = DireccionEntrega.objects.create(cliente=cliente, calle='Mitre', altura='10')
        self.client.force_login(vendedor)
        respuesta = self.client.get(reverse('apps.clientes:agregar_direccion', args=[cliente.pk]))
        self.assertEqual(respuesta.status_code, 302)
        self.assertIn(reverse('apps.clientes:editar_direccion', args=[direccion.pk]), respuesta.url)
