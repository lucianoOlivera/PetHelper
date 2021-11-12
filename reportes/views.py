from django.shortcuts import render
from django.views import generic
from datetime import datetime
from calendar import month_name
import locale 
from easy_pdf.views import PDFTemplateView

from organizaciones.models import Clinica, Organizacion, Veterinario
from solicitud.models import Solicitud_Donacion_Insumo, Solicitud_Donacion_Monetaria
from usuario.models import Usuario

class ReporteSolicitudesView(generic.TemplateView):
    template_name = 'reportes/reportes_list.html'

    def get_solicitudes_insumos_mes(self):
        data = []
        año = datetime.now().year
        for m in range(1, 13):
            total = Solicitud_Donacion_Insumo.objects.filter(fc__year=año, fc__month=m).count()
            data.append(total)
        return data

    def get_solicitudes_monetarias_mes(self):
        data = []
        año = datetime.now().year
        for m in range(1, 13):
            total = Solicitud_Donacion_Monetaria.objects.filter(fc__year=año, fc__month=m).count()
            data.append(total)
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo1'] = 'Solicitudes de donaciones'
        context['titulo2'] = 'Cantidad por usuarios'
        context['solicitudes_insumos'] = self.get_solicitudes_insumos_mes()
        context['solicitudes_monetarias'] = self.get_solicitudes_monetarias_mes()
        context['usuarios'] = Usuario.objects.all().count
        context['organizaciones'] = Organizacion.objects.all().count
        context['clinicas'] = Clinica.objects.all().count
        context['veterinarios'] = Veterinario.objects.all().count
        return context


class SolicitudesPDFiew(PDFTemplateView):
    template_name = 'reportes/solicitudes_pdf_reporte.html'

    def get_solicitudes_insumos_mes(self):
        data = []
        año = datetime.now().year
        for m in range(1, 13):
            total = Solicitud_Donacion_Insumo.objects.filter(fc__year=año, fc__month=m).count()
            data.append(total)
        return data

    def get_solicitudes_monetarias_mes(self):
        data = []
        año = datetime.now().year
        for m in range(1, 13):
            total = Solicitud_Donacion_Monetaria.objects.filter(fc__year=año, fc__month=m).count()
            data.append(total)
        return data
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['fecha'] = datetime.now()
        context['solicitudes_insumos'] = self.get_solicitudes_insumos_mes()
        context['solicitudes_monetarias'] = self.get_solicitudes_monetarias_mes()
        context['meses'] = list(month_name[1:])
        return context



class UsuariosPDFiew(PDFTemplateView):
    template_name = 'reportes/usuarios_pdf_reporte.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fecha'] = datetime.now()
        context['usuarios'] = Usuario.objects.all().count
        context['organizaciones'] = Organizacion.objects.all().count
        context['clinicas'] = Clinica.objects.all().count
        context['veterinarios'] = Veterinario.objects.all().count
        return context
