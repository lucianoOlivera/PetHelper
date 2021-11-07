from django import forms
from .models import Donacion_Insumo, Donacion_monetaria, Medio_Pago, Estado_Donacion_Monetaria, Estado_Donacion_Insumo
from captcha.fields import ReCaptchaField 

class ReCaptcha(forms.Form):
    captcha = ReCaptchaField()


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


class EstadoDonacionMonetariaForm(forms.ModelForm):
    class Meta:
        model = Estado_Donacion_Monetaria
        fields = ['nombre']

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class EstadoDonacionInsumoForm(forms.ModelForm):
    class Meta:
        model = Estado_Donacion_Insumo
        fields = ['nombre']

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })