from django.db.models.aggregates import Sum
from django.shortcuts import render
from django.views import generic
from datetime import datetime
from calendar import month_name
from donacionV2.models import Cantidad_Insumo_Donacion, Donacion_Insumo, Donacion_monetaria
from django.utils.translation import gettext
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

    def get_donaciones_monetarias(self):
        total = 0
        año = datetime.now().year
        total = Donacion_monetaria.objects.filter(fc__year=año).aggregate(total=Sum('monto'))
        for key,value in total.items():
            return value
    
    def get_donaciones_insumos(self):
        total = 0
        año = datetime.now().year
        total = Cantidad_Insumo_Donacion.objects.filter(fc__year=año).aggregate(total=Sum('cantidad'))
        for key,value in total.items():
            return value
    
    def get_donaciones_insumos_mes(self):
        data = []
        año = datetime.now().year
        for m in range(1, 13):
            total = Donacion_Insumo.objects.filter(fc__year=año, fc__month=m).count()
            data.append(total)
        return data

    def get_donaciones_monetarias_mes(self):
        data = []
        año = datetime.now().year
        for m in range(1, 13):
            total = Donacion_monetaria.objects.filter(fc__year=año, fc__month=m).count()
            data.append(total)
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo1'] = 'Solicitudes de donaciones'
        context['titulo2'] = 'Cantidad por usuarios'
        context['titulo3'] = 'Donaciones'
        context['solicitudes_insumos'] = self.get_solicitudes_insumos_mes()
        context['solicitudes_monetarias'] = self.get_solicitudes_monetarias_mes()
        context['usuarios'] = Usuario.objects.all().count
        context['organizaciones'] = Organizacion.objects.all().count
        context['clinicas'] = Clinica.objects.all().count
        context['veterinarios'] = Veterinario.objects.all().count
        context['donaciones_monetarias'] = self.get_donaciones_monetarias
        context['donaciones_insumos'] = self.get_donaciones_insumos
        context['donaciones_monetarias_mes'] = self.get_donaciones_monetarias_mes
        context['donaciones_insumos_mes'] = self.get_donaciones_insumos_mes
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


class DonacionesPDFiew(PDFTemplateView):
    template_name = 'reportes/donaciones_pdf_reporte.html'

    def get_donaciones_insumos_mes(self):
        data = []
        año = datetime.now().year
        for m in range(1, 13):
            total = Donacion_Insumo.objects.filter(fc__year=año, fc__month=m).count()
            data.append(total)
        return data

    def get_donaciones_monetarias_mes(self):
        data = []
        año = datetime.now().year
        for m in range(1, 13):
            total = Donacion_monetaria.objects.filter(fc__year=año, fc__month=m).count()
            data.append(total)
        return data
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['fecha'] = datetime.now()
        context['donaciones_insumos'] = self.get_donaciones_insumos_mes()
        context['donaciones_monetarias'] = self.get_donaciones_monetarias_mes()
        print(context)
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
