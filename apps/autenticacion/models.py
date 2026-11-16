from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from distribuidora.limites import LARGO_NOMBRE, LARGO_TEXTO, limite_largo

# Create your models here.

class Usuario(AbstractUser):
    imagen_perfil = models.ImageField(upload_to='perfiles/', null=True, blank=True,default='usuarios/default.jpg')
    first_name = models.CharField('nombre', max_length=LARGO_NOMBRE, blank=True)
    last_name = models.CharField('apellido', max_length=LARGO_NOMBRE, blank=True)
    email = models.EmailField(unique=True)
    celular1 = models.CharField(max_length=20, null=True, blank=True)
    celular2 = models.CharField(max_length=20, null=True, blank=True)
    
    class Meta(AbstractUser.Meta):
        constraints = limite_largo(first_name=LARGO_NOMBRE, last_name=LARGO_NOMBRE, celular1=20, celular2=20)

    def get_absolute_url(self):

        return reverse('inicio')
    

class CodigoRecuperacion(models.Model):
    """Código temporal de 6 dígitos para recuperar la contraseña.

    Nunca se guarda el código en claro: sólo su HMAC (ver `recuperacion.py`).
    Vence a los pocos minutos, admite pocos intentos y sirve una sola vez.
    """
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='codigos_recuperacion')
    codigo_hash = models.CharField(max_length=64)
    creado = models.DateTimeField(auto_now_add=True)
    vence = models.DateTimeField()
    intentos = models.PositiveSmallIntegerField(default=0)
    verificado_en = models.DateTimeField(null=True, blank=True)
    usado = models.BooleanField(default=False)

    class Meta:
        ordering = ['-creado']
        verbose_name = 'Código de recuperación'
        verbose_name_plural = 'Códigos de recuperación'

    def __str__(self):
        return f'Código de {self.usuario} ({self.creado:%d/%m/%Y %H:%M})'
