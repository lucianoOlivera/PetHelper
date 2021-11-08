from django.contrib.auth.models import User
from django.views import generic

from .models import Direccion
from organizaciones.models import Organizacion, Veterinario, Clinica
from django.contrib.auth.mixins import PermissionRequiredMixin
from bases.views import SinPrivilegios

# Create your views here.
""" esto seria para crear la direccion """
class MapaList(SinPrivilegios, generic.ListView):
    permission_required = "mapa.view_direccion"
    model = Direccion
    template_name = 'mapa/mapa.html'
    login_url = 'bases/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['direcciones'] = Direccion.objects.all()
        context['organizaciones'] = Organizacion.objects.all()
        context['veterinarios'] = Veterinario.objects.all()
        context['clinicas'] = Clinica.objects.all()
        return context

class MapaVeterinariosList(generic.ListView):
    model = Direccion
    template_name = 'mapa/mapa_veterinarios.html'
    login_url = 'bases/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coordenadas'] = []
        veterinarios = Veterinario.objects.all()
        coordenadas = Direccion.objects.all()
        for coordenada in coordenadas:
            for veterinario in veterinarios:
                if coordenada.direccion == veterinario.direccion:
                    context['coordenadas'].append(coordenada)
                    # context['veterinario'].append(veterinario)
                    return context


class MapaClinicasList(generic.ListView):
    model = Direccion
    template_name = 'mapa/mapa_clinicas.html'
    login_url = 'bases/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coordenadas'] = []
        clinicas = Clinica.objects.all()
        coordenadas = Direccion.objects.all()
        for coordenada in coordenadas:
            for clinica in clinicas:
                if coordenada.direccion == clinica.direccion:
                    context['coordenadas'].append(coordenada)
                    # context['veterinario'].append(veterinario)
                    return context


class MapaOrganizacionesList(generic.ListView):
    model = Direccion
    template_name = 'mapa/mapa_organizaciones.html'
    login_url = 'bases/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coordenadas'] = []
        organizaciones = Organizacion.objects.all()
        coordenadas = Direccion.objects.all()
        for coordenada in coordenadas:
            for organizacion in organizaciones:
                if coordenada.direccion == organizacion.direccion:
                    context['coordenadas'].append(coordenada)
                    # context['veterinario'].append(veterinario)
                    return context
