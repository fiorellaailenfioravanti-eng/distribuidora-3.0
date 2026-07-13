from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    imagen_perfil = models.ImageField(upload_to='perfiles/', null=True, blank=True,default='usuarios/default.jpg')
    email = models.EmailField(unique=True)
    celular1 = models.CharField(max_length=20, null=True, blank=True)
    celular2 = models.CharField(max_length=20, null=True, blank=True)
    
    def get_absolute_url(self):

        return reverse('inicio')
    