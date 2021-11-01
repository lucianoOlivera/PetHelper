from django import forms
from .models import Donacion_Insumo


class DonacionInsumoForm(forms.ModelForm):
    class Meta:
        model = Donacion_Insumo

        def __init__(self, *arg, **kwargs):
            super().__init__(*arg, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })