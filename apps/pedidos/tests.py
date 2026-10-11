from django.test import TestCase

from apps.clientes.models import Cliente, DireccionEntrega
from apps.logistica.models import Barrio, Zona

from .forms import _etiqueta_direccion_con_fecha


class CheckoutFechaEstimadaTests(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nombre='Ana', apellido='Pérez')

    def test_etiqueta_incluye_fecha_estimada(self):
        zona = Zona.objects.create(nombre='Centro', dias_reparto='0,1,2,3,4,5,6')
        barrio = Barrio.objects.create(nombre='Centro', zona=zona)
        direccion = DireccionEntrega.objects.create(
            cliente=self.cliente, calle='Mitre', altura='100', barrio=barrio
        )
        etiqueta = _etiqueta_direccion_con_fecha(direccion)
        self.assertIn('entrega estimada', etiqueta)

    def test_etiqueta_sin_zona_no_agrega_fecha(self):
        barrio = Barrio.objects.create(nombre='Sin Zona')
        direccion = DireccionEntrega.objects.create(
            cliente=self.cliente, calle='Urquiza', altura='200', barrio=barrio
        )
        etiqueta = _etiqueta_direccion_con_fecha(direccion)
        self.assertNotIn('entrega estimada', etiqueta)
