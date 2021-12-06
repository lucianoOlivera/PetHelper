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
import mercadopago
sdk = mercadopago.SDK("TEST-3842048582306113-112022-c422c5bc8b41c494c1342837e941c719-1023214274")

# Create your views here.
DonacionFormset = inlineformset_factory(
   Donacion_Insumo, Cantidad_Insumo_Donacion, extra=5, fields=('insumo', 'cantidad',))

#Clase encragda de crear nuevas solicitudes de tipo insumo
class DonacionInsumoNew(SuccessMessageMixin, generic.CreateView):
    #se especifica el modelo con el que se va a trabajar
    model = Donacion_Insumo
    #se especifica la plantilla donde se renderiza el contenido
    template_name = 'donacionV2/donacion_insumo_form.html'
    fields = []
    #se especifica el nombre del objeto para obtenerlo desde la plantilla
    context_object_name = 'Donacion'
    #url donde redirige en caso de éxito
    success_url = reverse_lazy('solicitud:solicitud_list')
    #mensaje de exito
    success_message = "Tu donación ha sido procesada con éxito"

    #mediante este método se le manda a la plantilla el contexto para permitir el renderizado
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #se manda el ReCaptcha en el contexto
        context['captcha'] = ReCaptcha
        #se obtiene el id de la solitcitud que queremos donar
        context['idSolicitud_insumo'] = self.kwargs['pk']
        #obtenemos la solicitud con el id que capturamos anteriormente
        context['Solicitud_insumo_obj'] = Solicitud_Donacion_Insumo.objects.get(id=self.kwargs['pk'])
        objs = Solicitud_Donacion_Insumo.objects.all()
        for obj in objs:
            if obj.id == self.kwargs['pk']:
                context['Solicitud_insumo'] = obj
        #se manda en el contexto el formulario para que el usuario ingrese la cantidad de insumos a donar
        if self.request.POST:
            context['Donacion'] = DonacionFormset(self.request.POST, instance=self.object)
        else:
            context['Donacion'] = DonacionFormset(instance=self.object)
        return context

    #el siguiente método se ejecuta solo si los datos ingresados en el formulario de creación son válidos
    def form_valid(self, form):
        #se hace la relación con el usuario que ejecuta la donación
        form.instance.uc = self.request.user
        context = self.get_context_data()
        #obtenemos la solicitud que estará relacionada a la donación
        SolicitudDonacionInsumo = Solicitud_Donacion_Insumo.objects.get(id=context['idSolicitud_insumo'])
        form.instance.solicitud_insumo = SolicitudDonacionInsumo
        Donacion = context["Donacion"]
        self.object = form.save()
        #si los datos ingresados en el formularios son válidos se guarda la instancia de la donacion
        if Donacion.is_valid():
            Donacion.instance = self.object
            Donacion.save()
        #se relaciona los insumos seleccionados para donar con sus cantidades
        solicitud_insumo_cantidad = []
        cantidadInsumoSolicitud = Cantidad_Insumo.objects.all()
        for cantidadInsumo in cantidadInsumoSolicitud:
            if cantidadInsumo.solicitud_insumo.id == SolicitudDonacionInsumo.id:
                solicitud_insumo_cantidad.append(cantidadInsumo)    
        cantidadInsumoDonacion = Cantidad_Insumo_Donacion.objects.all()
        #se pasa a realizar las validaciones de las cantidades de insumos
        #si la cantidad ingresada en la donacion supera a la cantidad pedida se renderiza un mensaje de error
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

#Clase encargada de crear donaciones monetarias
class DonacionmonetariaNew(SuccessMessageMixin, generic.CreateView):
    #se especifica el modelo con el que se va a trabajar
    model = Donacion_monetaria
    #se especifica la plantilla donde se renderiza el contenido
    template_name = 'donacionV2/donacion_monetaria_form.html'
    form_class = DonacionMonetariaForm
    #url donde redirige en caso de éxito
    success_url = reverse_lazy('solicitud:solicitud_list')
    #mensaje de exito
    success_message = "Tu donación ha sido procesada con éxito"

    #mediante este método se le manda a la plantilla el contexto para permitir el renderizado
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #se manda el ReCaptcha en el contexto
        context['captcha'] = ReCaptcha
        #obtenemos los medios de pagos disponibles
        context['medios_pago'] = Medio_Pago.objects.all()
        #buscamos la solicitud a la cual se le donará
        context['Solicitud_monetaria_obj'] = Solicitud_Donacion_Monetaria.objects.get(id=self.kwargs['pk'])
        objs = Solicitud_Donacion_Monetaria.objects.all()
        for obj in objs:
            if obj.id == self.kwargs['pk']:
                context['Solicitud_monetaria'] = obj
        return context

    #el siguiente método se ejecuta solo si los datos ingresados en el formulario de creación son válidos
    def form_valid(self, form):
        #se hace la relación con el usuario que va a donar 
        form.instance.uc = self.request.user
        context = self.get_context_data()
        #obtenemos la solicitud a la cual se le donara para crear la relacion con la instancia de la donacion
        form.instance.solicitud_monetaria = context['Solicitud_monetaria']
        #se realiza la validacion de que el monto ingresado en la donacion no sea mayor al monto pedido
        #si no se cumple, se renderiza un mensaje de error
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
    success_message = "Medio de pago eliminado sastifactoriamente"


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

#clase encargada de renderizar el checkout de mercado pago
class MercadoPagoView(generic.TemplateView):
    #se especifica la plantilla donde se renderiza el contenido
    template_name = 'donacionV2/mercadopago.html'

    #mediante este método se le manda a la plantilla el contexto para permitir el renderizado
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Crea el item que se mostrara a la derecha en el checkout
        preference_data = {
            "items": [
                {
                    "title": "Donacion Monetaria",
                    "quantity": 1,
                    "unit_price": 1000,
                }
            ]
        }
        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]
        context['preference'] = preference
        print(context)
        return context

#clase encargada de renderizar los datos para transferencia bancaria
class TransferenciaView(generic.TemplateView):
    #se especifica la plantilla donde se renderiza el contenido
    template_name = 'donacionV2/transferencia.html'

    #mediante este método se le manda a la plantilla el contexto para permitir el renderizado
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #obtenemos los datos de la solicitud para renderizar datos bancarios
        objs = Solicitud_Donacion_Monetaria.objects.all()
        for obj in objs:
            if obj.id == self.kwargs['pk']:
                context['Solicitud_monetaria'] = obj
        return context
