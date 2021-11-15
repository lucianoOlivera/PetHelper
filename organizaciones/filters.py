import django_filters
from .models import Veterinario, Clinica, Organizacion
from django_filters import CharFilter


class VeterinarioFilter(django_filters.FilterSet):
    direccion = CharFilter(field_name='direccion', lookup_expr='icontains')

    class Meta:
        model = Veterinario
        fields = ['direccion', 'dia_desde', 'dia_hasta', 'hora_desde', 'hora_hasta']


class ClinicaFilter(django_filters.FilterSet):
    direccion = CharFilter(field_name='direccion', lookup_expr='icontains')

    class Meta:
        model = Clinica
        fields = ['direccion', 'dia_desde', 'dia_hasta', 'hora_desde', 'hora_hasta']


class OrganizacionFilter(django_filters.FilterSet):
    direccion = CharFilter(field_name='direccion', lookup_expr='icontains')

    class Meta:
        model = Organizacion
        fields = ['direccion', 'dia_desde', 'dia_hasta', 'hora_desde', 'hora_hasta']
