from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

from mapa.models import Direccion

from .models import Organizacion, Clinica, Veterinario 
from .forms import OrganizacionForm, ClinicaForm, VeterinarioForm
from .filters import OrganizacionFilter, VeterinarioFilter, ClinicaFilter
# Create your views here.


class OrganizacionView(generic.ListView):
    model = Organizacion
    template_name = "organizaciones/org_list.html"
    context_object_name = "obj"
    login_url = 'bases/login.html'


class OrganizacionDetail(generic.DetailView):
    model = Organizacion
    template_name = "organizaciones/org_perfil.html"
    context_object_name = "obj"
    login_url = 'bases/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coordenadas'] = Direccion.objects.get(direccion=self.object.direccion)
        return context


class OrganizacionNew(SuccessMessageMixin, generic.CreateView):
    model = Organizacion
    template_name = 'organizaciones/org_form.html'
    context_object_name = "obj"
    form_class = OrganizacionForm
    success_url = reverse_lazy('organizaciones:organizaciones_list')
    success_message = "Organizacion creada sastifactoriamente"

    def form_valid (self, form):
        form.instance.uc = self.request.user
        organizacion = form.instance
        Direccion.objects.get_or_create(direccion=organizacion.direccion)
        return super().form_valid(form)

class OrganizacionDel(SuccessMessageMixin, generic.DeleteView):
    model = Organizacion
    template_name = 'organizaciones/org_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('organizaciones:organizaciones_list')
    success_message = "Organizacion eliminada sastifactoriamente"


class OrganizacionEdit(SuccessMessageMixin,generic.UpdateView):
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


class ClinicaDetail(generic.DetailView):
    model = Clinica
    template_name = "organizaciones/cli_perfil.html"
    context_object_name = "obj"
    login_url = 'bases/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coordenadas'] = Direccion.objects.get(direccion=self.object.direccion)
        return context


class ClinicaNew(SuccessMessageMixin, generic.CreateView):
    model = Clinica
    template_name = 'organizaciones/cli_form.html'
    context_object_name = "obj"
    form_class = ClinicaForm
    success_url = reverse_lazy('organizaciones:clinicas_list')
    success_message = "Clinica creada sastifactoriamente"

    def form_valid (self, form):
        form.instance.uc = self.request.user
        clinica = form.instance
        Direccion.objects.get_or_create(direccion=clinica.direccion)
        return super().form_valid(form)


class ClinicaDel(SuccessMessageMixin, generic.DeleteView):
    model = Clinica
    template_name = 'organizaciones/cli_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('organizaciones:clinicas_list')
    success_message = "Clínica eliminada sastifactoriamente"


class ClinicaEdit(SuccessMessageMixin, generic.UpdateView):
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


class VeterinarioDetail(generic.DetailView):
    model = Veterinario
    template_name = "organizaciones/vet_perfil.html"
    context_object_name = "obj"
    login_url = 'bases/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coordenadas'] = Direccion.objects.get(direccion=self.object.direccion)
        return context


class VeterinarioNew(SuccessMessageMixin, generic.CreateView):
    model = Veterinario
    template_name = 'organizaciones/vet_form.html'
    context_object_name = "obj"
    form_class = VeterinarioForm
    success_url = reverse_lazy('organizaciones:veterinarios_list')
    success_message = "Veterinario creado sastifactoriamente"

    def form_valid (self, form):
        form.instance.uc = self.request.user
        veterinario = form.instance
        Direccion.objects.get_or_create(direccion=veterinario.direccion)
        return super().form_valid(form)



class VeterinarioDel(SuccessMessageMixin, generic.DeleteView):
    model = Veterinario
    template_name = 'organizaciones/vet_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('organizaciones:veterinarios_list')
    success_message = "Veterinario eliminado sastifactoriamente"

class VeterinarioEdit(SuccessMessageMixin, generic.UpdateView):
    model = Veterinario
    template_name = 'organizaciones/vet_modal_editar.html'
    context_object_name = "obj"
    form_class = VeterinarioForm
    success_url = reverse_lazy('organizaciones:veterinarios_list')
    success_message = "Veterinario editado sastifactoriamente"

    def form_valid (self, form):
        form.instance.um = self.request.user.id
        veterinario = form.instance
        Direccion.objects.get_or_create(direccion=veterinario.direccion)
        return super().form_valid(form)


class VeterinarioClinicaView(TemplateView):
    template_name = 'organizaciones/profesionales_list.html'
    context_object_name = 'profesionales'
    login_url = 'bases/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['veterinarios'] = Veterinario.objects.all()
        context['clinicas'] = Clinica.objects.all()
        context['total_veterinarios'] = Veterinario.objects.all().count
        context['total_clinicas'] = Clinica.objects.all().count
        return context


class VeterinarioFilterView(generic.ListView):
    model = Veterinario
    template_name = 'organizaciones/filter_veterinario.html'
    login_url = 'bases/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        veterinarios = Veterinario.objects.all()
        context['total_veterinarios'] = Veterinario.objects.all().count
        context['total_clinicas'] = 0
        context['myFilter'] = VeterinarioFilter(self.request.GET, queryset=veterinarios)
        context['veterinarios'] = context['myFilter'].qs
        return context


class ClinicaFilterView(generic.ListView):
    model = Veterinario
    template_name = 'organizaciones/filter_clinica.html'
    login_url = 'bases/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        clinicas = Clinica.objects.all()
        context['total_clinicas'] = Clinica.objects.all().count
        context['total_veterinarios'] = 0
        context['myFilter'] = ClinicaFilter(self.request.GET, queryset=clinicas)
        context['clinicas'] = context['myFilter'].qs
        return context


class OrganizacionListView(TemplateView):
    model = Organizacion
    template_name = "organizaciones/organizaciones_list.html"
    context_object_name = 'organizaciones'
    login_url = 'bases/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organizaciones = Organizacion.objects.all()
        context['organizaciones'] = Organizacion.objects.all()
        context['total_organizaciones'] = Organizacion.objects.all().count
        context['myFilter'] = OrganizacionFilter(self.request.GET, queryset=organizaciones)
        context['organizaciones'] = context['myFilter'].qs
        return context


# class OrganizacionFilterView(generic.ListView):
#     model = Organizacion
#     template_name = 'organizaciones/filter_organizacion.html'
#     login_url = 'bases/login.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         organizaciones = Organizacion.objects.all()
#         context['organizaciones'] = Organizacion.objects.all()
#         context['total_organizaciones'] = Organizacion.objects.all().count
#         context['myFilter'] = OrganizacionFilter(self.request.GET, queryset=organizaciones)
#         context['organizaciones'] = context['myFilter'].qs
#         return context
