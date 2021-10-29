from django.shortcuts import render
from django.views import generic
from .models import Insumo, Cantidad_Insumo
from .forms import InsumoForm, CantidadDeInsumo
from django.http.response import HttpResponseRedirect
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.


class InsumoView(generic.ListView):
    model = Insumo
    template_name = 'insumo/insumo_list.html'
    context_object_name = "obj"
    login_url = 'bases/login.html'


class InsumoNew(SuccessMessageMixin, generic.CreateView):
    model = Insumo
    template_name = 'insumo/insumo_form.html'
    context_object_name = "obj"
    form_class = InsumoForm
    success_url = reverse_lazy('insumo:insumo_list')
    success_message = "Insumo creado sastifactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class InsumoDel(SuccessMessageMixin, generic.DeleteView):
    model = Insumo
    template_name = 'insumo/insumo_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('insumo:insumo_list')
    success_message = "Insumo eliminado sastifactoriamente"


class CantidadInsumoNew(SuccessMessageMixin, generic.CreateView):
    model = Cantidad_Insumo
    template_name = 'insumo/cantidad_insumo_form.html'
    context_object_name = "obj"
    form_class = CantidadDeInsumo
    success_url = reverse_lazy('insumo:cantidad_insumo_list')
    success_message = "Cantidad insumo creada sastifactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class CantdadIsumoList(generic.ListView):
    model = Cantidad_Insumo
    template_name = 'insumo/cantidad_insumo_list.html'
    context_object_name = "obj"
    login_url = 'bases/login.html'