from unittest import mock

from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase
from django.urls import reverse

from .models import ConfiguracionCorreo


class ConfiguracionCorreoTests(TestCase):
    """El administrador elige la cuenta que envía el correo de recuperación."""

    def setUp(self):
        Usuario = get_user_model()
        self.admin = Usuario.objects.create_superuser('jefe', 'jefe@x.com', 'Agua-Lluvia-2026')
        self.cliente = Usuario.objects.create_user('ana', 'ana@x.com', 'Agua-Lluvia-2026')

    def _guardar(self, **datos):
        base = {'activo': 'on', 'nombre_remitente': 'Agua de Lluvia', 'correo_remitente': 'envios@x.com',
                'servidor': 'smtp.x.com', 'puerto': 587, 'usar_tls': 'on', 'usuario': '', 'clave': 'abcd efgh ijkl mnop'}
        base.update(datos)
        return self.client.post(reverse('apps.configuracion:configuracion'), base)

    def test_solo_el_admin_entra(self):
        self.client.force_login(self.cliente)
        respuesta = self.client.get(reverse('apps.configuracion:configuracion'))
        self.assertNotEqual(respuesta.status_code, 200)

    def test_guardar_y_conservar_la_clave(self):
        self.client.force_login(self.admin)
        self._guardar()
        cfg = ConfiguracionCorreo.actual()
        self.assertEqual(cfg.clave, 'abcdefghijklmnop')  # sin espacios
        self._guardar(clave='', nombre_remitente='Aguadelluvia')
        cfg.refresh_from_db()
        self.assertEqual(cfg.clave, 'abcdefghijklmnop')  # vacía = no se pisa
        self.assertTrue(cfg.lista())

    def test_activar_sin_clave_se_rechaza(self):
        self.client.force_login(self.admin)
        self._guardar(clave='')
        self.assertFalse(ConfiguracionCorreo.actual().lista())

    def test_recuperacion_usa_la_cuenta_configurada(self):
        self.client.force_login(self.admin)
        self._guardar()
        self.client.logout()
        original = mail.get_connection
        pedidos = []

        def conexion_de_prueba(backend=None, **opciones):
            # La conexión SMTP configurada se reemplaza por la de memoria para el test
            pedidos.append((backend, opciones))
            return original('django.core.mail.backends.locmem.EmailBackend')

        with mock.patch('django.core.mail.get_connection', side_effect=conexion_de_prueba):
            self.client.post(reverse('apps.autenticacion:recuperar'), {'email': 'ana@x.com'})
        self.assertEqual(pedidos[0][1]['host'], 'smtp.x.com')
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].from_email, 'Agua de Lluvia <envios@x.com>')

    def test_prueba_sin_email_del_admin_va_a_la_cuenta_que_envia(self):
        self.client.force_login(self.admin)
        self._guardar()
        self.admin.email = ''
        self.admin.save()
        original = mail.get_connection
        with mock.patch('django.core.mail.get_connection',
                        side_effect=lambda backend=None, **o: original('django.core.mail.backends.locmem.EmailBackend')):
            self.client.post(reverse('apps.configuracion:probar_correo'))
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, ['envios@x.com'])
