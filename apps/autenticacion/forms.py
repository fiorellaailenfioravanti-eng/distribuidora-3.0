from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email','password1', 'password2','celular1','celular2', 'imagen_perfil')

class IngresarUsuarioForm(forms.Form):
    username = forms.CharField(
        label='Nombre de usuario', 
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control rounded-3 py-2 px-3'})
    )
    password = forms.CharField(
        label='Contraseña', 
        widget=forms.PasswordInput(attrs={'class': 'form-control rounded-3 py-2 px-3'})
    )