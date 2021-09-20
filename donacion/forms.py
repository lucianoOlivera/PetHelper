from django import forms
from .models import Solicitud_Donacion_Monetaria, Solicitud_Donacion_Insumo


class SolicitudDonacionMonetariaForm(forms.ModelForm):
    class Meta:
        model = Solicitud_Donacion_Monetaria
        fields = ['titulo', 'tipo_donacion', 'descripcion', 'monto', 'fecha']

        def __init__(self, *arg, **kwargs):
            super().__init__(*arg, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })


class SolicitudDonacionInsumoForm(forms.ModelForm):
    class Meta:
        model = Solicitud_Donacion_Insumo
        fields = ['titulo', 'tipo_donacion', 'descripcion', 'fecha']

        def __init__(self, *arg, **kwargs):
            super().__init__(*arg, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })