from django.shortcuts import render
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from .models import Solicitud_Donacion_Insumo
from .forms import SolicitudDonacionInsumoForm
from insumo.models import Cantidad_Insumo
from usuario.models import Usuario
from organizaciones.models import Veterinario
from django.forms.models import inlineformset_factory
#  fields=('titulo', 'pedido', 'veterinario',)
InsumoFormset = inlineformset_factory(
   Solicitud_Donacion_Insumo, Cantidad_Insumo, fields=('insumo', 'cantidad', 'solicitud_insumo',)
)

class SolicitudDonacionInsumoView(generic.ListView):
    model = Solicitud_Donacion_Insumo
    template_name = "solicitud/solicitud_insumo_list.html"
    context_object_name = 'solicitud'
    login_url = 'bases/login.html'


class SolicitudDonacionInsumoNew(SuccessMessageMixin, generic.CreateView):
    model = Solicitud_Donacion_Insumo
    template_name = 'solicitud/solicitud_insumo_form.html'
    context_object_name = 'solicitud'
    fields = '__all__'
    # form_class = SolicitudDonacionInsumoForm
    # second_form_class = CantidadDeInsumo
    success_url = reverse_lazy('donacion:solicitudes_list')
    success_message = "Solicitud creada sastifactoriamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['Insumo'] = InsumoFormset(self.request.POST, instance=self.object)
        else:
            context['Insumo'] = InsumoFormset(instance=self.object)
        return context
 
    def form_valid(self, form):
        form.instance.uc = self.request.user
        context = self.get_context_data()
        Insumo = context["Insumo"]
        self.object = form.save()
        if Insumo.is_valid():
            Insumo.instance = self.object
            Insumo.save()
        return super().form_valid(form)


# class SolicitudDonacionInsumoDel(SuccessMessageMixin, generic.DeleteView):
#     model = Solicitud_Donacion_Insumo
#     template_name = 'donacion/solicitud_insumo_del.html'
#     context_object_name = 'solicitudes_insumos'
#     success_url = reverse_lazy('donacion:solicitudes_list')
#     success_message = "Solicitud eliminada sastifactoriamente"


# class SolicitudDonacionInsumoEdit(SuccessMessageMixin, generic.UpdateView):
#     model = Solicitud_Donacion_Insumo
#     template_name = 'donacion/solicitud_insumo_modal_editar.html'
#     context_object_name = "solicitudes_insumos"
#     form_class = SolicitudDonacionInsumoForm
#     success_url = reverse_lazy('donacion:solicitudes_list')
#     success_message = "Solicitud editada sastifactoriamente"

#     def form_valid(self, form):
#         form.instance.um = self.request.user.id
#         return super().form_valid(form)