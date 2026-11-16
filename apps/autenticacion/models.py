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
    