from django import forms
from .models import Producto, Categoria
from django.forms import ModelForm
from django.forms import widgets


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),

        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Bebidas'})
        }