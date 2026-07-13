from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email','password1', 'password2','celular1','celular2', 'imagen_perfil')

class IngresarUsuarioForm(forms.Form):
   username = forms.CharField(label='Nombre de usuario', max_length=150)
   password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)