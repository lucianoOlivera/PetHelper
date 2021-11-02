from django import forms
from django.db import models
from django.db.models import fields
from .models import Organizacion, Clinica, Veterinario

class OrganizacionForm(forms.ModelForm):
    class Meta:
        model = Organizacion
        fields = ['descripcion', 'nombre', 'direccion','cuit', 'telefono', 'email', 'logo', 'dia_desde', 'dia_hasta', 'hora_desde', 'hora_hasta']
        labels = {'descripcion': 'Descripcion de la organizacion'}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class ClinicaForm(forms.ModelForm):
    class Meta:
        model = Clinica
        fields = ['descripcion','nombre', 'direccion','cuit', 'email', 'logo', 'telefono' , 'whatsapp', 'dia_desde', 'dia_hasta', 'hora_desde', 'hora_hasta']
        labels = {'descripcion': 'Descripcion de clinica'}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class VeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = ['descripcion','nombre', 'direccion','apellido','matricula', 'email', 'logo', 'whatsapp', 'dia_desde', 'dia_hasta', 'hora_desde', 'hora_hasta']
        labels = {'descripcion': 'Descripcion de veterinario'}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            }) 