from decimal import Decimal

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse

from .forms import EmpleadoForm
from .models import Empleado, RolEmpleado


class RolSincronizaGrupoTests(TestCase):
    """H-25 / A-D3: el rol del empleado define su grupo de permisos."""

    def setUp(self):
        self.rol_rep = RolEmpleado.objects.create(nombre='Chofer', grupo_permisos='Repartidor')
        self.rol_vend = RolEmpleado.objects.create(nombre='Vendedora', grupo_permisos='Vendedor')
        self.rol_sin = RolEmpleado.objects.create(nombre='Limpieza', grupo_permisos='')

    def _alta(self, rol, **extra):
        datos = {
            'nombre': 'Juan', 'apellido': 'Pérez', 'dni': '30111222', 'email': 'juan@x.com',
            'rol': rol.pk, 'activo': True, 'username': 'juanp', 'password': 'Agua-Lluvia-2026',
        }
        datos.update(extra)
        form = EmpleadoForm(data=datos)
        self.assertTrue(form.is_valid(), form.errors)
        return form.save()

    def _grupos(self, empleado):
        return set(empleado.usuario.groups.values_list('name', flat=True))

    def test_alta_asigna_grupo_del_rol(self):
        empleado = self._alta(self.rol_rep)
        self.assertEqual(self._grupos(empleado), {'Repartidor'})

    def test_cambio_de_rol_cambia_grupo(self):
        empleado = self._alta(self.rol_rep)
        empleado.rol = self.rol_vend
        empleado.save()
        self.assertEqual(self._grupos(empleado), {'Vendedor'})

    def test_empleado_inactivo_o_rol_sin_permisos_queda_sin_grupo(self):
        empleado = self._alta(self.rol_vend)
        empleado.activo = False
        empleado.save()
        self.assertEqual(self._grupos(empleado), set())
        empleado.activo = True
        empleado.rol = self.rol_sin
        empleado.save()
        self.assertEqual(self._grupos(empleado), set())

    def test_cambiar_permisos_del_rol_resincroniza(self):
        empleado = self._alta(self.rol_rep)
        self.rol_rep.grupo_permisos = 'Vendedor'
        self.rol_rep.save()
        self.assertEqual(self._grupos(empleado), {'Vendedor'})

    def test_no_otorga_superusuario_ni_toca_otros_grupos(self):
        empleado = self._alta(self.rol_vend)
        extra = Group.objects.create(name='Auditoria')
        empleado.usuario.groups.add(extra)
        empleado.save()
        empleado.usuario.refresh_from_db()
        self.assertFalse(empleado.usuario.is_superuser)
        self.assertIn('Auditoria', self._grupos(empleado))

    def test_contrasena_debil_rechazada(self):
        """H-36: el alta de empleado aplica AUTH_PASSWORD_VALIDATORS (RF-02)."""
        form = EmpleadoForm(data={
            'nombre': 'Ana', 'apellido': 'Gómez', 'dni': '30999888', 'email': 'ana@x.com',
            'rol': self.rol_rep.pk, 'activo': True, 'username': 'anag', 'password': '1234',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)


class GuardsUnificadosTests(TestCase):
    def setUp(self):
        Usuario = get_user_model()
        self.vendedor = Usuario.objects.create_user('vend', 'vend@x.com', 'Agua-Lluvia-2026')
        self.vendedor.groups.add(Group.objects.get(name='Vendedor'))

    def test_vendedor_por_grupo_ve_el_dashboard(self):
        """H-24: el dashboard usa la misma regla que el resto de las apps."""
        self.client.force_login(self.vendedor)
        respuesta = self.client.get(reverse('dashboard'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTrue(respuesta.context['es_vendedor'])

    def test_dashboard_cuenta_pedidos_pendientes(self):
        """H-23: el filtro usa el valor real del estado ('Pendiente')."""
        from apps.pedidos.models import MetodoPago, Pedido
        Pedido.objects.create(
            metodo_pago=MetodoPago.objects.get(codigo='EFECTIVO'),
            total=Decimal('10'), estado='Pendiente',
        )
        self.client.force_login(self.vendedor)
        respuesta = self.client.get(reverse('dashboard'))
        self.assertEqual(respuesta.context['pedidos_pendientes'], 1)

    def test_usuario_sin_permiso_en_empleados_no_da_500(self):
        """H-26: la redirección apunta a una ruta existente."""
        Usuario = get_user_model()
        cliente = Usuario.objects.create_user('cli', 'cli@x.com', 'Agua-Lluvia-2026')
        self.client.force_login(cliente)
        respuesta = self.client.get(reverse('apps.empleados:listar_empleados'))
        self.assertEqual(respuesta.status_code, 302)


class PantallasDeRolesTests(TestCase):
    def test_listado_de_roles_renderiza(self):
        """El template usaba `rol.id` (la PK es `id_rol`) y daba 500."""
        RolEmpleado.objects.create(nombre='Chofer', grupo_permisos='Repartidor')
        admin = get_user_model().objects.create_superuser('root', 'root@x.com', 'Agua-Lluvia-2026')
        self.client.force_login(admin)
        respuesta = self.client.get(reverse('apps.empleados:listar_roles'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'Chofer')
