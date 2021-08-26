from django.shortcuts import render
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import Organizacion, Clinica, Veterinario 
from .forms import OrganizacionForm, ClinicaForm
# Create your views here.

class OrganizacionView(generic.ListView):
    model = Organizacion
    template_name = "organizaciones/org_list.html"
    context_object_name = "obj"
    login_url = 'bases/login.html'


class OrganizacionNew(SuccessMessageMixin,generic.CreateView):
    model = Organizacion
    template_name = 'organizaciones/org_form.html'
    context_object_name = "obj"
    form_class = OrganizacionForm
    success_url = reverse_lazy('organizaciones:organizaciones_list')
    success_message = "Organizacion creada sastifactoriamente"

    def form_valid (self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class OrganizacionDel(generic.DeleteView):
    model = Organizacion
    template_name = 'organizaciones/org_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('organizaciones:organizaciones_list')

class OrganizacionEdit(generic.UpdateView):
    model = Organizacion
    template_name = 'organizaciones/org_form.html'
    context_object_name = "obj"
    form_class = OrganizacionForm
    success_url = reverse_lazy('organizaciones:organizaciones_list')
    success_message = "Organizacion editada sastifactoriamente"

    def form_valid (self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class ClinicaView(generic.ListView):
    model = Clinica
    template_name = "organizaciones/cli_list.html"
    context_object_name = "obj"
    login_url = 'bases/login.html'

class ClinicaNew(SuccessMessageMixin,generic.CreateView):
    model = Clinica
    template_name = 'organizaciones/cli_form.html'
    context_object_name = "obj"
    form_class = ClinicaForm
    success_url = reverse_lazy('clinicas:clinicas_list')
    success_message = "Clinica creada sastifactoriamente"

    def form_valid (self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class ClinicaDel(generic.DeleteView):
    model = Clinica
    template_name = 'organizaciones/cli_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('clinicas:clinicas_list')

class ClinicaEdit(generic.UpdateView):
    model = Clinica
    template_name = 'organizaciones/cli_form.html'
    context_object_name = "obj"
    form_class = ClinicaForm
    success_url = reverse_lazy('clinicas:clinicas_list')
    success_message = "Clinica editada sastifactoriamente"

    def form_valid (self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


