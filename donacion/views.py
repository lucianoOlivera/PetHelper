from django.shortcuts import render
from donacion.models import Solicitud_Donacion_Insumo, Solicitud_Donacion_Monetaria


def listarSolicitudes(request):
   solicitudes_monetarias = Solicitud_Donacion_Monetaria.objects.all()
   solictudes_insumos = Solicitud_Donacion_Insumo.objects.all()
   contexto = {
           'solicitudes_monetarias': solicitudes_monetarias,
           'solicitudes_insumos': solictudes_insumos
   }
   return render(request, 'donacion/listado_solicitudes.html', contexto)
