from django.contrib.auth.views import PasswordChangeView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from .models import Usuario
from django.views.generic.edit import FormView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from verify_email.email_handler import send_verification_email
from .forms import  UserRegisterForm, UserEditForm


class RegistroUsuario(FormView):
    model = Usuario
    template_name = "bases/registracion.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy('usuario:verification_mensage')

    def form_valid(self, form):
        inactive_user = send_verification_email(self.request, form)
        """ form.save() """
        return super().form_valid(form)


class VerificarEmailMensage(generic.ListView):
    model = Usuario
    template_name = "bases/verificacion_confirm.html"
    context_object_name = "obj"
    login_url = 'bases/login.html'


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
    # aca deberia llevar al perfil
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


class UsuarioPasswordReset(SuccessMessageMixin, PasswordResetView):
    template_name = 'bases/resetear_contraseña.html'
    form_class = PasswordResetForm
    email_template_name = 'bases/resetear_contraseña_email.html'
    success_url = reverse_lazy('usuario:password_reset_done')
    success_message = "Su contraseña se cambió sastifactoriamente"


class UsuarioPasswordResetDone(SuccessMessageMixin, PasswordResetDoneView):
    template_name = 'bases/resetear_contraseña_done.html'
    success_message = "Su contraseña se cambió sastifactoriamente"


class UsuarioPasswordResetConfirm(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = 'bases/resetear_contraseña_confirm.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('usuario:password_reset_complete')


class UsuarioPasswordResetComplete(SuccessMessageMixin, PasswordResetCompleteView):
    template_name = 'bases/resetear_contraseña_complete.html'
