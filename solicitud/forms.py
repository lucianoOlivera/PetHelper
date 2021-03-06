from django import forms
from captcha.fields import ReCaptchaField 
from .models import Solicitud_Donacion_Insumo, Solicitud_Donacion_Monetaria, Estado_Solicitud_Monetaria, Estado_Solicitud_Insumo

class ReCaptcha(forms.Form):
    captcha = ReCaptchaField()

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
        fields = ['titulo', 'monto', 'pedido', 'veterinario', 'cbu', 'nombre_titular', 'alias', 'nombre_banco']

        def __init__(self, *arg, **kwargs):
            super().__init__(*arg, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })


class EstadoSolicitudMonetariaForm(forms.ModelForm):
    class Meta:
        model = Estado_Solicitud_Monetaria
        fields = ['nombre']

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class EstadoSolicitudInsumoForm(forms.ModelForm):
    class Meta:
        model = Estado_Solicitud_Insumo
        fields = ['nombre']

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
