from django import forms
from .models import Solicitud_Donacion_Monetaria, Solicitud_Donacion_Insumo, Donacion_Monetaria, Donacion_Insumo, Cantidad_Insumo


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


class CantidadInsumoForm(forms.ModelForm):
    class Meta:
        model = Cantidad_Insumo
        fields = ['cantidad', 'insumo']

        def __init__(self, *arg, **kwargs):
            super().__init__(*arg, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })


class DonacionMonetariaForm(forms.ModelForm):
    class Meta:
        model = Donacion_Monetaria
        fields = ['monto']

        def __init__(self, *arg, **kwargs):
            super().__init__(*arg, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })


class DonacionInsumoForm(forms.ModelForm):
    class Meta:
        model = Donacion_Insumo
        fields = ['monto']

        def __init__(self, *arg, **kwargs):
            super().__init__(*arg, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })