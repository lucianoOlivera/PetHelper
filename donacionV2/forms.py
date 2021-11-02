from django import forms
from .models import Donacion_Insumo, Donacion_monetaria, Medio_Pago


class DonacionInsumoForm(forms.ModelForm):
    class Meta:
        model = Donacion_Insumo
        fields = '__all__'

        def __init__(self, *arg, **kwargs):
            super().__init__(*arg, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })


class DonacionMonetariaForm(forms.ModelForm):
    class Meta:
        model = Donacion_monetaria
        fields = ['monto']

        def __init__(self, *arg, **kwargs):
            super().__init__(*arg, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })


class FormaDePagoForm(forms.ModelForm):
    class Meta:
        model = Medio_Pago
        fields = ['nombre_pago', 'imagen']

        def __init__(self, *arg, **kwargs):
            super().__init__(*arg, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })