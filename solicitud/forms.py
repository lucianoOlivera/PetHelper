from django import forms
from .models import Solicitud_Donacion_Insumo, Solicitud_Donacion_Monetaria

class SolicitudDonacionInsumoForm(forms.ModelForm):
    class Meta:
        model = Solicitud_Donacion_Insumo
        fields = ['titulo', 'pedido', 'veterinario']

        def __init__(self, *arg, **kwargs):
            super().__init__(*arg, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })


class SolicitudDonacionMonetariaForm(forms.ModelForm):
    class Meta:
        model = Solicitud_Donacion_Monetaria
        fields = ['titulo', 'monto', 'pedido', 'veterinario']

        def __init__(self, *arg, **kwargs):
            super().__init__(*arg, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })