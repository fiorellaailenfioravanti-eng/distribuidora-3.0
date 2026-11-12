from django.core.exceptions import ValidationError
from django.test import SimpleTestCase

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
