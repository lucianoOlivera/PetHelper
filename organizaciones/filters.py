import django_filters
from .models import Veterinario, Clinica,Organizacion


class VeterinarioFilter(django_filters.FilterSet):
    class Meta:
        model = Veterinario
        fields = ['direccion', 'dia_desde', 'dia_hasta', 'hora_desde', 'hora_hasta']


class ClinicaFilter(django_filters.FilterSet):
    class Meta:
        model = Clinica
        fields = ['direccion', 'dia_desde', 'dia_hasta', 'hora_desde', 'hora_hasta']


class OrganizacionFilter(django_filters.FilterSet):
    class Meta:
        model = Organizacion
        fields = ['direccion', 'dia_desde', 'dia_hasta', 'hora_desde', 'hora_hasta']
