from django.contrib.messages.views import SuccessMessageMixin
from django.forms.models import inlineformset_factory
from django.http import request
from donacionV2.models import Donacion_Insumo, Cantidad_Insumo_Donacion, Donacion_monetaria, Medio_Pago, Estado_Donacion_Insumo,Estado_Donacion_Insumo_Detalle,Estado_Donacion_Monetaria,Estado_Donacion_Monetaria_Detalle
from django.urls import reverse_lazy
from django.views import generic
from solicitud.models import Solicitud_Donacion_Insumo, Solicitud_Donacion_Monetaria
from insumo.models import Cantidad_Insumo
from django.contrib import messages
from django.shortcuts import render
from .forms import DonacionMonetariaForm, FormaDePagoForm, EstadoDonacionInsumoForm, EstadoDonacionMonetariaForm
from .forms import ReCaptcha

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
        context['captcha'] = ReCaptcha
        context['idSolicitud_insumo'] = self.kwargs['pk'] 
        context['Solicitud_insumo_obj'] = Solicitud_Donacion_Monetaria.objects.get(id=self.kwargs['pk'])
        objs = Solicitud_Donacion_Insumo.objects.all()
        for obj in objs:
            if obj.id == self.kwargs['pk']:
                context['Solicitud_insumo'] = obj
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
        solicitud_insumo_cantidad = []
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
                            messages.error(self.request, f"La cantidad {cantidadID.cantidad} supera a lo pedido del insumo {cantidadID.insumo}")
                            return render(self.request, 'donacionV2/donacion_insumo_form.html', context)  


class DonacionmonetariaNew(SuccessMessageMixin, generic.CreateView):
    model = Donacion_monetaria
    template_name = 'donacionV2/donacion_monetaria_form.html'
    form_class = DonacionMonetariaForm
    success_url = reverse_lazy('solicitud:solicitud_list')
    success_message = "Tu donación ha sido procesada con éxito"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['captcha'] = ReCaptcha
        context['Solicitud_monetaria_obj'] = Solicitud_Donacion_Monetaria.objects.get(id=self.kwargs['pk'])
        objs = Solicitud_Donacion_Monetaria.objects.all()
        for obj in objs:
            if obj.id == self.kwargs['pk']:
                context['Solicitud_monetaria'] = obj
        return context

    def form_valid(self, form):
        form.instance.uc = self.request.user
        context = self.get_context_data()
        form.instance.solicitud_monetaria = context['Solicitud_monetaria']
        if float(form.data['monto']) <= context['Solicitud_monetaria'].monto:
            newResult = float(context['Solicitud_monetaria'].monto) - float(form.data['monto'])
            Solicitud_Donacion_Monetaria.objects.filter(id=context['Solicitud_monetaria'].id).update(monto=newResult)
            return super().form_valid(form)
        messages.error(self.request, f"El monto de ${form.data['monto']} supera al pedido de ${context['Solicitud_monetaria'].monto}  en la solicitud")
        return render(self.request, 'donacionV2/donacion_monetaria_form.html', context)  


class MedioPagoView(generic.ListView):
    model = Medio_Pago
    template_name = "donacionV2/medioPago_list.html"
    context_object_name = "obj"
    login_url = 'bases/login.html'


class MedioPagoNew(SuccessMessageMixin, generic.CreateView):
    model = Medio_Pago
    template_name = 'donacionV2/medioPago_form.html'
    context_object_name = "obj"
    form_class = FormaDePagoForm
    success_url = reverse_lazy("donacionV2:medioPago_list")
    success_message = "Medio de pago creada sastifactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class MedioPagoDel(SuccessMessageMixin, generic.DeleteView):
    model = Medio_Pago
    template_name = 'donacionV2/medioPago_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy("donacionV2:medioPago_list")
    success_message = "Medio de pago sastifactoriamente"


class EstadosMonetariosListView(generic.ListView):
    model = Estado_Donacion_Monetaria
    template_name = 'donacionV2/estado_monetario_list.html'
    context_object_name = "obj"
    login_url = 'bases/login.html'


class EstadosMonetariosNew(SuccessMessageMixin, generic.CreateView):
    model = Estado_Donacion_Monetaria
    template_name = 'donacionV2/estado_monetario_form.html'
    context_object_name = "obj"
    form_class = EstadoDonacionMonetariaForm
    success_url = reverse_lazy('donacionV2:donacion_estado_monetaria_list')
    success_message = "Estado creado sastifactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class EstadosMonetariosDel(SuccessMessageMixin, generic.DeleteView):
    model = Estado_Donacion_Monetaria
    template_name = 'donacionV2/estado_monetario_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('donacionV2:donacion_estado_monetaria_list')
    success_message = "Estado eliminado sastifactoriamente"


class EstadosInsumosListView(generic.ListView):
    model = Estado_Donacion_Insumo
    template_name = 'donacionV2/estado_insumo_list.html'
    context_object_name = "obj"
    login_url = 'bases/login.html'


class EstadosInsumosNew(SuccessMessageMixin, generic.CreateView):
    model = Estado_Donacion_Insumo
    template_name = 'donacionV2/estado_insumo_form.html'
    context_object_name = "obj"
    form_class = EstadoDonacionInsumoForm
    success_url = reverse_lazy('donacionV2:donacion_estado_insumo_list')
    success_message = "Estado creado sastifactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class EstadosInsumosDel(SuccessMessageMixin, generic.DeleteView):
    model = Estado_Donacion_Insumo
    template_name = 'donacionV2/estado_insumos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('donacionV2:donacion_estado_insumo_list')
    success_message = "Estado eliminado sastifactoriamente"