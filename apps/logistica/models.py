from django.db import models
from django.utils import timezone

# `Empleado` y `RolEmpleado` viven ÚNICAMENTE en `apps.empleados`.
#
# Antes cada app declaraba su propia copia, lo que producía cuatro tablas
# (empleados_empleado, empleados_rolempleado, logistica_empleado y
# logistica_rolempleado) con los datos repartidos entre ambas. Como la de
# logística quedó vacía, el selector de repartidor de `HojaRutaForm` no tenía
# opciones y no se podía crear ninguna hoja de ruta.
#
# Ver migración logistica.0006_eliminar_empleados_duplicados.
from apps.empleados.models import Empleado  # noqa: F401  (re-exportado)


# ────────────────────────────────────────────────
# 1. ZONA
# ────────────────────────────────────────────────
class Zona(models.Model):
    id_zona     = models.AutoField(primary_key=True)
    nombre      = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    dias_reparto = models.CharField(
        max_length=20,
        blank=True,
        default='',
        verbose_name='Días de reparto',
        help_text='Días de la semana en que se reparte la zona. Ej: 1,4 (lunes y jueves).'
    )

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'

    def __str__(self):
        return self.nombre

    def get_dias_reparto(self):
        """Devuelve la lista de días de reparto como enteros de `weekday()` (0=lunes)."""
        partes = (self.dias_reparto or '').split(',')
        return sorted({int(p) for p in partes if p.strip().isdigit() and 0 <= int(p) <= 6})

    def set_dias_reparto(self, dias):
        """Guarda los días de reparto como cadena ordenada y sin repetidos."""
        self.dias_reparto = ','.join(str(int(d)) for d in sorted({int(d) for d in dias}))

    def incluye_dia(self, weekday):
        return weekday in self.get_dias_reparto()

    def dias_reparto_display(self):
        """Nombres legibles de los días de reparto."""
        return ', '.join(dict(DIA_SEMANA_CHOICES).get(d, str(d)) for d in self.get_dias_reparto())


# ────────────────────────────────────────────────
# 1.2. EXCEPCIONES DE CALENDARIO
#      Permiten suspender o agregar un día de reparto
#      (feriados, días no laborables o jornadas extra).
# ────────────────────────────────────────────────
TIPOS_EXCEPCION = [
    ('suspende', 'Suspende reparto'),
    ('agrega',   'Agrega reparto'),
]

class CalendarioExcepcion(models.Model):
    id_excepcion = models.AutoField(primary_key=True)
    fecha = models.DateField()
    zona  = models.ForeignKey(
        Zona,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='excepciones_calendario',
        verbose_name='Zona',
        help_text='Vacío = aplica a todas las zonas.'
    )
    tipo   = models.CharField(max_length=10, choices=TIPOS_EXCEPCION, default='suspende')
    motivo = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Excepción de calendario'
        verbose_name_plural = 'Excepciones de calendario'

    def __str__(self):
        alcance = self.zona.nombre if self.zona_id else 'Todas las zonas'
        return f"{self.fecha} · {self.get_tipo_display()} · {alcance}"


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
# 3. CAMION
# ────────────────────────────────────────────────
class Camion(models.Model):
    patente     = models.CharField(max_length=10, primary_key=True)
    descripcion = models.CharField(max_length=200, blank=True)
    activo      = models.BooleanField(default=True)
    capacidad_botellones = models.PositiveIntegerField(
        default=30,
        verbose_name='Capacidad en botellones',
        help_text='Cantidad de botellones que puede cargar. No limita los productos de menor tamaño.'
    )

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
    ('Borrador',   'Borrador'),
    ('Confirmada', 'Confirmada'),
    ('Cerrada',    'Cerrada'),
]

class HojaRuta(models.Model):
    id_ruta       = models.AutoField(primary_key=True)
    fecha         = models.DateField()
    zona          = models.ForeignKey(
        Zona,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='hojas_ruta',
        verbose_name='Zona'
    )
    ruta_reparto  = models.ForeignKey(
        RutaReparto,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='hojas_ruta',
        verbose_name='Ruta de Reparto'
    )
    empleado      = models.ForeignKey(
        Empleado,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='hojas_ruta'
    )
    camion        = models.ForeignKey(
        Camion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='hojas_ruta'
    )
    estado        = models.CharField(
        max_length=20,
        choices=ESTADOS_RUTA,
        default='Borrador'
    )
    observaciones = models.TextField(blank=True)
    generada_automaticamente = models.BooleanField(default=False)
    confirmada_por = models.ForeignKey(
        'autenticacion.Usuario',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='rutas_confirmadas'
    )
    fecha_confirmacion = models.DateTimeField(null=True, blank=True)
    fecha_salida       = models.DateTimeField(null=True, blank=True)
    fecha_regreso      = models.DateTimeField(null=True, blank=True)
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
        zona_str = self.zona.nombre if self.zona_id else (str(self.ruta_reparto) if self.ruta_reparto_id else 'sin zona')
        return f"Hoja #{self.id_ruta} — {self.fecha} · {zona_str} · {self.empleado or 'sin asignar'}"

    def total_paradas(self):
        return self.detalles.count()

    def paradas_entregadas(self):
        return self.detalles.filter(estado='Entregado').count()

    def porcentaje_completado(self):
        total = self.total_paradas()
        if total == 0:
            return 0
        return int((self.paradas_entregadas() / total) * 100)

    def total_botellones(self):
        return sum(d.cantidad_bidones for d in self.detalles.all())

    def supera_capacidad(self):
        if not self.camion_id:
            return False
        return self.total_botellones() > self.camion.capacidad_botellones


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
        help_text='Referencia/observación manual para paradas sin pedido asociado'
    )
    pedido        = models.ForeignKey(
        'pedidos.Pedido',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='paradas',
        verbose_name='Pedido'
    )
    cliente       = models.ForeignKey(
        'clientes.Cliente',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='paradas_ruta',
        verbose_name='Cliente'
    )
    es_frecuente  = models.BooleanField(
        default=False,
        verbose_name='Cliente frecuente',
        help_text='Indica que la parada proviene de un cliente frecuente de la zona.'
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
    cantidad_bidones  = models.PositiveIntegerField(
        default=0,
        verbose_name='Botellones llenos',
        help_text='Botellones llenos a entregar en esta parada.'
    )
    envases_retirados = models.PositiveIntegerField(
        default=0,
        verbose_name='Envases retirados',
        help_text='Bidones vacíos devueltos por el cliente.'
    )
    envases_vendidos  = models.PositiveIntegerField(
        default=0,
        verbose_name='Envases vendidos',
        help_text='Envases no devueltos que se cobran al cliente.'
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


# ────────────────────────────────────────────────
# 7. CARGA DE LA HOJA DE RUTA (salida / regreso)
# ────────────────────────────────────────────────
class CargaHojaRuta(models.Model):
    id_carga           = models.AutoField(primary_key=True)
    hoja_ruta          = models.ForeignKey(
        HojaRuta,
        on_delete=models.CASCADE,
        related_name='cargas'
    )
    producto           = models.ForeignKey(
        'productos.Producto',
        on_delete=models.PROTECT,
        related_name='cargas_ruta'
    )
    cantidad_cargada   = models.PositiveIntegerField(default=0)
    cantidad_entregada = models.PositiveIntegerField(default=0)
    cantidad_retornada = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Carga de Hoja de Ruta'
        verbose_name_plural = 'Cargas de Hojas de Ruta'

    def __str__(self):
        return f"Hoja #{self.hoja_ruta_id} · {self.producto} (cargados: {self.cantidad_cargada})"
