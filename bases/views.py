from django.contrib.auth.models import Group, GroupManager
from django.urls.base import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect

from organizaciones.models import Veterinario, Organizacion, Clinica


class SinPrivilegios(PermissionRequiredMixin):
    raise_exception = False
    redirect_field_name = 'redirect_to'

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user == AnonymousUser:
            self.login_url = 'bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url = 'bases:login'

    def get_context_data(self, **kwargs):
        user = self.request.user
        a = Group.objects.all()
        print(user.get_all_permissions())
        context = super().get_context_data(**kwargs)
        context['veterinarios'] = Veterinario.objects.all()
        context['clinicas'] = Clinica.objects.all()
        context['organizaciones'] = Organizacion.objects.all()
        return context


class HomeSinPrivilegios(generic.TemplateView):
    template_name = "bases/sin_privilegios.html"
