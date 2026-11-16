from decimal import Decimal

from django.core.exceptions import ValidationError
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from apps.logistica.models import Zona
from apps.productos.models import Producto

from . import validadores as v


class ValidadoresTests(SimpleTestCase):
    def test_dni(self):
        self.assertEqual(v.validar_dni('30.123.456'), '30123456')
        self.assertEqual(v.validar_dni('1234567'), '1234567')
        for malo in ('abc12345', '123', '123456789'):
            with self.assertRaises(ValidationError):
                v.validar_dni(malo)

    def test_telefono(self):
        self.assertEqual(v.validar_telefono('(362) 412-3456'), '(362) 412-3456')
        for malo in ('llamame', '123'):
            with self.assertRaises(ValidationError):
                v.validar_telefono(malo)

    def test_coordenadas_altura_patente(self):
        self.assertEqual(v.validar_coordenadas(' -27.45 , -58.98 '), '-27.45,-58.98')
        self.assertEqual(v.validar_altura('s/n'), 'S/N')
        self.assertEqual(v.normalizar_patente('ab 123 cd'), 'AB123CD')
        for funcion, malo in ((v.validar_coordenadas, '999,1'), (v.validar_coordenadas, 'plaza'),
                              (v.validar_altura, '-5'), (v.normalizar_patente, '12ABC')):
            with self.assertRaises(ValidationError):
                funcion(malo)


class InicioTests(TestCase):
    """Portada de la tienda: destacados con stock, sin envases, y días de reparto."""

    def test_muestra_destacados_y_zonas(self):
        Producto.objects.create(nombre='Bidón 20 L', descripcion='x', precio=Decimal('1500'), stock=10)
        Producto.objects.create(nombre='Bidón agotado', descripcion='x', precio=Decimal('1500'), stock=0)
        Producto.objects.create(nombre='Envase vacío', descripcion='x', precio=Decimal('900'), stock=10, es_envase=True)
        Zona.objects.create(nombre='Norte', dias_reparto='1,4')
        respuesta = self.client.get(reverse('inicio'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'Bidón 20 L')
        self.assertNotContains(respuesta, 'Bidón agotado')
        self.assertNotContains(respuesta, 'Envase vacío')
        self.assertContains(respuesta, 'Martes, Viernes')
        self.assertNotContains(respuesta, '/media/perfiles/')

    def test_sin_datos_no_falla(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'Pureza en cada gota')
