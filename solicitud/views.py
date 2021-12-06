from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

from bases.views import SinPrivilegios
from .models import Solicitud_Donacion_Insumo, Solicitud_Donacion_Monetaria, Estado_Solicitud_Insumo, Estado_Solicitud_Insumo_Detalle, Estado_Solicitud_Monetaria, Estado_Solicitud_Monetaria_Detalle
from .forms import ReCaptcha, SolicitudDonacionInsumoForm, SolicitudDonacionMonetariaForm, EstadoSolicitudInsumoForm, EstadoSolicitudMonetariaForm
from insumo.models import Cantidad_Insumo, Insumo
from usuario.models import Usuario
from django.forms.models import inlineformset_factory
from django.contrib.auth.mixins import PermissionRequiredMixin

InsumoFormset = inlineformset_factory(
   Solicitud_Donacion_Insumo, Cantidad_Insumo, extra=5, fields=('insumo', 'cantidad', 'solicitud_insumo',))

#Clase encargada de listar solicitudes monetarias y de insumos.
class SolicitudesListView(SinPrivilegios, generic.ListView):
    model = Solicitud_Donacion_Insumo
    #se especifica el tipo de permiso que deben tener los usuarios para poder acceder
    #a esta funcionalidad
    permission_required = "solicitud.view_solicitud_donacion_monetaria"
    #nombre de la plantilla donde se renderizará todo el contenido
    template_name = "solicitud/solicitud_list.html"
    login_url = 'bases/login.html'

    #mediante este método se le manda a la plantilla el contexto para permitir el renderizado
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solicitudes_insumos'] = Solicitud_Donacion_Insumo.objects.all()
        context['solicitudes_monetarias'] = Solicitud_Donacion_Monetaria.objects.all()
        context['cantidades_insumos'] = Cantidad_Insumo.objects.select_related('solicitud_insumo')
        context['insumos'] = Insumo.objects.all()
        return context

#Clase encargada de crear una donación del tipo insumo
class SolicitudDonacionInsumoNew(SuccessMessageMixin, generic.CreateView):
    #se especifica el modelo con el que se va a trabajar
    model = Solicitud_Donacion_Insumo
    #se especifica la plantilla donde se renderiza el contenido
    template_name = 'solicitud/solicitud_insumo_form.html'
    #se especifica el nombre del objeto para obtenerlo desde la plantilla
    context_object_name = 'solicitud'
    fields = ['titulo', 'pedido', 'veterinario']
    #url donde redirige en caso de éxito
    success_url = reverse_lazy('solicitud:solicitud_list')
    #mensaje de exito
    success_message = "Solicitud creada sastifactoriamente"
    
    #mediante este método se le manda a la plantilla el contexto para permitir el renderizado
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['captcha'] = ReCaptcha
        if self.request.POST:
            context['Insumo'] = InsumoFormset(self.request.POST, instance=self.object)
        else:
            context['Insumo'] = InsumoFormset(instance=self.object)
        return context
    
    #el siguiente método se ejecuta solo si los datos ingresados en el formulario de creación son válidos
    def form_valid(self, form):
        #se crea la relación con el usuario
        form.instance.uc = self.request.user
        context = self.get_context_data()
        #se crea la relación con el insumo seleccionado y si cantidad
        Insumo = context["Insumo"]
        self.object = form.save()
        if Insumo.is_valid():
            Insumo.instance = self.object
            Insumo.save()
        return super().form_valid(form)

#Clase encargada de crear una donación del tipo monetaria
class SolicitudDonacionMonetariaNew(SuccessMessageMixin, generic.CreateView):
    #se especifica el modelo con el que se va a trabajar
    model = Solicitud_Donacion_Monetaria
    #se especifica la plantilla donde se renderiza el contenido
    template_name = 'solicitud/solicitud_monetaria_form.html'
    #se especifica el nombre del objeto para obtenerlo desde la plantilla
    context_object_name = "solicitudes_monetarias"
    form_class = SolicitudDonacionMonetariaForm
    #url donde redirige en caso de éxito
    success_url = reverse_lazy('solicitud:solicitud_list')
    #mensaje de exito
    success_message = "Solicitud creada sastifactoriamente"

    #mediante este método se le manda a la plantilla el contexto para permitir el renderizado
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #contexto para renderizar el recaptcha
        context['captcha'] = ReCaptcha
        return context

    #el siguiente método se ejecuta solo si los datos ingresados en el formulario de creación son válidos
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class EstadosMonetariosListView(generic.ListView):
    model = Estado_Solicitud_Monetaria
    template_name = 'solicitud/estado_monetario_list.html'
    context_object_name = "obj"
    login_url = 'bases/login.html'


class EstadosMonetariosNew(SuccessMessageMixin, generic.CreateView):
    model = Estado_Solicitud_Monetaria
    template_name = 'solicitud/estado_monetario_form.html'
    context_object_name = "obj"
    form_class = EstadoSolicitudMonetariaForm
    success_url = reverse_lazy('solicitud:solicitud_estado_monetaria_list')
    success_message = "Estado creado sastifactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class EstadosMonetariosDel(SuccessMessageMixin, generic.DeleteView):
    model = Estado_Solicitud_Monetaria
    template_name = 'solicitud/estado_monetario_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('solicitud:solicitud_estado_monetaria_list')
    success_message = "Estado eliminado sastifactoriamente"


class EstadosInsumosListView(generic.ListView):
    model = Estado_Solicitud_Insumo
    template_name = 'solicitud/estado_insumo_list.html'
    context_object_name = "obj"
    login_url = 'bases/login.html'


class EstadosInsumosNew(SuccessMessageMixin, generic.CreateView):
    model = Estado_Solicitud_Insumo
    template_name = 'solicitud/estado_insumo_form.html'
    context_object_name = "obj"
    form_class = EstadoSolicitudInsumoForm
    success_url = reverse_lazy('solicitud:solicitud_estado_insumo_list')
    success_message = "Estado creado sastifactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class EstadosInsumosDel(SuccessMessageMixin, generic.DeleteView):
    model = Estado_Solicitud_Insumo
    template_name = 'solicitud/estado_insumos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('solicitud:solicitud_estado_insumo_list')
    success_message = "Estado eliminado sastifactoriamente"
