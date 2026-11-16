import re
from datetime import timedelta

from django.core import mail
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from . import recuperacion
from .forms import RegistroUsuarioForm
from .models import CodigoRecuperacion


class SesionTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user('ana', 'ana@x.com', 'Agua-Lluvia-2026')

    def test_cerrar_sesion_por_get_no_desloguea(self):
        """H-31: un simple enlace no puede cerrar la sesión."""
        self.client.force_login(self.usuario)
        self.client.get(reverse('apps.autenticacion:cerrar_sesion'))
        self.assertIn('_auth_user_id', self.client.session)
        self.client.post(reverse('apps.autenticacion:cerrar_sesion'))
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_ingresar_respeta_next_interno(self):
        """H-37: después del login vuelve a la página pedida."""
        destino = reverse('apps.carrito:ver_carrito')
        respuesta = self.client.post(
            reverse('apps.autenticacion:ingresar') + f'?next={destino}',
            {'username': 'ana', 'password': 'Agua-Lluvia-2026'},
        )
        self.assertEqual(respuesta.url, destino)

    def test_ingresar_ignora_next_externo(self):
        respuesta = self.client.post(
            reverse('apps.autenticacion:ingresar') + '?next=https://sitio-malicioso.example/',
            {'username': 'ana', 'password': 'Agua-Lluvia-2026'},
        )
        self.assertEqual(respuesta.url, reverse('inicio'))


class RegistroTelefonosTests(TestCase):
    """El registro exige un celular y permite sumar otros (cada uno con su relación)."""

    url = None

    def setUp(self):
        from apps.logistica.models import Barrio
        self.url = reverse('apps.autenticacion:registrar')
        barrio = Barrio.objects.create(nombre='Villa Centenario', ciudad='Resistencia')
        self.datos = {
            'first_name': 'Nora', 'last_name': 'Paz',
            'dir-calle': 'Av. Sarmiento', 'dir-altura': '450', 'dir-piso_depto': '',
            'dir-barrio': barrio.pk, 'dir-ciudad': 'Resistencia',
            'username': 'nuevo', 'email': 'nuevo@x.com',
            'password1': 'Agua-Lluvia-2026', 'password2': 'Agua-Lluvia-2026',
            'telefono_numero[]': ['3624111111', '3624222222'],
            'telefono_relacion[]': ['Titular', 'Esposa'],
        }

    def test_registro_sin_celulares_se_rechaza(self):
        datos = {k: v for k, v in self.datos.items() if not k.startswith('telefono_')}
        self.client.post(self.url, datos)
        self.assertFalse(get_user_model().objects.filter(username='nuevo').exists())

    def test_celulares_iguales_se_rechazan(self):
        self.client.post(self.url, {**self.datos, 'telefono_numero[]': ['3624111111', '3624 111111']})
        self.assertFalse(get_user_model().objects.filter(username='nuevo').exists())

    def test_registro_crea_dos_telefonos_con_la_relacion_declarada(self):
        self.client.post(self.url, self.datos)
        usuario = get_user_model().objects.get(username='nuevo')
        relaciones = set(usuario.perfil_cliente.telefonos.values_list('desc_relacion', flat=True))
        self.assertEqual(relaciones, {'Titular', 'Esposa'})

    def test_alcanza_con_un_solo_celular(self):
        self.client.post(self.url, {**self.datos, 'telefono_numero[]': ['3624111111'],
                                    'telefono_relacion[]': ['Titular']})
        cliente = get_user_model().objects.get(username='nuevo').perfil_cliente
        telefono = cliente.telefonos.get()
        self.assertTrue(telefono.es_principal)

    def test_puede_cargar_varios_telefonos(self):
        numeros = ['3624111111', '3624222222', '3624333333', '3624444444']
        self.client.post(self.url, {**self.datos, 'telefono_numero[]': numeros,
                                    'telefono_relacion[]': ['Titular', 'Esposa', 'Hija', 'Trabajo']})
        cliente = get_user_model().objects.get(username='nuevo').perfil_cliente
        self.assertEqual(cliente.telefonos.count(), 4)

    def test_registro_guarda_nombre_y_domicilio_principal(self):
        self.client.post(self.url, self.datos)
        cliente = get_user_model().objects.get(username='nuevo').perfil_cliente
        self.assertEqual(cliente.nombre_completo(), 'Nora Paz')
        direccion = cliente.direcciones.get()
        self.assertTrue(direccion.es_principal)
        self.assertEqual((direccion.calle, direccion.altura), ('Av. Sarmiento', '450'))

    def test_registro_sin_domicilio_se_rechaza(self):
        datos = {k: v for k, v in self.datos.items() if not k.startswith('dir-')}
        self.client.post(self.url, datos)
        self.assertFalse(get_user_model().objects.filter(username='nuevo').exists())


class RecuperarContrasenaTests(TestCase):
    """«Olvidé mi contraseña»: código temporal por email y nueva contraseña."""

    def setUp(self):
        self.usuario = get_user_model().objects.create_user('ana', 'ana@x.com', 'Agua-Lluvia-2026')
        self.url = reverse('apps.autenticacion:recuperar')
        self.url_codigo = reverse('apps.autenticacion:recuperar_codigo')

    def _pedir(self, email='ana@x.com'):
        return self.client.post(self.url, {'email': email})

    def _codigo_del_correo(self, indice=-1):
        return re.search(r'Tu código es: (\d{6})', mail.outbox[indice].body).group(1)

    def test_flujo_completo(self):
        respuesta = self._pedir('ANA@x.com')
        self.assertRedirects(respuesta, self.url_codigo)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, ['ana@x.com'])
        self.assertTrue(mail.outbox[0].alternatives)  # versión HTML
        codigo = self._codigo_del_correo()
        respuesta = self.client.post(self.url_codigo, {'codigo': f'{codigo[:3]} {codigo[3:]}'})
        self.assertRedirects(respuesta, reverse('apps.autenticacion:recuperar_nueva'))
        respuesta = self.client.post(reverse('apps.autenticacion:recuperar_nueva'),
                                     {'new_password1': 'Otra-Clave-2026x', 'new_password2': 'Otra-Clave-2026x'})
        self.assertRedirects(respuesta, reverse('apps.autenticacion:recuperar_listo'))
        self.usuario.refresh_from_db()
        self.assertTrue(self.usuario.check_password('Otra-Clave-2026x'))
        self.assertIn('se cambió', mail.outbox[-1].subject)  # aviso de cambio
        # El código no se puede volver a usar.
        self.assertFalse(CodigoRecuperacion.objects.filter(usado=False).exists())

    def test_el_codigo_no_se_guarda_en_claro(self):
        self._pedir()
        codigo = self._codigo_del_correo()
        self.assertNotIn(codigo, CodigoRecuperacion.objects.get().codigo_hash)

    def test_email_desconocido_no_revela_nada(self):
        respuesta = self._pedir('nadie@x.com')
        self.assertRedirects(respuesta, self.url_codigo)
        self.assertEqual(len(mail.outbox), 0)
        respuesta = self.client.post(self.url_codigo, {'codigo': '123456'})
        self.assertContains(respuesta, 'incorrecto o venció')

    def test_sin_codigo_validado_no_se_cambia(self):
        self._pedir()
        respuesta = self.client.get(reverse('apps.autenticacion:recuperar_nueva'))
        self.assertRedirects(respuesta, self.url)

    def test_codigo_vencido(self):
        self._pedir()
        codigo = self._codigo_del_correo()
        CodigoRecuperacion.objects.update(vence=timezone.now() - timedelta(seconds=1))
        respuesta = self.client.post(self.url_codigo, {'codigo': codigo})
        self.assertContains(respuesta, 'incorrecto o venció')

    def test_se_anula_tras_cinco_intentos(self):
        self._pedir()
        codigo = self._codigo_del_correo()
        malo = '000000' if codigo != '000000' else '111111'
        for _ in range(recuperacion.MAX_INTENTOS):
            self.client.post(self.url_codigo, {'codigo': malo})
        respuesta = self.client.post(self.url_codigo, {'codigo': codigo})
        self.assertContains(respuesta, 'incorrecto o venció')

    def test_codigo_nuevo_anula_el_anterior_y_hay_espera(self):
        self._pedir()
        viejo = self._codigo_del_correo()
        self._pedir()  # dentro de la espera: no manda otro
        self.assertEqual(len(mail.outbox), 1)
        CodigoRecuperacion.objects.update(creado=timezone.now() - timedelta(minutes=2))
        self.client.post(reverse('apps.autenticacion:recuperar_reenviar'))
        self.assertEqual(len(mail.outbox), 2)
        nuevo = self._codigo_del_correo()
        if viejo != nuevo:
            respuesta = self.client.post(self.url_codigo, {'codigo': viejo})
            self.assertContains(respuesta, 'incorrecto o venció')
        respuesta = self.client.post(self.url_codigo, {'codigo': nuevo})
        self.assertRedirects(respuesta, reverse('apps.autenticacion:recuperar_nueva'))

    def test_limite_por_hora(self):
        for _ in range(recuperacion.MAX_POR_HORA + 2):
            CodigoRecuperacion.objects.update(creado=timezone.now() - timedelta(minutes=5))
            self._pedir()
        self.assertEqual(len(mail.outbox), recuperacion.MAX_POR_HORA)


class RegistroValidacionesTests(TestCase):
    def _datos(self, **cambios):
        datos = dict(username='nuevo', email='nuevo@x.com', password1='Clave-Segura-2026x',
                     password2='Clave-Segura-2026x', celular1='3624111222', relacion1='Titular',
                     celular2='3624333444', relacion2='Esposa')
        datos.update(cambios)
        return datos

    def test_email_repetido_en_mayusculas(self):
        get_user_model().objects.create_user('ana', 'ana@x.com', 'Agua-Lluvia-2026')
        self.assertIn('email', RegistroUsuarioForm(self._datos(email='ANA@X.COM')).errors)

    def test_celular_con_letras(self):
        self.assertIn('celular1', RegistroUsuarioForm(self._datos(celular1='llamame ya')).errors)

    def test_personal_no_es_enviado_al_carrito(self):
        from django.contrib.auth.models import Group
        vendedor = get_user_model().objects.create_user('vend', 'v@x.com', 'Agua-Lluvia-2026')
        vendedor.groups.add(Group.objects.get(name='Vendedor'))
        respuesta = self.client.post(
            reverse('apps.autenticacion:ingresar') + '?next=/carrito/',
            {'username': 'vend', 'password': 'Agua-Lluvia-2026'},
        )
        self.assertNotIn('/carrito', respuesta.url)

    def test_usuario_logueado_no_ve_login_ni_registro(self):
        usuario = get_user_model().objects.create_user('ana', 'ana@x.com', 'Agua-Lluvia-2026')
        self.client.force_login(usuario)
        for nombre in ('ingresar', 'registrar'):
            self.assertEqual(self.client.get(reverse(f'apps.autenticacion:{nombre}')).status_code, 302)


class PerfilPersonalTests(TestCase):
    """El personal edita sus datos y cambia su contraseña desde /auth/perfil/."""

    def setUp(self):
        from django.contrib.auth.models import Group
        from apps.empleados.models import Empleado, RolEmpleado
        Usuario = get_user_model()
        self.usuario = Usuario.objects.create_user('vend', 'v@x.com', 'Agua-Lluvia-2026')
        self.usuario._es_empleado = True
        self.usuario.groups.add(Group.objects.get(name='Vendedor'))
        rol = RolEmpleado.objects.create(nombre='Vendedor QA', grupo_permisos='Vendedor')
        self.empleado = Empleado.objects.create(usuario=self.usuario, nombre='Viejo', apellido='Nombre',
                                                dni='30111222', rol=rol)
        self.client.force_login(self.usuario)
        self.url = reverse('apps.autenticacion:perfil')

    def test_edita_datos_y_sincroniza_empleado(self):
        respuesta = self.client.post(self.url, {'form_datos': '1', 'first_name': 'Ana', 'last_name': 'Paz',
                                                'email': 'ana@x.com', 'celular1': '3624 111222'})
        self.assertRedirects(respuesta, self.url)
        self.empleado.refresh_from_db()
        self.assertEqual((self.empleado.nombre, self.empleado.apellido, self.empleado.email, self.empleado.celular),
                         ('Ana', 'Paz', 'ana@x.com', '3624 111222'))

    def test_email_de_otra_cuenta(self):
        get_user_model().objects.create_user('otro', 'otro@x.com', 'Agua-Lluvia-2026')
        respuesta = self.client.post(self.url, {'form_datos': '1', 'first_name': 'Ana', 'last_name': 'Paz',
                                                'email': 'OTRO@x.com', 'celular1': ''})
        self.assertEqual(respuesta.status_code, 200)
        self.usuario.refresh_from_db()
        self.assertEqual(self.usuario.email, 'v@x.com')

    def test_cambia_contrasena_sin_cerrar_sesion(self):
        respuesta = self.client.post(self.url, {
            'form_password': '1', 'old_password': 'Agua-Lluvia-2026',
            'new_password1': 'Otra-Clave-2026x', 'new_password2': 'Otra-Clave-2026x',
        })
        self.assertRedirects(respuesta, self.url)
        self.usuario.refresh_from_db()
        self.assertTrue(self.usuario.check_password('Otra-Clave-2026x'))
        self.assertEqual(self.client.get(self.url).status_code, 200)

    def test_cliente_va_a_su_perfil(self):
        cliente = get_user_model().objects.create_user('cli', 'c@x.com', 'Agua-Lluvia-2026')
        self.client.force_login(cliente)
        self.assertRedirects(self.client.get(self.url), reverse('apps.clientes:mi_perfil'))
