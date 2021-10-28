from django.views import generic
from django.urls import reverse_lazy

from .models import Direccion

# Create your views here.

""" esto seria para crear la direccion """
class MapaList(generic.CreateView):
    model = Direccion
    fields = ['direccion']
    template_name = 'mapa/mapa.html'
    success_url = reverse_lazy('usuario:usuario_profile')
    login_url = 'bases/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['direcciones'] = Direccion.objects.all()
        return context
