from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from apps.empleados.models import Empleado, RolEmpleado
from apps.productos.models import Producto
from .services import guardar_recarga


class RecargaTests(TestCase):
    """Recarga diaria: suma llenos, descuenta envases vacíos y se corrige por diferencia."""

    def setUp(self):
        self.envase20 = Producto.objects.create(nombre='Env 20', descripcion='', precio=Decimal('1'), stock=50, es_envase=True)
        self.envase10 = Producto.objects.create(nombre='Env 10', descripcion='', precio=Decimal('1'), stock=5, es_envase=True)
        self.b20a = Producto.objects.create(nombre='20 1ra', descripcion='', precio=Decimal('1'), stock=10,
                                            es_recargable=True, envase=self.envase20)
        self.b20b = Producto.objects.create(nombre='20 2da', descripcion='', precio=Decimal('1'), stock=0,
                                            es_recargable=True, envase=self.envase20)
        self.b10 = Producto.objects.create(nombre='10 1ra', descripcion='', precio=Decimal('1'), stock=0,
                                           es_recargable=True, envase=self.envase10)
        Usuario = get_user_model()
        self.recargador = Usuario.objects.create_user('recarga', 'r@x.com', 'Agua-Lluvia-2026')
        self.recargador._es_empleado = True
        Empleado.objects.create(usuario=self.recargador, nombre='Chico', apellido='Planta', dni='30555111',
                                rol=RolEmpleado.objects.get(nombre='Recargador'))

    def _refrescar(self):
        for p in (self.envase20, self.envase10, self.b20a, self.b20b, self.b10):
            p.refresh_from_db()

    def test_suma_llenos_y_descuenta_vacios_del_mismo_tamano(self):
        guardar_recarga(self.recargador, {self.b20a.pk: 20, self.b20b.pk: 10, self.b10.pk: 3})
        self._refrescar()
        self.assertEqual((self.b20a.stock, self.b20b.stock, self.b10.stock), (30, 10, 3))
        self.assertEqual((self.envase20.stock, self.envase10.stock), (20, 2))

    def test_corregir_mueve_solo_la_diferencia(self):
        guardar_recarga(self.recargador, {self.b20a.pk: 20})
        guardar_recarga(self.recargador, {self.b20a.pk: 15})
        self._refrescar()
        self.assertEqual((self.b20a.stock, self.envase20.stock), (25, 35))

    def test_no_alcanzan_los_envases(self):
        with self.assertRaises(ValidationError):
            guardar_recarga(self.recargador, {self.b10.pk: 6})
        self._refrescar()
        self.assertEqual((self.b10.stock, self.envase10.stock), (0, 5))

    def test_marcas_que_comparten_envase_suman_contra_el_mismo_stock(self):
        with self.assertRaises(ValidationError):
            guardar_recarga(self.recargador, {self.b20a.pk: 30, self.b20b.pk: 30})

    def test_pantalla_del_recargador(self):
        self.client.force_login(self.recargador)
        url = reverse('apps.planta:recarga_diaria')
        self.assertEqual(self.client.get(url).status_code, 200)
        respuesta = self.client.post(url, {f'cantidad_{self.b20a.pk}': '4', f'cantidad_{self.b20b.pk}': '',
                                           f'cantidad_{self.b10.pk}': '0'})
        self.assertRedirects(respuesta, url)
        self._refrescar()
        self.assertEqual(self.b20a.stock, 14)

    def test_recargador_no_ve_el_panel_ni_el_stock(self):
        self.client.force_login(self.recargador)
        self.assertEqual(self.client.get(reverse('dashboard')).status_code, 302)
        self.assertEqual(self.client.get(reverse('apps.planta:stock_bidones')).status_code, 302)

    def test_admin_ve_el_stock_y_puede_recargar(self):
        admin = get_user_model().objects.create_superuser('root', 'root@x.com', 'Agua-Lluvia-2026')
        self.client.force_login(admin)
        self.assertEqual(self.client.get(reverse('apps.planta:stock_bidones')).status_code, 200)
        self.assertEqual(self.client.get(reverse('apps.planta:recarga_diaria')).status_code, 200)
