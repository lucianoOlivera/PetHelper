from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.shortcuts import render

from .models import Solicitud_Donacion_Monetaria, Solicitud_Donacion_Insumo, Donacion_Monetaria, Donacion_Insumo, Insumo, Cantidad_Insumo
from .forms import SolicitudDonacionMonetariaForm, SolicitudDonacionInsumoForm, DonacionMonetariaForm, DonacionInsumoForm, CantidadInsumoForm
from usuario.models import Usuario
from organizaciones.models import Veterinario


""" class SolicitudDonacionMonetariaView(generic.ListView):
    model = Solicitud_Donacion_Monetaria
    template_name = 'donacion/solicitudes_list.html'
    context_object_name = 'solicitudes_monetarias'
    login_url = 'bases/login.html' """


class SolicitudDonacionMonetariaNew(SuccessMessageMixin, generic.CreateView):
    model = Solicitud_Donacion_Monetaria
    template_name = 'donacion/solicitud_monetaria_form.html'
    context_object_name = "solicitudes_monetarias"
    form_class = SolicitudDonacionMonetariaForm
    success_url = reverse_lazy('donacion:solicitudes_list')
    success_message = "Solicitud creada sastifactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class SolicitudDonacionMonetariaDel(SuccessMessageMixin, generic.DeleteView):
    model = Solicitud_Donacion_Monetaria
    template_name = 'donacion/solicitud_monetaria_del.html'
    context_object_name = 'solicitudes_monetarias'
    success_url = reverse_lazy('donacion:solicitudes_list')
    success_message = "Solicitud eliminada sastifactoriamente"


class SolicitudDonacionMonetariaEdit(SuccessMessageMixin, generic.UpdateView):
    model = Solicitud_Donacion_Monetaria
    template_name = 'donacion/solicitud_monetaria_modal_editar.html'
    context_object_name = "solicitudes_monetarias"
    form_class = SolicitudDonacionMonetariaForm
    success_url = reverse_lazy('donacion:solicitudes_list')
    success_message = "Solicitud editada sastifactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form) 


""" class SolicitudDonacionInsumoView(generic.ListView):
    model = Solicitud_Donacion_Insumo
    template_name = "donacion/solicitudes_list.html"
    context_object_name = 'solicitudes_insumos'
    login_url = 'bases/login.html' """


class SolicitudInsumoMonetariaView(TemplateView):
    template_name = "donacion/solicitudes_list.html"
    login_url = 'bases/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solicitudes_insumos'] = Solicitud_Donacion_Insumo.objects.all()
        context['solicitudes_monetarias'] = Solicitud_Donacion_Monetaria.objects.all()
        context['usuario'] = Usuario.objects.get(pk=1) 
        context['cantidades_insumos'] = Cantidad_Insumo.objects.select_related('solicitud_insumo')
        context['insumos'] = Insumo.objects.all()
        return context

    """ creo que aca puedo definir el post, cada vez que le den click que se cree """


class SolicitudDonacionInsumoNew(SuccessMessageMixin, generic.CreateView):
    model = Solicitud_Donacion_Insumo
    template_name = 'donacion/solicitud_insumo_form.html'
    context_object_name = 'object'
    form_class = SolicitudDonacionInsumoForm
    second_form_class = CantidadInsumoForm
    success_url = reverse_lazy('donacion:solicitudes_list')
    success_message = "Solicitud creada sastifactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        context['insumos'] = Insumo.objects.all()
        return context
    
    def post(self, request, *arg, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)

        if form.is_valid() and form2.is_valid():
            """ tengo que iterar el formulario pero sobre que? """
            solicitud = form.save(commit=False)
            solicitud.uc = request.user
            solicitud.save()
            donacion = Donacion_Insumo(solicitud_insumo=solicitud, monto=10, uc=request.user)
            donacion.save() 
            cantidad_insumo = form2.save(commit=False)
            cantidad_insumo.solicitud_insumo = solicitud
            cantidad_insumo.uc = self.request.user
            cantidad_insumo.save()
            return HttpResponseRedirect(reverse_lazy('donacion:solicitudes_list'))
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class SolicitudDonacionInsumoDel(SuccessMessageMixin, generic.DeleteView):
    model = Solicitud_Donacion_Insumo
    template_name = 'donacion/solicitud_insumo_del.html'
    context_object_name = 'solicitudes_insumos'
    success_url = reverse_lazy('donacion:solicitudes_list')
    success_message = "Solicitud eliminada sastifactoriamente"


class SolicitudDonacionInsumoEdit(SuccessMessageMixin, generic.UpdateView):
    model = Solicitud_Donacion_Insumo
    template_name = 'donacion/solicitud_insumo_modal_editar.html'
    context_object_name = "solicitudes_insumos"
    form_class = SolicitudDonacionInsumoForm
    success_url = reverse_lazy('donacion:solicitudes_list')
    success_message = "Solicitud editada sastifactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class DonacionMonetariaView(generic.ListView):
    model = Donacion_Monetaria
    template_name = "donacion/donaciones_list.html"
    context_object_name = 'donaciones_monetarias'
    login_url = 'bases/login.html' 


class DonacionMonetariaNew(SuccessMessageMixin, generic.CreateView):
    model = Donacion_Monetaria
    template_name = 'donacion/donacion_monetaria_form.html'
    context_object_name = "object"
    form_class = DonacionMonetariaForm
    success_url = reverse_lazy('donacion:solicitudes_list')
    success_message = "Donación creada sastifactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class DonacionMonetariaDel(SuccessMessageMixin, generic.DeleteView):
    model = Donacion_Monetaria
    template_name = 'donacion/donacion_monetaria_del.html'
    context_object_name = 'donaciones_monetarias'
    success_url = reverse_lazy('donacion:solicitudes_list')
    success_message = "Donación eliminada sastifactoriamente"


class DonacionMonetariaEdit(SuccessMessageMixin, generic.UpdateView):
    model = Donacion_Monetaria
    template_name = 'organizaciones/donacion_monetaria_modal_editar.html'
    context_object_name = 'donaciones_monetarias'
    form_class = DonacionMonetariaForm
    success_url = reverse_lazy('donacion:solicitudes_list')
    success_message = "Donación editada sastifactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class DonacionInsumoView(generic.ListView):
    model = Donacion_Insumo
    template_name = "donacion/donaciones_list.html"
    context_object_name = 'donaciones_insumos'
    login_url = 'bases/login.html'


class DonacionInsumoNew(SuccessMessageMixin, generic.CreateView):
    model = Donacion_Insumo
    template_name = 'donacion/donacion_insumo_form.html'
    context_object_name = 'object'
    form_class = DonacionInsumoForm
    second_form_class = CantidadInsumoForm
    success_url = reverse_lazy('donacion:solicitudes_list')
    success_message = "Tu donación ha sido procesada con éxito"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        context['insumos'] = Insumo.objects.all()
        return context
    
    def post(self, request, *arg, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)

        if form.is_valid() and form2.is_valid():
            """ tengo que iterar el formulario pero sobre que? """
            donacion = form.save(commit=False)
            donacion.uc = request.user
            donacion.save() 
            cantidad_insumo = form2.save(commit=False)
            cantidad_insumo.donacion_insumo = donacion
            cantidad_insumo.uc = self.request.user
            cantidad_insumo.save()
            return HttpResponseRedirect(reverse_lazy('donacion:solicitudes_list'))
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class DonacionInsumoDel(SuccessMessageMixin, generic.DeleteView):
    model = Donacion_Insumo
    template_name = 'donacion/donacion_insumo_del.html'
    context_object_name = 'donaciones_insumos'
    success_url = reverse_lazy('donacion:solicitudes_list')
    success_message = "Donación eliminada sastifactoriamente"


class DonacionInsumoEdit(SuccessMessageMixin, generic.UpdateView):
    model = Donacion_Insumo
    template_name = 'donacion/donacion_insumo_form.html'
    context_object_name = 'donaciones'
    form_class = DonacionInsumoForm
    success_url = reverse_lazy('donacion:solicitudes_list')
    success_message = "Donación editada sastifactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
