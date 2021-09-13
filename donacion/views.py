from django.shortcuts import render
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import Solicitud_Donacion_Monetaria, Solicitud_Donacion_Insumo
from .forms import SolicitudDonacionMonetariaForm, SolicitudDonacionInsumoForm


class SolicitudDonacionMonetariaView(generic.ListView):
    model = Solicitud_Donacion_Monetaria
    template_name = 'donacion/solicitudes_list.html'
    context_object_name = "obj"
    login_url = 'bases/login.html'


class SolicitudDonacionMonetariaNew(SuccessMessageMixin, generic.CreateView):
    model = Solicitud_Donacion_Monetaria
    template_name = 'donacion/solicitud_monetaria_form.html'
    context_object_name = "obj"
    form_class = SolicitudDonacionMonetariaForm
    success_url = reverse_lazy('donacion:solicitudes_list')
    success_message = "Solicitud creada sastifactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class SolicitudDonacionMonetariaDel(SuccessMessageMixin, generic.DeleteView):
    model = Solicitud_Donacion_Monetaria
    template_name = 'donacion/solicitud_monetaria_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('donacion:solicitudes_list')
    success_message = "Solicitud eliminada sastifactoriamente"


class SolicitudDonacionMonetariaEdit(SuccessMessageMixin, generic.UpdateView):
    model = Solicitud_Donacion_Monetaria
    template_name = 'organizaciones/solicitud_monetaria_modal_editar.html'
    context_object_name = "obj"
    form_class = SolicitudDonacionMonetariaForm
    success_url = reverse_lazy('donacion:solicitudes_list')
    success_message = "Solicitud editada sastifactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form) 


class SolicitudDonacionInsumoView(generic.ListView):
    model = Solicitud_Donacion_Insumo
    template_name = "donacion/solicitudes_list.html"
    context_object_name = "obj"
    login_url = 'bases/login.html'


class SolicitudDonacionInsumoNew(SuccessMessageMixin, generic.CreateView):
    model = Solicitud_Donacion_Insumo
    template_name = 'donacion/solicitud_insumo_form.html'
    context_object_name = "obj"
    form_class = SolicitudDonacionInsumoForm
    success_url = reverse_lazy('donacion:solicitudes_list')
    success_message = "Solicitud creada sastifactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class SolicitudDonacionInsumoDel(SuccessMessageMixin, generic.DeleteView):
    model = Solicitud_Donacion_Insumo
    template_name = 'donacion/solicitud_insumo_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('donacion:solicitudes_list')
    success_message = "Solicitud eliminada sastifactoriamente"


class SolicitudDonacionInsumoEdit(SuccessMessageMixin, generic.UpdateView):
    model = Solicitud_Donacion_Insumo
    template_name = 'organizaciones/solicitud_insumo_modal_editar.html'
    context_object_name = "obj"
    form_class = SolicitudDonacionInsumoForm
    success_url = reverse_lazy('donacion:solicitudes_list')
    success_message = "Solicitud editada sastifactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)     
