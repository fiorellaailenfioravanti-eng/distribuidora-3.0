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


class EnvaseForm(forms.Form):
    """Mini alta de un envase vacío (producto `es_envase`) y su asociación a los bidones."""
    nombre = forms.CharField(
        max_length=Producto._meta.get_field('nombre').max_length, label='Nombre del envase',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Envase bidón 20 L'}))
    precio = forms.DecimalField(
        max_digits=10, decimal_places=2, label='Precio del envase ($)',
        help_text='Lo que se cobra si el cliente se queda con el envase.',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0.01', 'step': '0.01',
                                        'inputmode': 'decimal', 'placeholder': '0.00'}))
    stock = forms.IntegerField(
        min_value=0, max_value=100000, initial=0, label='Envases vacíos en depósito',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '1',
                                        'inputmode': 'numeric'}))
    bidones = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.none(), required=False, label='Bidones que usan este envase',
        help_text='Los bidones marcados pasan a usar este envase (reemplaza el que tuvieran).',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bidones'].queryset = bidones_retornables()

    def clean_nombre(self):
        nombre = ' '.join((self.cleaned_data.get('nombre') or '').split())
        if Producto.objects.filter(es_envase=True, nombre__iexact=nombre).exists():
            raise forms.ValidationError('Ya existe un envase con ese nombre.')
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor a cero.')
        return precio

    def save(self):
        """Crea el envase en la categoría «Envases» y lo asocia a los bidones elegidos."""
        from django.db import transaction
        datos = self.cleaned_data
        with transaction.atomic():
            categoria = (Categoria.objects.vigentes().filter(nombre__iexact='Envases').first()
                         or Categoria.objects.create(
                             nombre='Envases',
                             descripcion='Envases retornables que se prestan con cada entrega.'))
            envase = Producto.objects.create(
                nombre=datos['nombre'], precio=datos['precio'], stock=datos['stock'],
                descripcion='Bidón retornable vacío, sin contenido.',
                es_envase=True, es_retornable=True, activo=True)
            envase.categoria.add(categoria)
            Producto.objects.filter(pk__in=[b.pk for b in datos['bidones']]).update(envase=envase)
        return envase


def bidones_retornables():
    """Bidones que se reparten o se recargan en planta (los que necesitan un envase)."""
    from django.db.models import Q
    return (Producto.objects.filter(Q(es_botellon=True) | Q(es_recargable=True), es_envase=False)
            .select_related('envase').order_by('nombre'))
