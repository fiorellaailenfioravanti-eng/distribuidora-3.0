from django.db import models
from django.utils import timezone


# ────────────────────────────────────────────────
# 1. ZONA
# ────────────────────────────────────────────────
class Zona(models.Model):
    id_zona     = models.AutoField(primary_key=True)
    nombre      = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, verbose_name='Descripción')

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'

    def __str__(self):
        return self.nombre


# ────────────────────────────────────────────────
# 1.5. BARRIO
# ────────────────────────────────────────────────
class Barrio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100, default='Resistencia')
    zona   = models.ForeignKey(
        Zona, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='barrios_asociados'
    )

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Barrio'
        verbose_name_plural = 'Barrios'

    def __str__(self):
        return f"{self.nombre} ({self.ciudad})"


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
# 4.5. RUTA DE REPARTO
# ────────────────────────────────────────────────
DIA_SEMANA_CHOICES = [
    (0, 'Lunes'),
    (1, 'Martes'),
    (2, 'Miércoles'),
    (3, 'Jueves'),
    (4, 'Viernes'),
    (5, 'Sábado'),
    (6, 'Domingo'),
]

class RutaReparto(models.Model):
    id_ruta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, help_text='Ej: Ruta Norte - Lunes')
    zona = models.ForeignKey(Zona, on_delete=models.PROTECT, related_name='rutas')
    dia_semana = models.IntegerField(choices=DIA_SEMANA_CHOICES)
    empleado_default = models.ForeignKey(
        Empleado, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='rutas_default'
    )
    camion_default = models.ForeignKey(
        Camion, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='rutas_default'
    )

    class Meta:
        ordering = ['dia_semana', 'nombre']
        verbose_name = 'Ruta de Reparto'
        verbose_name_plural = 'Rutas de Reparto'

    def __str__(self):
        return f"{self.nombre} ({self.get_dia_semana_display()})"


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
    ruta_reparto  = models.ForeignKey(
        RutaReparto,
        on_delete=models.PROTECT,
        related_name='hojas_ruta',
        verbose_name='Ruta de Reparto'
    )
    empleado      = models.ForeignKey(
        Empleado,
        on_delete=models.PROTECT,
        related_name='hojas_ruta'
    )
    camion        = models.ForeignKey(
        Camion,
        on_delete=models.PROTECT,
        related_name='hojas_ruta'
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
        return f"Hoja #{self.id_ruta} — {self.fecha} · {self.ruta_reparto} · {self.empleado}"

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
    pedido_ref    = models.CharField(
        max_length=100,
        blank=True,
        help_text='Referencia temporal al pedido hasta que exista el modelo Pedido'
    )
    direccion_entrega = models.ForeignKey(
        'clientes.DireccionEntrega',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='visitas_ruta',
        verbose_name='Dirección de Entrega'
    )
    # Dirección textual de respaldo
    direccion_texto = models.CharField(
        max_length=255,
        blank=True,
        help_text='Dirección en texto si no hay una vinculada'
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
