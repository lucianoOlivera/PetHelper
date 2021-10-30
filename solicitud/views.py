from django.forms import forms
from django.forms.formsets import formset_factory
from django.shortcuts import render
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from .models import Solicitud_Donacion_Insumo
from insumo.forms import CantidadDeInsumo
from .forms import SolicitudDonacionInsumoForm
from insumo.models import Cantidad_Insumo, Insumo
from usuario.models import Usuario
from organizaciones.models import Veterinario
from django.forms.models import inlineformset_factory, modelformset_factory
from django.views.generic.edit import FormView, UpdateView
#  fields=('titulo', 'pedido', 'veterinario',)
InsumoFormset = inlineformset_factory(
   Solicitud_Donacion_Insumo, Cantidad_Insumo, fields=('insumo', 'cantidad', 'solicitud_insumo',)
)

class SolicitudesListView(TemplateView):
    template_name = "solicitud/solicitud_list.html"
    login_url = 'bases/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solicitudes_insumos'] = Solicitud_Donacion_Insumo.objects.all()
        # context['solicitudes_monetarias'] = Solicitud_Donacion_Monetaria.objects.all()
        context['usuario'] = Usuario.objects.get(pk=1) 
        context['cantidades_insumos'] = Cantidad_Insumo.objects.select_related('solicitud_insumo')
        context['insumos'] = Insumo.objects.all()
        return context


class SolicitudDonacionInsumoNew(SuccessMessageMixin, generic.CreateView):
    model = Solicitud_Donacion_Insumo
    template_name = 'solicitud/solicitud_insumo_form.html'
    context_object_name = 'solicitud'
    fields = ['titulo', 'pedido', 'veterinario']
    # form_class = SolicitudDonacionInsumoForm
    # second_form_class = CantidadDeInsumo
    success_url = reverse_lazy('solicitud:solicitudes_list')
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


class AddSolicitud(FormView):
    template_name = 'solicitud/add.html'
    form_class = formset_factory(Solicitud_Donacion_Insumo, extra=3)
    success_url = '.'
    
    def form_valid(self, form): 

        for f in form:
            print(f.cleaned_data['full_name'])
            f.save()

        return super(AddSolicitud, self).form_valid(form)


class AddAsistencia(FormView):
    template_name = 'solicitud/asistencia.html'
    form_class = inlineformset_factory(Solicitud_Donacion_Insumo, Cantidad_Insumo, fields=('insumo', 'cantidad', 'solicitud_insumo',))
    success_url = '/'
    context_object_name = 'solicitud'
    fields = ['titulo', 'pedido', 'veterinario']

    def form_valid(self, form):
        # cuando se trabaja con model formset no es necesario hacer la iteracion
        # este puede guardar de golpe todo el conjunto de formularios
        #
        form.save() 
        return super(AddAsistencia, self).form_valid(form)



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