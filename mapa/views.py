from django.views import generic

from .models import Direccion
from organizaciones.models import Organizacion, Veterinario, Clinica

# Create your views here.

""" esto seria para crear la direccion """
class MapaList(generic.ListView):
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
