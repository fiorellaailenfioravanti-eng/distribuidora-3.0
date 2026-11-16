from django import forms

from .models import ConfiguracionCorreo


class ConfiguracionCorreoForm(forms.ModelForm):
    clave = forms.CharField(
        label='Contraseña de aplicación', required=False, max_length=128,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'},
                                   render_value=False),
        help_text='En Gmail se crea en la cuenta de Google → Seguridad → «Contraseñas de aplicaciones» '
                  '(16 letras). Dejala vacía para mantener la que ya está guardada.',
    )

    class Meta:
        model = ConfiguracionCorreo
        fields = ['activo', 'nombre_remitente', 'correo_remitente', 'servidor', 'puerto',
                  'usar_tls', 'usuario', 'clave']
        widgets = {
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input', 'role': 'switch'}),
            'usar_tls': forms.CheckboxInput(attrs={'class': 'form-check-input', 'role': 'switch'}),
            'nombre_remitente': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_remitente': forms.EmailInput(attrs={'class': 'form-control',
                                                        'placeholder': 'aguadelluvia@gmail.com'}),
            'servidor': forms.TextInput(attrs={'class': 'form-control'}),
            'puerto': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 65535}),
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Igual al correo'}),
        }

    def clean_puerto(self):
        puerto = self.cleaned_data.get('puerto')
        if puerto is not None and not 1 <= puerto <= 65535:
            raise forms.ValidationError('El puerto debe estar entre 1 y 65535.')
        return puerto

    def clean_clave(self):
        # Gmail la muestra en grupos de 4 con espacios: se guardan sin espacios.
        clave = (self.cleaned_data.get('clave') or '').replace(' ', '')
        return clave or self.instance.clave  # vacía = conservar la guardada

    def clean(self):
        datos = super().clean()
        if datos.get('activo'):
            if not datos.get('correo_remitente'):
                self.add_error('correo_remitente', 'Indicá el correo que va a enviar los emails.')
            if not datos.get('clave'):
                self.add_error('clave', 'Falta la contraseña de aplicación de esa cuenta.')
        return datos
