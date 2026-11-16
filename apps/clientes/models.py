from django.conf import settings
from django.db import models
from django.utils import timezone
from distribuidora.bajas import SinEliminadosManager
from distribuidora.limites import LARGO_NOMBRE, LARGO_TEXTO, limite_largo


# ────────────────────────────────────────────────
# TIPO DE CLIENTE
# ────────────────────────────────────────────────
TIPO_CLIENTE_CHOICES = [
    ('Normal',  'Normal'),
    ('Premium', 'VIP / Premium'),
]


# ────────────────────────────────────────────────
# TIPO DE REGISTRO
# ────────────────────────────────────────────────
TIPO_REGISTRO_CHOICES = [
    ('registrado', 'Registrado'),
    ('pasajero',   'Pasajero'),
]


# ────────────────────────────────────────────────
# 1. CLIENTE
#    Perfil de negocio. Puede o no tener cuenta de acceso web.
#    Si tiene cuenta: vinculado a autenticacion.Usuario via OneToOne.
#    Si no tiene cuenta: sus datos se guardan directamente en este modelo.
# ────────────────────────────────────────────────

def _bloquear_cuenta(usuario, bloquear):
    """Baja/alta de la cuenta web vinculada. Nunca toca al superusuario."""
    if usuario is None or usuario.is_superuser:
        return
    usuario.is_active = not bloquear
    usuario.save(update_fields=['is_active'])

class Cliente(models.Model):
    # ── Cuenta web (opcional) ──────────────────────────────────
    usuario          = models.OneToOneField(
        'autenticacion.Usuario',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='perfil_cliente',
        verbose_name='Cuenta de usuario'
    )
    numero           = models.CharField(
        max_length=10,
        unique=True,
        null=True,
        blank=True,
        editable=False,
        verbose_name='Nro de cliente',
        help_text='Los importados conservan su número del sistema anterior (ej. 1003389); '
                  'los nuevos se numeran 0000001, 0000002…'
    )
    # ── Datos propios (para clientes sin cuenta) ───────────────
    nombre           = models.CharField(
        max_length=LARGO_NOMBRE,
        blank=True,
        verbose_name='Nombre'
    )
    apellido         = models.CharField(
        max_length=LARGO_NOMBRE,
        blank=True,
        verbose_name='Apellido'
    )
    email_contacto   = models.EmailField(
        max_length=120,
        blank=True,
        verbose_name='Email de contacto',
        help_text='Opcional — para clientes sin cuenta web'
    )
    dni              = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        verbose_name='DNI'
    )
    fecha_nacimiento = models.DateField(
        null=True,
        blank=True,
        verbose_name='Fecha de nacimiento'
    )
    fecha_alta       = models.DateField(
        auto_now_add=True,
        verbose_name='Fecha de alta'
    )
    tipo_cliente     = models.CharField(
        max_length=10,
        choices=TIPO_CLIENTE_CHOICES,
        default='Normal',
        verbose_name='Tipo de cliente'
    )
    bidones_prestados = models.IntegerField(
        default=0,
        verbose_name='Bidones prestados',
        help_text='Saldo calculado del historial de envases. No se edita a mano: '
                  'se registra un movimiento. Negativo = devolvió más de los prestados.'
    )
    permite_fiado    = models.BooleanField(
        default=False,
        verbose_name='Permite fiado',
        help_text='Automático para Premium. A un cliente Normal sólo se le habilita '
                  'como excepción autorizada.'
    )
    notas_internas   = models.TextField(
        max_length=LARGO_TEXTO,
        blank=True,
        verbose_name='Notas internas',
        help_text='Visible solo para Admin/Vendedor'
    )
    tipo_registro    = models.CharField(
        max_length=12,
        choices=TIPO_REGISTRO_CHOICES,
        default='registrado',
        verbose_name='Tipo de registro',
        help_text='Los clientes pasajeros son registrados en el reparto y pueden no tener cuenta.'
    )
    eliminado        = models.BooleanField(
        default=False,
        verbose_name='Eliminado',
        help_text='Baja lógica: no aparece en el directorio ni en los listados para '
                  'elegir clientes, y no puede ingresar a la tienda. Se restaura desde '
                  '«Clientes eliminados». Sus pedidos, cuenta e historial se conservan.'
    )
    es_frecuente     = models.BooleanField(
        default=False,
        verbose_name='Cliente frecuente',
        help_text='Aparece al planificar las hojas de ruta de su zona.'
    )
    cantidad_recurrente_default = models.PositiveIntegerField(
        default=0,
        verbose_name='Botellones habituales',
        help_text='Cantidad sugerida al incluirlo en una hoja de ruta.'
    )

    class Meta:
        ordering = ['apellido', 'nombre']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        constraints = limite_largo(nombre=LARGO_NOMBRE, apellido=LARGO_NOMBRE, notas_internas=LARGO_TEXTO,
                                   email_contacto=120, dni=15)

    def __str__(self):
        return f"{self.nombre_completo()} [{self.tipo_cliente}]"

    def tiene_cuenta(self):
        """True si el cliente tiene cuenta de acceso web."""
        return self.usuario_id is not None

    def es_premium(self):
        return self.tipo_cliente == 'Premium'

    def dar_de_baja(self):
        """Baja lógica: se oculta y se bloquea su acceso web (si no es personal)."""
        self.eliminado = True
        self.es_frecuente = False
        self.save(update_fields=['eliminado', 'es_frecuente'])
        u = self.usuario
        if u is not None and not hasattr(u, 'perfil_empleado'):
            _bloquear_cuenta(u, True)

    def restaurar(self):
        self.eliminado = False
        self.save(update_fields=['eliminado'])
        u = self.usuario
        if u is not None and not hasattr(u, 'perfil_empleado'):
            _bloquear_cuenta(u, False)

    def nombre_completo(self):
        """Nombre legíble independientemente de si tiene cuenta o no."""
        if self.usuario_id:
            nombre_user = self.usuario.get_full_name()
            return nombre_user if nombre_user.strip() else self.usuario.username
        # Sin cuenta: usar campos propios
        partes = [p for p in [self.nombre, self.apellido] if p]
        return ' '.join(partes) if partes else f'Cliente #{self.pk}'

    def email_display(self):
        """Email para mostrar (de la cuenta si existe, sino el propio)."""
        if self.usuario_id:
            return self.usuario.email
        return self.email_contacto

    def cantidad_telefonos(self):
        return self.telefonos.count()

    def cantidad_direcciones(self):
        return self.direcciones.count()

    def tiene_datos_completos(self):
        """Indica si el cliente tiene al menos 1 teléfono y 1 dirección."""
        return self.cantidad_telefonos() >= 1 and self.cantidad_direcciones() >= 1

    def save(self, *args, **kwargs):
        # RF-05 (decisión A-D6): el Premium siempre tiene fiado; un Normal sólo
        # como excepción manual. Al bajar de Premium a Normal se quita el
        # fiado automático (H-41); si corresponde, se vuelve a habilitar aparte.
        if self.tipo_cliente == 'Premium':
            self.permite_fiado = True
        elif self.pk:
            tipo_anterior = (
                Cliente.objects.filter(pk=self.pk).values_list('tipo_cliente', flat=True).first()
            )
            if tipo_anterior == 'Premium':
                self.permite_fiado = False
        if not self.numero:
            self.numero = siguiente_numero_cliente()
        super().save(*args, **kwargs)


def siguiente_numero_cliente():
    """Próximo número para un cliente nuevo: 0000001, 0000002… (los que empiezan
    con 0 son los dados de alta en este sistema; los importados conservan el suyo)."""
    ultimo = (Cliente._base_manager.filter(numero__startswith='000')
              .order_by('-numero').values_list('numero', flat=True).first())
    siguiente = int(ultimo or 0) + 1
    # Algunos importados también empiezan con 0 (ej. 0010059): se saltean.
    while Cliente._base_manager.filter(numero=f'{siguiente:07d}').exists():
        siguiente += 1
    return f'{siguiente:07d}'


# ────────────────────────────────────────────────
# 2. TELÉFONO DE CONTACTO  — RF-04
#    Mínimo 2 por cliente con relación explícita
# ────────────────────────────────────────────────
class TelefonoContacto(models.Model):
    cliente       = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='telefonos'
    )
    numero        = models.CharField(max_length=20, verbose_name='Número')
    desc_relacion = models.CharField(
        max_length=40,
        verbose_name='Relación',
        help_text='Ej: "Titular", "Cónyuge", "Hijo", "Vecino de confianza"'
    )
    es_principal  = models.BooleanField(
        default=False,
        verbose_name='Principal'
    )

    eliminado = models.BooleanField(default=False, verbose_name='Eliminado',
                                    help_text='Baja lógica: se oculta pero no se borra; se puede restaurar.')

    objects = SinEliminadosManager()
    todos = models.Manager()

    class Meta:
        ordering = ['-es_principal', 'desc_relacion']
        verbose_name = 'Teléfono de contacto'
        verbose_name_plural = 'Teléfonos de contacto'
        constraints = limite_largo(numero=20, desc_relacion=40)

    def __str__(self):
        principal = ' ⭐' if self.es_principal else ''
        return f"{self.numero} ({self.desc_relacion}){principal}"

    def dar_de_baja(self):
        self.eliminado = True
        era_principal = self.es_principal
        self.es_principal = False
        self.save(update_fields=['eliminado', 'es_principal'])
        if era_principal:
            otro = TelefonoContacto.objects.filter(cliente=self.cliente).first()
            if otro:
                TelefonoContacto.objects.filter(pk=otro.pk).update(es_principal=True)

    def save(self, *args, **kwargs):
        # Si se marca como principal, desmarcar los demás del mismo cliente
        if self.es_principal:
            TelefonoContacto.objects.filter(
                cliente=self.cliente, es_principal=True
            ).exclude(pk=self.pk).update(es_principal=False)
        super().save(*args, **kwargs)


# ────────────────────────────────────────────────
# 3. DIRECCIÓN DE ENTREGA  — RF-03
#    desc_seguridad es información sensible: se controla por RNF-02
#    (ver apps/permisos/roles.py::puede_ver_nota_seguridad)
# ────────────────────────────────────────────────
class DireccionEntrega(models.Model):
    cliente        = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='direcciones'
    )
    calle          = models.CharField(max_length=100, verbose_name='Calle')
    altura         = models.CharField(max_length=10, verbose_name='Altura / Número')
    piso_depto     = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Piso / Depto',
        help_text='Ej: "2°B", "PB derecha"'
    )
    barrio         = models.ForeignKey(
        'logistica.Barrio',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='direcciones_clientes',
        verbose_name='Barrio'
    )
    ciudad         = models.CharField(
        max_length=LARGO_NOMBRE,
        blank=True,
        default='Resistencia',
        verbose_name='Ciudad / Localidad'
    )
    desc_seguridad = models.TextField(
        max_length=LARGO_TEXTO,
        blank=True,
        verbose_name='Nota de seguridad',
        help_text=(
            'Información sensible: visible solo para Admin, Vendedor y el '
            'Repartidor asignado a esa dirección.'
        )
    )
    coordenadas    = models.CharField(
        max_length=40,
        blank=True,
        verbose_name='Coordenadas (lat,lng)',
        help_text='Para futura integración con mapas'
    )
    es_principal   = models.BooleanField(
        default=False,
        verbose_name='Principal'
    )

    eliminado = models.BooleanField(default=False, verbose_name='Eliminado',
                                    help_text='Baja lógica: se oculta pero no se borra; se puede restaurar.')

    objects = SinEliminadosManager()
    todos = models.Manager()

    class Meta:
        ordering = ['-es_principal', 'calle', 'altura']
        verbose_name = 'Dirección de entrega'
        verbose_name_plural = 'Direcciones de entrega'
        constraints = limite_largo(desc_seguridad=LARGO_TEXTO, calle=100, altura=10, piso_depto=30,
                                   ciudad=LARGO_NOMBRE, coordenadas=40)

    def __str__(self):
        extra = f" — {self.piso_depto}" if self.piso_depto else ""
        barrio_str = f" (B° {self.barrio.nombre})" if self.barrio else ""
        zona  = f" [{self.barrio.zona}]" if self.barrio and self.barrio.zona else ""
        return f"{self.calle} {self.altura}{extra}{barrio_str}{zona}"

    def url_google_maps(self):
        """Enlace para ver el domicilio en Google Maps: por coordenadas si están
        cargadas (más preciso); si no, por calle, altura y ciudad."""
        from urllib.parse import quote
        if self.coordenadas.strip():
            consulta = self.coordenadas.replace(' ', '')
        else:
            consulta = f'{self.calle} {self.altura}, {self.ciudad or "Resistencia"}, Chaco, Argentina'
        return f'https://www.google.com/maps/search/?api=1&query={quote(consulta)}'

    def direccion_completa(self):
        partes = [f"{self.calle} {self.altura}"]
        if self.piso_depto:
            partes.append(self.piso_depto)
        if self.barrio:
            partes.append(f"B° {self.barrio.nombre}")
        if self.ciudad:
            partes.append(self.ciudad)
        if self.barrio and self.barrio.zona:
            partes.append(str(self.barrio.zona))
        return ', '.join(partes)

    def dar_de_baja(self):
        self.eliminado = True
        era_principal = self.es_principal
        self.es_principal = False
        self.save(update_fields=['eliminado', 'es_principal'])
        if era_principal:
            otra = DireccionEntrega.objects.filter(cliente=self.cliente).first()
            if otra:
                DireccionEntrega.objects.filter(pk=otra.pk).update(es_principal=True)

    def save(self, *args, **kwargs):
        # Si se marca como principal, desmarcar las demás del mismo cliente
        if self.es_principal:
            DireccionEntrega.objects.filter(
                cliente=self.cliente, es_principal=True
            ).exclude(pk=self.pk).update(es_principal=False)
        super().save(*args, **kwargs)



# ────────────────────────────────────────────────
# 4. MOVIMIENTO DE BIDONES  — RF-08
#    Historial de envases prestados y devueltos. El saldo del cliente
#    (`Cliente.bidones_prestados`) es la suma de `cantidad`.
# ────────────────────────────────────────────────
TIPOS_MOVIMIENTO_BIDON = [
    ('Prestamo',   'Préstamo (entrega de llenos)'),
    ('Devolucion', 'Devolución de vacíos'),
    ('Venta',      'Envase vendido al cliente'),
    ('Ajuste',     'Ajuste manual'),
]


class MovimientoBidon(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    cliente       = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='movimientos_bidon',
        verbose_name='Cliente'
    )
    tipo          = models.CharField(max_length=12, choices=TIPOS_MOVIMIENTO_BIDON, verbose_name='Tipo')
    cantidad      = models.IntegerField(
        verbose_name='Efecto en el saldo',
        help_text='Positivo suma envases prestados; negativo los descuenta.'
    )
    fecha         = models.DateTimeField(default=timezone.now, verbose_name='Fecha')
    pedido        = models.ForeignKey(
        'pedidos.Pedido',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='movimientos_bidon',
        verbose_name='Pedido'
    )
    parada        = models.ForeignKey(
        'logistica.DetalleHojaRuta',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='movimientos_bidon',
        verbose_name='Parada de reparto'
    )
    registrado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='movimientos_bidon',
        verbose_name='Registrado por'
    )
    nota          = models.CharField(max_length=200, blank=True, verbose_name='Nota')

    class Meta:
        ordering = ['-fecha', '-id_movimiento']
        verbose_name = 'Movimiento de bidones'
        verbose_name_plural = 'Movimientos de bidones'

    def __str__(self):
        return f"{self.get_tipo_display()} {self.cantidad:+d} — {self.cliente.nombre_completo()}"

    def cantidad_absoluta(self):
        return abs(self.cantidad)
