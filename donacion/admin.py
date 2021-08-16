from django.contrib import admin
from .models import Solicitud_Donacion_Insumo, Solicitud_Donacion_Monetaria

admin.site.register([ Solicitud_Donacion_Insumo, Solicitud_Donacion_Monetaria])
