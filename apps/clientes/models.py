from django.db import models


# ────────────────────────────────────────────────
# TIPO DE CLIENTE
# ────────────────────────────────────────────────
TIPO_CLIENTE_CHOICES = [
    ('Normal',  'Normal'),
    ('Premium', 'VIP / Premium'),
]


# ────────────────────────────────────────────────
# 1. CLIENTE
#    Perfil de negocio. Puede o no tener cuenta de acceso web.
#    Si tiene cuenta: vinculado a autenticacion.Usuario via OneToOne.
#    Si no tiene cuenta: sus datos se guardan directamente en este modelo.
# ────────────────────────────────────────────────
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
    # ── Datos propios (para clientes sin cuenta) ───────────────
    nombre           = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Nombre'
    )
    apellido         = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Apellido'
    )
    email_contacto   = models.EmailField(
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
    bidones_prestados = models.PositiveIntegerField(
        default=0,
        verbose_name='Bidones prestados'
    )
    permite_fiado    = models.BooleanField(
        default=False,
        verbose_name='Permite fiado',
        help_text='Habilitado automáticamente para clientes Premium'
    )
    notas_internas   = models.TextField(
        blank=True,
        verbose_name='Notas internas',
        help_text='Visible solo para Admin/Vendedor'
    )

    class Meta:
        ordering = ['apellido', 'nombre']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f"{self.nombre_completo()} [{self.tipo_cliente}]"

    def tiene_cuenta(self):
        """True si el cliente tiene cuenta de acceso web."""
        return self.usuario_id is not None

    def es_premium(self):
        return self.tipo_cliente == 'Premium'

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
        """Indica si el cliente tiene al menos 2 teléfonos y 1 dirección."""
        return self.cantidad_telefonos() >= 2 and self.cantidad_direcciones() >= 1

    def save(self, *args, **kwargs):
        # Si se cambia a Premium, habilitar fiado automáticamente
        if self.tipo_cliente == 'Premium':
            self.permite_fiado = True
        super().save(*args, **kwargs)


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
    numero        = models.CharField(max_length=25, verbose_name='Número')
    desc_relacion = models.CharField(
        max_length=100,
        verbose_name='Relación',
        help_text='Ej: "Titular", "Cónyuge", "Hijo", "Vecino de confianza"'
    )
    es_principal  = models.BooleanField(
        default=False,
        verbose_name='Principal'
    )

    class Meta:
        ordering = ['-es_principal', 'desc_relacion']
        verbose_name = 'Teléfono de contacto'
        verbose_name_plural = 'Teléfonos de contacto'

    def __str__(self):
        principal = ' ⭐' if self.es_principal else ''
        return f"{self.numero} ({self.desc_relacion}){principal}"

    def save(self, *args, **kwargs):
        # Si se marca como principal, desmarcar los demás del mismo cliente
        if self.es_principal:
            TelefonoContacto.objects.filter(
                cliente=self.cliente, es_principal=True
            ).exclude(pk=self.pk).update(es_principal=False)
        super().save(*args, **kwargs)


# ────────────────────────────────────────────────
# 3. DIRECCIÓN DE ENTREGA  — RF-03
#    desc_seguridad visible SOLO para Admin/Vendedor/Repartidor
# ────────────────────────────────────────────────
class DireccionEntrega(models.Model):
    cliente        = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='direcciones'
    )
    calle          = models.CharField(max_length=150, verbose_name='Calle')
    altura         = models.CharField(max_length=10, verbose_name='Altura / Número')
    piso_depto     = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Piso / Depto',
        help_text='Ej: "2°B", "PB derecha"'
    )
    zona           = models.ForeignKey(
        'logistica.Zona',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='direcciones_clientes',
        verbose_name='Zona'
    )
    desc_seguridad = models.TextField(
        blank=True,
        verbose_name='Nota de seguridad',
        help_text='SOLO visible para Admin, Vendedor y Repartidor asignado — RF-03'
    )
    coordenadas    = models.CharField(
        max_length=60,
        blank=True,
        verbose_name='Coordenadas (lat,lng)',
        help_text='Para futura integración con mapas'
    )
    es_principal   = models.BooleanField(
        default=False,
        verbose_name='Principal'
    )

    class Meta:
        ordering = ['-es_principal', 'calle', 'altura']
        verbose_name = 'Dirección de entrega'
        verbose_name_plural = 'Direcciones de entrega'

    def __str__(self):
        extra = f" — {self.piso_depto}" if self.piso_depto else ""
        zona  = f" [{self.zona}]" if self.zona else ""
        return f"{self.calle} {self.altura}{extra}{zona}"

    def direccion_completa(self):
        partes = [f"{self.calle} {self.altura}"]
        if self.piso_depto:
            partes.append(self.piso_depto)
        if self.zona:
            partes.append(str(self.zona))
        return ', '.join(partes)

    def save(self, *args, **kwargs):
        # Si se marca como principal, desmarcar las demás del mismo cliente
        if self.es_principal:
            DireccionEntrega.objects.filter(
                cliente=self.cliente, es_principal=True
            ).exclude(pk=self.pk).update(es_principal=False)
        super().save(*args, **kwargs)
