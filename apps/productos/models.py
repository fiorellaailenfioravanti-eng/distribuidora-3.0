from django.db import models
from distribuidora.limites import LARGO_NOMBRE, LARGO_TEXTO, limite_largo

# Create your models here.

class VigentesQuerySet(models.QuerySet):
    def vigentes(self):
        """Sin las eliminadas (baja lógica)."""
        return self.filter(eliminada=False)


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=LARGO_NOMBRE)
    descripcion = models.TextField(max_length=LARGO_TEXTO)
    eliminada = models.BooleanField(
        default=False, verbose_name='Eliminada',
        help_text='Baja lógica: no aparece en la tienda ni para elegir; sus productos no cambian.')

    objects = VigentesQuerySet.as_manager()

    class Meta:
        constraints = limite_largo(nombre=LARGO_NOMBRE, descripcion=LARGO_TEXTO)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=LARGO_NOMBRE)
    descripcion = models.TextField(max_length=LARGO_TEXTO)
    categoria= models.ManyToManyField(Categoria)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    es_envase = models.BooleanField(
        default=False,
        verbose_name='Es envase',
        help_text='Marca el producto que representa al bidón vacío (envase retornable).'
    )
    es_botellon = models.BooleanField(
        default=False,
        verbose_name='Botellón lleno de reparto',
        help_text='Bidón lleno que se carga en el camión y se entrega en las paradas. '
                  'Por ahora el reparto sólo maneja botellones llenos y envases vacíos.'
    )
    es_recargable = models.BooleanField(
        default=False,
        verbose_name='Se recarga en planta',
        help_text='Bidón que el recargador llena en la planta: suma stock lleno y descuenta su envase vacío.'
    )
    es_retornable = models.BooleanField(
        default=False,
        verbose_name='Es retornable',
        help_text='Producto cuyo envase se retira al momento de entregar.'
    )
    activo = models.BooleanField(
        default=True,
        verbose_name='Activo',
        help_text='Los productos inactivos no se muestran en la tienda ni se pueden comprar. '
                  'Se usa en lugar de borrar un producto que ya tiene pedidos.'
    )
    envase = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='productos_que_lo_usan',
        verbose_name='Envase asociado',
        help_text='Envase que debe retirarse al entregar este producto.'
    )

    class Meta:
        constraints = limite_largo(nombre=LARGO_NOMBRE, descripcion=LARGO_TEXTO)

    def __str__(self):
        return self.nombre

