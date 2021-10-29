from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from .models import Usuario
from django.views.generic.edit import FormView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import  UserRegisterForm, UserEditForm


class RegistroUsuario(FormView):
    model = Usuario
    template_name = "bases/registracion.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy('bases:home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UsuarioDetail(generic.DetailView):
    model = Usuario
    template_name = "bases/usuario_perfil.html"
    context_object_name = "obj"
    login_url = 'bases/login.html'


class UsuarioEdit(SuccessMessageMixin, generic.UpdateView):
    model = Usuario
    template_name = 'bases/usuario_editar.html'
    context_object_name = "obj"
    form_class = UserEditForm
    success_url = reverse_lazy('bases:home')
    success_message = "Su información fue editada sastifactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class UsuarioPasswordEdit(SuccessMessageMixin, PasswordChangeView):
    template_name = 'bases/cambiar_contraseña.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('bases:home')
    success_message = "Su contraseña se cambió sastifactoriamente"