from django.shortcuts import render
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import Organizacion 
from .forms import OrganizacionForm
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
    success_message = "organizacion creada sastifactoriamente"

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
    success_message = "organizacion creada sastifactoriamente"

    def form_valid (self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

