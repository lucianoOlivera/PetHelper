

from django import forms
from mapa.models import Direccion


class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['direccion']

        def __init__(self, *arg, **kwargs):
            super().__init__(*arg, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })