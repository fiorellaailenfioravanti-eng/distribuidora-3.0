from django import forms
from .models import Producto, Categoria
from django.forms import ModelForm
from django.forms import widgets


class ProductoForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True,
        label="Categoría",
        empty_label="-- Seleccionar Categoría --"
    )

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'categoria', 'precio', 'stock', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Botellón 20L'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción detallada...'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad inicial'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            cat_actual = self.instance.categoria.first()
            if cat_actual:
                self.fields['categoria'].initial = cat_actual.pk

    def clean_categoria(self):
        cat = self.cleaned_data.get('categoria')
        if isinstance(cat, Categoria):
            return [cat]
        if isinstance(cat, (list, tuple)):
            return cat
        return []


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Bebidas'})
        }