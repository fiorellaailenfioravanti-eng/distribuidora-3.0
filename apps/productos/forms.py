from django import forms

from .models import Producto, Categoria


class ProductoForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.vigentes(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True,
        label="Categoría",
        empty_label="-- Seleccionar Categoría --"
    )

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'categoria', 'precio', 'stock', 'imagen', 'activo', 'es_botellon', 'envase']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Botellón 20L'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción detallada...'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00',
                                               'min': '0.01', 'step': '0.01', 'inputmode': 'decimal'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad inicial',
                                              'min': '0', 'step': '1', 'inputmode': 'numeric'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'es_botellon': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'envase': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descripcion'].required = False
        self.fields['envase'].queryset = Producto.objects.filter(es_envase=True).order_by('nombre')
        self.fields['envase'].required = False
        self.fields['envase'].empty_label = '— Sin envase —'
        if self.instance and self.instance.pk:
            cat_actual = self.instance.categoria.first()
            if cat_actual:
                self.fields['categoria'].initial = cat_actual.pk
            # Reparto y recarga se manejan con un solo interruptor («Bidón retornable»).
            self.initial['es_botellon'] = self.instance.es_botellon or self.instance.es_recargable

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor a cero.')
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise forms.ValidationError('El stock no puede ser negativo.')
        return stock

    def clean(self):
        datos = super().clean()
        es_bidon = bool(datos.get('es_botellon'))
        if es_bidon and not datos.get('envase'):
            self.add_error('envase', 'Elegí el envase vacío de este bidón: se retira al entregar y se usa al recargar.')
        # Un bidón retornable se reparte y también se recarga en la planta.
        self.instance.es_recargable = es_bidon
        return datos

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
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Bebidas'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3,
                                                 'placeholder': 'Opcional: qué productos agrupa'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descripcion'].required = False

    def clean_nombre(self):
        nombre = ' '.join((self.cleaned_data.get('nombre') or '').split())
        if Categoria.objects.filter(nombre__iexact=nombre).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Ya existe una categoría con ese nombre.')
        return nombre
