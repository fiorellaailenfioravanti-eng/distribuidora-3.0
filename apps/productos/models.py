from django.db import models

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
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

    def __str__(self):
        return self.nombre

