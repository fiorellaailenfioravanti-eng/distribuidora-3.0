from django.db import models
from django.utils import timezone


# ────────────────────────────────────────────────
# 1. ZONA
# ────────────────────────────────────────────────
class Zona(models.Model):
    id_zona     = models.AutoField(primary_key=True)
    nombre      = models.CharField(max_length=100, unique=True)
    ciudad      = models.CharField(max_length=100, default='Presidencia Roque Sáenz Peña', blank=True, verbose_name='Ciudad')
    barrios     = models.TextField(blank=True, verbose_name='Barrios incluidos', help_text='Barrios que abarca esta zona (ej: Centro, San Martín, Belgrano)')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    # Días de reparto
    lunes       = models.BooleanField(default=False)
    martes      = models.BooleanField(default=False)
    miercoles   = models.BooleanField(default=False)
    jueves      = models.BooleanField(default=False)
    viernes     = models.BooleanField(default=False)
    sabado      = models.BooleanField(default=False)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'

    def dias_activos(self):
        dias = []
        if self.lunes: dias.append("Lun")
        if self.martes: dias.append("Mar")
        if self.miercoles: dias.append("Mié")
        if self.jueves: dias.append("Jue")
        if self.viernes: dias.append("Vie")
        if self.sabado: dias.append("Sáb")
        return ", ".join(dias) if dias else "Sin días"

    def __str__(self):
        return self.nombre


# ────────────────────────────────────────────────
# 2. ROL EMPLEADO
# ────────────────────────────────────────────────
class RolEmpleado(models.Model):
    id_rol      = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Rol de Empleado'
        verbose_name_plural = 'Roles de Empleados'

    def __str__(self):
        return self.descripcion


# ────────────────────────────────────────────────
# 3. EMPLEADO
# ────────────────────────────────────────────────
class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    usuario     = models.OneToOneField(
        'autenticacion.Usuario',
        on_delete=models.CASCADE,
        related_name='empleado'
    )
    rol         = models.ForeignKey(
        RolEmpleado,
        on_delete=models.PROTECT,
        related_name='empleados'
    )
    activo      = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return f"{self.usuario.get_full_name() or self.usuario.username} — {self.rol}"

    def es_repartidor(self):
        return self.usuario.groups.filter(name='Repartidor').exists()


# ────────────────────────────────────────────────
# 4. CAMION
# ────────────────────────────────────────────────
class Camion(models.Model):
    patente     = models.CharField(max_length=10, primary_key=True)
    descripcion = models.CharField(max_length=200, blank=True)
    activo      = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Camión'
        verbose_name_plural = 'Camiones'

    def __str__(self):
        return f"{self.patente}" + (f" — {self.descripcion}" if self.descripcion else "")


# ────────────────────────────────────────────────
# 5. HOJA DE RUTA
# ────────────────────────────────────────────────
ESTADOS_RUTA = [
    ('Abierta',   'Abierta'),
    ('En curso',  'En curso'),
    ('Cerrada',   'Cerrada'),
]


class HojaRuta(models.Model):
    id_ruta       = models.AutoField(primary_key=True)
    fecha         = models.DateField()
    empleado      = models.ForeignKey(
        Empleado,
        on_delete=models.PROTECT,
        related_name='rutas'
    )
    camion        = models.ForeignKey(
        Camion,
        on_delete=models.PROTECT,
        related_name='rutas'
    )
    zona          = models.ForeignKey(
        Zona,
        on_delete=models.PROTECT,
        related_name='rutas'
    )
    estado        = models.CharField(
        max_length=20,
        choices=ESTADOS_RUTA,
        default='Abierta'
    )
    observaciones = models.TextField(blank=True)
    creado_por    = models.ForeignKey(
        'autenticacion.Usuario',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='rutas_creadas'
    )

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Hoja de Ruta'
        verbose_name_plural = 'Hojas de Ruta'

    def __str__(self):
        return f"Ruta #{self.id_ruta} — {self.fecha} · {self.zona} · {self.empleado}"

    def total_paradas(self):
        return self.detalles.count()

    def paradas_entregadas(self):
        return self.detalles.filter(estado='Entregado').count()

    def porcentaje_completado(self):
        total = self.total_paradas()
        if total == 0:
            return 0
        return int((self.paradas_entregadas() / total) * 100)


# ────────────────────────────────────────────────
# 6. DETALLE HOJA DE RUTA
# ────────────────────────────────────────────────
ESTADOS_ENTREGA = [
    ('Pendiente',     'Pendiente'),
    ('Entregado',     'Entregado'),
    ('Cancelado',     'Cancelado'),
    ('Reprogramado',  'Reprogramado'),
]


class DetalleHojaRuta(models.Model):
    id_detalle    = models.AutoField(primary_key=True)
    hoja_ruta     = models.ForeignKey(
        HojaRuta,
        on_delete=models.CASCADE,
        related_name='detalles'
    )
    # FK a Pedido se activa cuando el módulo de Pedidos (Mes 8) esté implementado
    # pedido      = models.ForeignKey('pedidos.Pedido', on_delete=models.SET_NULL, null=True, blank=True)
    pedido_ref    = models.CharField(
        max_length=100,
        blank=True,
        help_text='Referencia temporal al pedido hasta que exista el modelo Pedido'
    )
    # Dirección textual hasta integrar el modelo Direccion_entrega (Mes 7)
    direccion     = models.CharField(
        max_length=255,
        blank=True,
        help_text='Dirección de entrega (texto libre hasta integrar Direccion_entrega)'
    )
    cliente_nombre = models.CharField(
        max_length=200,
        blank=True,
        help_text='Nombre del cliente para identificación rápida'
    )
    orden         = models.PositiveIntegerField(
        default=0,
        help_text='Orden de visita dentro de la ruta (menor = primero)'
    )
    estado        = models.CharField(
        max_length=20,
        choices=ESTADOS_ENTREGA,
        default='Pendiente'
    )
    nota_entrega  = models.TextField(blank=True)
    hora_registro = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['orden']
        verbose_name = 'Detalle de Ruta'
        verbose_name_plural = 'Detalles de Ruta'

    def __str__(self):
        return f"Parada {self.orden} — {self.get_estado_display()} ({self.cliente_nombre or self.pedido_ref})"

    def marcar_estado(self, nuevo_estado):
        """Actualiza el estado y registra la hora si es una acción terminal."""
        self.estado = nuevo_estado
        if nuevo_estado in ('Entregado', 'Cancelado'):
            self.hora_registro = timezone.now()
        self.save()
