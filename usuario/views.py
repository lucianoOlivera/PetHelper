from .models import Usuario
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import UserRegisterForm


class RegistroUsuario(FormView):
    model = Usuario
    template_name = "bases/registracion.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy('bases:home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
