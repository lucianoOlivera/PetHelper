from django.contrib import admin
from .models import Solicitud_Donacion_Monetaria, Solicitud_Donacion_Insumo, Insumo, Cantidad_Insumo, Donacion_Insumo, Donacion_Monetaria

admin.site.register([Solicitud_Donacion_Monetaria, Solicitud_Donacion_Insumo, Insumo, Cantidad_Insumo, Donacion_Insumo, Donacion_Monetaria])
