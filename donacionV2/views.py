from django.contrib.messages.views import SuccessMessageMixin
from django.forms.models import inlineformset_factory
from django.http import request
from donacionV2.models import Donacion_Insumo, Cantidad_Insumo_Donacion
from django.urls import reverse_lazy
from django.views import generic
from solicitud.models import Solicitud_Donacion_Insumo
from insumo.models import Cantidad_Insumo
from django import forms
from django.contrib import messages
from django.shortcuts import render

# Create your views here.
DonacionFormset = inlineformset_factory(
   Donacion_Insumo, Cantidad_Insumo_Donacion, extra=5, fields=('insumo', 'cantidad',))


class DonacionInsumoNew(SuccessMessageMixin, generic.CreateView):
    model = Donacion_Insumo
    template_name = 'donacionV2/donacion_insumo_form.html'
    fields = []
    context_object_name = 'Donacion'
    success_url = reverse_lazy('solicitud:solicitud_list')
    success_message = "Tu donación ha sido procesada con éxito"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['idSolicitud_insumo'] = self.kwargs['pk'] 
        if self.request.POST:
            context['Donacion'] = DonacionFormset(self.request.POST, instance=self.object)
        else:
            context['Donacion'] = DonacionFormset(instance=self.object)
        return context

    def form_valid(self, form):
        form.instance.uc = self.request.user
        context = self.get_context_data()
        SolicitudDonacionInsumo = Solicitud_Donacion_Insumo.objects.get(id=context['idSolicitud_insumo'])
        form.instance.solicitud_insumo = SolicitudDonacionInsumo
        Donacion = context["Donacion"]
        self.object = form.save()
        if Donacion.is_valid():
            Donacion.instance = self.object
            Donacion.save()
        solicitud_insumo_cantidad=[]
        cantidadInsumoSolicitud = Cantidad_Insumo.objects.all()
        for cantidadInsumo in cantidadInsumoSolicitud:
            if cantidadInsumo.solicitud_insumo.id == SolicitudDonacionInsumo.id:
                solicitud_insumo_cantidad.append(cantidadInsumo)    
        cantidadInsumoDonacion = Cantidad_Insumo_Donacion.objects.all()
        for cantidadID in cantidadInsumoDonacion:
            if cantidadID.donacion_isumo.id == form.instance.id:
                for insumosolicitud in solicitud_insumo_cantidad:
                    if cantidadID.insumo == insumosolicitud.insumo:
                        if cantidadID.cantidad <= insumosolicitud.cantidad:
                            cantidadNew=insumosolicitud.cantidad-cantidadID.cantidad
                            Cantidad_Insumo.objects.filter(id=insumosolicitud.id).update(cantidad=cantidadNew)
                            return super().form_valid(form)
                        else:
                            messages.error(self.request, f"la cantidad {cantidadID.cantidad} supera a lo pedido")
                            return render(self.request, 'donacionV2/donacion_insumo_form.html', context)  
