from django import forms
from .models import Organizacion

class OrganizacionForm(forms.ModelForm):
    class Meta:
        model = Organizacion
        fields = ['nombre', 'cuit', 'email', 'logo']
        labels = {'descripcion': 'Descripcion de la organizacion'}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
