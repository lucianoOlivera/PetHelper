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

def get_mes(mes):
    if mes == 1:
        return 'Ene'
    elif mes == 2:
        return 'Feb'
    if mes == 3:
        return 'Mar'
    elif mes == 4:
        return 'Abr'
    if mes == 5:
        return 'May'
    elif mes == 6:
        return 'Jun'
    if mes == 7:
        return 'Jul'
    elif mes == 8:
        return 'Ago'
    if mes == 9:
        return 'Sep'
    elif mes == 10:
        return 'Oct'
    if mes == 11:
        return 'Nov'
    else:
        return 'Dic'


def get_meses_cero(meses):
    donaciones_insumos = []
    for m in meses:
        donaciones_insumos.append(0)
    return donaciones_insumos


def get_filtrar_solicitudes_monetarias_mes(fromMonth, toMonth,fromDateFormat,toDateFormat, fromYear, toYear):
    data = []
    meses = []
    if fromYear == toYear:
        for m in range(fromMonth, toMonth+1):
            total = Solicitud_Donacion_Monetaria.objects.filter(fc__month=m,fc__gte=fromDateFormat,fc__lte=toDateFormat).count()
            data.append(total)
            mes_format = get_mes(m)
            meses.append(mes_format)
        return data, meses
    else:
        for y in range(fromYear ,toYear+1):
            # del 12 al 1
            for m in range(fromMonth, toMonth+1): 
                print(y)
                print(m)
                total = Solicitud_Donacion_Monetaria.objects.filter(fc__year=y,fc__month=m,fc__gte=fromDateFormat,fc__lte=toDateFormat).count()
                data.append(total)
                mes_format = get_mes(m)
                meses.append(mes_format)
            return data, meses


def get_filtrar_solicitudes_insumos_mes(fromMonth, toMonth,fromDateFormat,toDateFormat):
    data = []
    for m in range(fromMonth, toMonth+1):
        total = Solicitud_Donacion_Insumo.objects.filter(fc__month=m,fc__gte=fromDateFormat,fc__lte=toDateFormat).count()
        data.append(total)
    return data


def get_filtrar_donaciones_monetarias_mes(fromMonth, toMonth,fromDateFormat,toDateFormat, fromYear, toYear):
    data = []
    meses = []
    if fromYear == toYear:
        for m in range(fromMonth, toMonth+1):
            total = Donacion_monetaria.objects.filter(fc__month=m,fc__gte=fromDateFormat,fc__lte=toDateFormat).count()
            data.append(total)
            mes_format = get_mes(m)
            meses.append(mes_format)
        return data, meses
    else:
        for y in range(fromYear ,toYear+1):
            # del 12 al 1
            for m in range(fromMonth, toMonth+1): 
                print(y)
                print(m)
                total = Donacion_monetaria.objects.filter(fc__year=y,fc__month=m,fc__gte=fromDateFormat,fc__lte=toDateFormat).count()
                data.append(total)
                mes_format = get_mes(m)
                meses.append(mes_format)
            return data, meses


def get_filtrar_donaciones_insumos_mes(fromMonth, toMonth,fromDateFormat,toDateFormat):
    data = []
    for m in range(fromMonth, toMonth+1):
        total = Donacion_Insumo.objects.filter(fc__month=m,fc__gte=fromDateFormat,fc__lte=toDateFormat).count()
        data.append(total)
    return data


def get_solicitudes_insumos_mes():
    data = []
    año = datetime.now().year
    for m in range(1, 13):
        total = Solicitud_Donacion_Insumo.objects.filter(fc__year=año, fc__month=m).count()
        data.append(total)
    return data


def get_solicitudes_monetarias_mes():
    data = []
    meses = []
    año = datetime.now().year
    for m in range(1, 13):
        total = Solicitud_Donacion_Monetaria.objects.filter(fc__year=año, fc__month=m).count()
        data.append(total)
        mes_format = get_mes(m)
        meses.append(mes_format)
    return data, meses

def get_donaciones_insumos_mes():
    data = []
    año = datetime.now().year
    for m in range(1, 13):
        total = Donacion_Insumo.objects.filter(fc__year=año, fc__month=m).count()
        data.append(total)
    return data

def get_donaciones_monetarias_mes():
    data = []
    meses = []
    año = datetime.now().year
    for m in range(1, 13):
        total = Donacion_monetaria.objects.filter(fc__year=año, fc__month=m).count()
        data.append(total)
        mes_format = get_mes(m)
        meses.append(mes_format)
    return data, meses


class ReporteSolicitudesView(generic.TemplateView):
    template_name = 'reportes/reportes_list.html'

    # acumuladores
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo1'] = 'Solicitudes de donaciones'
        context['titulo2'] = 'Cantidad por usuarios'
        context['titulo3'] = 'Donaciones'
        context['usuarios'] = Usuario.objects.all().count
        context['organizaciones'] = Organizacion.objects.all().count
        context['clinicas'] = Clinica.objects.all().count
        context['veterinarios'] = Veterinario.objects.all().count
        context['acumulador_monetarias'] = self.get_donaciones_monetarias
        context['acumulador_insumos'] = self.get_donaciones_insumos
        if self.request.method == 'GET':
            fromDate1 = self.request.GET.get('fromDate1')
            toDate1 = self.request.GET.get('toDate1')
            fromDate2 = self.request.GET.get('fromDate2')
            toDate2 = self.request.GET.get('toDate2')
            fromDate3 = self.request.GET.get('fromDate3')
            toDate3 = self.request.GET.get('toDate3')
            solicitud_monetaria = self.request.GET.get('solicitud_monetaria')
            solicitud_insumos = self.request.GET.get('solicitud_insumos')
            donacion_monetaria = self.request.GET.get('donacion_monetaria')
            donacion_insumos = self.request.GET.get('donacion_insumos')
            context['solicitud_monetaria'] = solicitud_monetaria
            context['solicitud_insumos'] = solicitud_insumos
            context['donacion_monetaria'] = donacion_monetaria
            context['donacion_insumos'] = donacion_insumos
            if fromDate1 and toDate1:
                fromDateFormat = datetime.strptime(fromDate1, '%Y-%m-%d')
                toDateFormat = datetime.strptime(toDate1, '%Y-%m-%d')
                fromYear = fromDateFormat.year
                toYear = toDateFormat.year
                fromMonth = fromDateFormat.month
                toMonth = toDateFormat.month
                donaciones_monetarias, meses2 = get_donaciones_monetarias_mes()
                context['donaciones_monetarias'] = donaciones_monetarias
                context['donaciones_insumos'] = get_donaciones_insumos_mes()
                context['meses2'] = meses2
                context['fromDate1']= fromDate1
                context['toDate1']= toDate1
                # filtrar solicitudes monetarias con fecha
                if solicitud_monetaria == 'on':
                    solicitudes_monetarias, meses1 = get_filtrar_solicitudes_monetarias_mes(fromMonth,toMonth,fromDateFormat,toDateFormat, fromYear, toYear)
                    context['solicitudes_insumos'] = get_meses_cero(meses1)
                    context['meses1'] = meses1
                    context['solicitudes_monetarias'] = solicitudes_monetarias
                    return context
                # filtrar solicitudes insumos con fecha
                elif solicitud_insumos == 'on':
                    solicitudes_monetarias, meses1 = get_filtrar_solicitudes_monetarias_mes(fromMonth,toMonth,fromDateFormat,toDateFormat, fromYear, toYear)
                    solicitudes_insumos = get_filtrar_solicitudes_insumos_mes(fromMonth,toMonth,fromDateFormat,toDateFormat)
                    context['solicitudes_insumos'] = solicitudes_insumos
                    context['solicitudes_monetarias'] = get_meses_cero(meses1)
                    context['meses1'] = meses1
                    return context
                # filtrar todas solicitudes con fecha
                else:
                    solicitudes_monetarias, meses1 = get_filtrar_solicitudes_monetarias_mes(fromMonth,toMonth,fromDateFormat,toDateFormat, fromYear, toYear)
                    solicitudes_insumos = get_filtrar_solicitudes_insumos_mes(fromMonth,toMonth,fromDateFormat,toDateFormat)
                    context['solicitudes_monetarias'] = solicitudes_monetarias
                    context['solicitudes_insumos'] = solicitudes_insumos
                    context['meses1'] = meses1
                    return context
            elif fromDate2 and toDate2:
                fromDateFormat = datetime.strptime(fromDate2, '%Y-%m-%d')
                toDateFormat = datetime.strptime(toDate2, '%Y-%m-%d')
                fromYear = fromDateFormat.year
                toYear = toDateFormat.year
                fromMonth = fromDateFormat.month
                toMonth = toDateFormat.month
                solicitudes_monetarias, meses1 = get_solicitudes_monetarias_mes()
                context['solicitudes_insumos'] = get_solicitudes_insumos_mes()
                context['solicitudes_monetarias'] = solicitudes_monetarias
                context['meses1'] = meses1
                # filtrar donaciones monetarias con fecha
                if donacion_monetaria == 'on':
                    donaciones_monetarias, meses2 = get_filtrar_donaciones_monetarias_mes(fromMonth,toMonth,fromDateFormat,toDateFormat, fromYear, toYear)
                    context['donaciones_monetarias'] = donaciones_monetarias
                    context['donaciones_insumos'] = get_meses_cero(meses2)
                    context['meses2'] = meses2
                    context['fromDate2']= fromDate2
                    context['toDate2']= toDate2
                    return context
                # filtrar donaciones insumos con fecha
                elif donacion_insumos == 'on':
                    donaciones_monetarias, meses2 = get_filtrar_donaciones_monetarias_mes(fromMonth,toMonth,fromDateFormat,toDateFormat, fromYear, toYear)
                    context['donaciones_monetarias'] = get_meses_cero(meses2)
                    context['donaciones_insumos'] = get_filtrar_solicitudes_insumos_mes(fromMonth,toMonth,fromDateFormat,toDateFormat)
                    context['meses2'] = meses2
                    context['fromDate2']= fromDate2
                    context['toDate2']= toDate2
                    return context
                # filtrar todas donaciones con fecha
                else:
                    donaciones_monetarias, meses2 = get_filtrar_donaciones_monetarias_mes(fromMonth,toMonth,fromDateFormat,toDateFormat, fromYear, toYear)
                    donaciones_insumos = get_filtrar_donaciones_insumos_mes(fromMonth, toMonth,fromDateFormat,toDateFormat)
                    context['donaciones_monetarias'] = donaciones_monetarias
                    context['donaciones_insumos'] = donaciones_insumos
                    context['meses2'] = meses2
                    context['fromDate2']= fromDate2
                    context['toDate2']= toDate2
                    return context
            else:
                # filtrar solicitudes insumos sin fecha
                if solicitud_insumos == 'on':
                    solicitudes_monetarias, meses1 = get_solicitudes_monetarias_mes()
                    context['solicitudes_insumos'] = get_solicitudes_insumos_mes()
                    context['solicitudes_monetarias'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    context['meses1'] = meses1
                    donaciones_monetarias, meses2 = get_donaciones_monetarias_mes()
                    context['donaciones_monetarias'] = donaciones_monetarias
                    context['donaciones_insumos'] = get_donaciones_insumos_mes()
                    context['meses2'] = meses2
                    return context
                 # filtrar solicitudes monetarias sin fecha
                elif solicitud_monetaria == 'on':
                    solicitudes_monetarias, meses1 = get_solicitudes_monetarias_mes()
                    context['solicitudes_monetarias'] = solicitudes_monetarias
                    # siempre va a ser asi porque me trae todos los meses
                    context['solicitudes_insumos'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    context['meses1'] = meses1
                    donaciones_monetarias, meses2 = get_donaciones_monetarias_mes()
                    context['donaciones_monetarias'] = donaciones_monetarias
                    context['donaciones_insumos'] = get_donaciones_insumos_mes()
                    context['meses2'] = meses2
                    return context
                # filtrar donaciones insumos sin fecha
                elif donacion_insumos == 'on':
                    donaciones_monetarias, meses2 = get_donaciones_monetarias_mes()
                    context['donaciones_monetarias'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    context['donaciones_insumos'] = get_donaciones_insumos_mes()
                    context['meses2'] = meses2
                    solicitudes_monetarias, meses1 = get_solicitudes_monetarias_mes()
                    context['solicitudes_insumos'] = get_solicitudes_insumos_mes()
                    context['solicitudes_monetarias'] = solicitudes_monetarias
                    context['meses1'] = meses1
                    return context
                # filtrar donaciones monetaria sin fecha
                elif donacion_monetaria == 'on':
                    donaciones_monetarias, meses2 = get_donaciones_monetarias_mes()
                    context['donaciones_monetarias'] = donaciones_monetarias
                    context['donaciones_insumos'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    context['meses2'] = meses2
                    solicitudes_monetarias, meses1 = get_solicitudes_monetarias_mes()
                    context['solicitudes_insumos'] = get_solicitudes_insumos_mes()
                    context['solicitudes_monetarias'] = solicitudes_monetarias
                    context['meses1'] = meses1
                    return context
                # filtrar todas solicitudes y donaciones sin fecha
                else:
                    solicitudes_monetarias, meses1 = get_solicitudes_monetarias_mes()
                    context['solicitudes_insumos'] = get_solicitudes_insumos_mes()
                    context['solicitudes_monetarias'] = solicitudes_monetarias
                    context['meses1'] = meses1
                    donaciones_monetarias, meses2 = get_donaciones_monetarias_mes()
                    context['donaciones_monetarias'] = donaciones_monetarias
                    context['donaciones_insumos'] = get_donaciones_insumos_mes()
                    context['meses2'] = meses2
                    return context

class SolicitudesPDFiew(PDFTemplateView):
    template_name = 'reportes/solicitudes_pdf_reporte.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['fecha'] = datetime.now()
        if self.request.method == 'GET':
            fromDate1 = self.request.GET.get('fromDate1')
            toDate1 = self.request.GET.get('toDate1')
            solicitud_monetaria = self.request.GET.get('monetaria')
            solicitud_insumos = self.request.GET.get('insumos')
            if fromDate1 and toDate1:
                fromDateFormat = datetime.strptime(fromDate1, '%Y-%m-%d')
                toDateFormat = datetime.strptime(toDate1, '%Y-%m-%d')
                fromYear = fromDateFormat.year
                toYear = toDateFormat.year
                fromMonth = fromDateFormat.month
                toMonth = toDateFormat.month
                # filtrar solicitudes monetarias con fecha
                if solicitud_monetaria == 'on':
                    solicitudes_monetarias, meses1 = get_filtrar_solicitudes_monetarias_mes(fromMonth,toMonth,fromDateFormat,toDateFormat, fromYear, toYear)
                    context['meses1'] = meses1
                    context['solicitudes_monetarias'] = solicitudes_monetarias
                    return context
                # filtrar solicitudes insumos con fecha
                elif solicitud_insumos == 'on':
                    solicitudes_monetarias, meses1 = get_filtrar_solicitudes_monetarias_mes(fromMonth,toMonth,fromDateFormat,toDateFormat, fromYear, toYear)
                    solicitudes_insumos = get_filtrar_solicitudes_insumos_mes(fromMonth,toMonth,fromDateFormat,toDateFormat)
                    context['solicitudes_insumos'] = solicitudes_insumos
                    context['meses1'] = meses1
                    return context
                # filtrar todas solicitudes con fecha
                else:
                    solicitudes_monetarias, meses1 = get_filtrar_solicitudes_monetarias_mes(fromMonth,toMonth,fromDateFormat,toDateFormat, fromYear, toYear)
                    solicitudes_insumos = get_filtrar_solicitudes_insumos_mes(fromMonth,toMonth,fromDateFormat,toDateFormat)
                    context['solicitudes_monetarias'] = solicitudes_monetarias
                    context['solicitudes_insumos'] = solicitudes_insumos
                    context['meses1'] = meses1
                    return context
            else:
                # filtrar solicitudes insumos sin fecha
                if solicitud_insumos == 'on':
                    solicitudes_monetarias, meses1 = get_solicitudes_monetarias_mes()
                    context['solicitudes_insumos'] = get_solicitudes_insumos_mes()
                    context['meses1'] = meses1
                    return context
                 # filtrar solicitudes monetarias sin fecha
                elif solicitud_monetaria == 'on':
                    solicitudes_monetarias, meses1 = get_solicitudes_monetarias_mes()
                    context['solicitudes_monetarias'] = solicitudes_monetarias
                    context['meses1'] = meses1
                    return context
                else:
                    solicitudes_monetarias, meses1 = get_solicitudes_monetarias_mes()
                    context['solicitudes_insumos'] = get_solicitudes_insumos_mes()
                    context['solicitudes_monetarias'] = solicitudes_monetarias
                    context['meses1'] = meses1
                    return context

class DonacionesPDFiew(PDFTemplateView):
    template_name = 'reportes/donaciones_pdf_reporte.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['fecha'] = datetime.now()
        if self.request.method == 'GET':
            fromDate2 = self.request.GET.get('fromDate2')
            toDate2 = self.request.GET.get('toDate2')
            donacion_monetaria = self.request.GET.get('monetaria')
            donacion_insumos = self.request.GET.get('insumos')
            if fromDate2 and toDate2:
                fromDateFormat = datetime.strptime(fromDate2, '%Y-%m-%d')
                toDateFormat = datetime.strptime(toDate2, '%Y-%m-%d')
                fromYear = fromDateFormat.year
                toYear = toDateFormat.year
                fromMonth = fromDateFormat.month
                toMonth = toDateFormat.month
                # filtrar donaciones monetarias con fecha
                if donacion_monetaria == 'on':
                    donaciones_monetarias, meses2 = get_filtrar_donaciones_monetarias_mes(fromMonth,toMonth,fromDateFormat,toDateFormat, fromYear, toYear)
                    context['donaciones_monetarias'] = donaciones_monetarias
                    context['meses2'] = meses2
                    return context
                # filtrar donaciones insumos con fecha
                elif donacion_insumos == 'on':
                    donaciones_monetarias, meses2 = get_filtrar_donaciones_monetarias_mes(fromMonth,toMonth,fromDateFormat,toDateFormat, fromYear, toYear)
                    context['donaciones_insumos'] = get_filtrar_solicitudes_insumos_mes(fromMonth,toMonth,fromDateFormat,toDateFormat)
                    context['meses2'] = meses2
                    return context
                # filtrar todas donaciones con fecha
                else:
                    donaciones_monetarias, meses2 = get_filtrar_donaciones_monetarias_mes(fromMonth,toMonth,fromDateFormat,toDateFormat, fromYear, toYear)
                    donaciones_insumos = get_filtrar_donaciones_insumos_mes(fromMonth, toMonth,fromDateFormat,toDateFormat)
                    context['donaciones_monetarias'] = donaciones_monetarias
                    context['donaciones_insumos'] = donaciones_insumos
                    context['meses2'] = meses2
                    return context
            else:
                # filtrar donaciones insumos sin fecha
                if donacion_insumos == 'on':
                    donaciones_monetarias, meses2 = get_donaciones_monetarias_mes()
                    context['donaciones_insumos'] = get_donaciones_insumos_mes()
                    context['meses2'] = meses2
                    return context
                # filtrar donaciones monetaria sin fecha
                elif donacion_monetaria == 'on':
                    donaciones_monetarias, meses2 = get_donaciones_monetarias_mes()
                    context['donaciones_monetarias'] = donaciones_monetarias
                    context['meses2'] = meses2
                    return context
                # filtrar todas solicitudes y donaciones sin fecha
                else:
                    donaciones_monetarias, meses2 = get_donaciones_monetarias_mes()
                    context['donaciones_monetarias'] = donaciones_monetarias
                    context['donaciones_insumos'] = get_donaciones_insumos_mes()
                    context['meses2'] = meses2
                    return context
        else:
            print("error")


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
