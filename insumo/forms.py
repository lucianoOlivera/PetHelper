from django import forms
from .models import Cantidad_Insumo, Insumo


class CantidadDeInsumo(forms.ModelForm):
    class Meta:
        modal = Cantidad_Insumo
        fields = ['cantidad', 'insumo']

        def __init__(self, *arg, **kwargs):
            super().__init__(*arg, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })


class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['nombre']

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
