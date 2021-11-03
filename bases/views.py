from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from organizaciones.models import Veterinario, Organizacion, Clinica


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url = 'bases:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['veterinarios'] = Veterinario.objects.all()
        context['clinicas'] = Clinica.objects.all()
        context['organizaciones'] = Organizacion.objects.all()
        return context
        

