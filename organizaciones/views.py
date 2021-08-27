from django.shortcuts import render
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import Organizacion, Clinica, Veterinario 
from .forms import OrganizacionForm, ClinicaForm, VeterinarioForm
# Create your views here.

class OrganizacionView(generic.ListView):
    model = Organizacion
    template_name = "organizaciones/org_list.html"
    context_object_name = "obj"
    login_url = 'bases/login.html'


class OrganizacionNew(SuccessMessageMixin, generic.CreateView):
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
    template_name = 'organizaciones/org_modal_editar.html'
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
    success_url = reverse_lazy('organizaciones:clinicas_list')
    success_message = "Clinica creada sastifactoriamente"

    def form_valid (self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class ClinicaDel(generic.DeleteView):
    model = Clinica
    template_name = 'organizaciones/cli_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('organizaciones:clinicas_list')


class ClinicaEdit(generic.UpdateView):
    model = Clinica
    template_name = 'organizaciones/cli_modal_editar.html'
    context_object_name = "obj"
    form_class = ClinicaForm
    success_url = reverse_lazy('organizaciones:clinicas_list')
    success_message = "Clinica editada sastifactoriamente"

    def form_valid (self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class VeterinarioView(generic.ListView):
    model = Veterinario
    template_name = "organizaciones/vet_list.html"
    context_object_name = "obj"
    login_url = 'bases/login.html'


class VeterinarioNew(SuccessMessageMixin,generic.CreateView):
    model = Veterinario
    template_name = 'organizaciones/vet_form.html'
    context_object_name = "obj"
    form_class = VeterinarioForm
    success_url = reverse_lazy('organizaciones:veterinarios_list')
    success_message = "Veterinario creado sastifactoriamente"

    def form_valid (self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class VeterinarioDel(generic.DeleteView):
    model = Veterinario
    template_name = 'organizaciones/vet_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('organizaciones:veterinarios_list')

class VeterinarioEdit(generic.UpdateView):
    model = Veterinario
    template_name = 'organizaciones/vet_modal_editar.html'
    context_object_name = "obj"
    form_class = VeterinarioForm
    success_url = reverse_lazy('organizaciones:veterinarios_list')
    success_message = "Veterinario editado sastifactoriamente"

    def form_valid (self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

