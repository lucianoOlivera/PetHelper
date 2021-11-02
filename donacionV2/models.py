from django.db import models
from bases.models import ClaseModelo
from insumo.models import Insumo
from solicitud.models import Solicitud_Donacion_Monetaria, Solicitud_Donacion_Insumo


class Donacion_Insumo(ClaseModelo):
    fechaCreacion = models.DateField(auto_now_add=True)
    solicitud_insumo = models.ForeignKey(Solicitud_Donacion_Insumo, on_delete=models.CASCADE, null=True)

    def save(self):
        super(Donacion_Insumo, self).save()
         
    class Meta:
        verbose_name_plural = 'donaciones_insumos'


class Cantidad_Insumo_Donacion(models.Model):
    donacion_isumo = models.ForeignKey(Donacion_Insumo, on_delete=models.CASCADE, null=True)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, null=True)
    cantidad = models.PositiveIntegerField(unique=False)
    fc = models.DateTimeField(auto_now_add=True)

    def save(self):
        super(Cantidad_Insumo_Donacion, self).save()
             
    class Meta:
        verbose_name_plural = 'cantidad_insumos_donacion'


class Donacion_monetaria(ClaseModelo):
    solicitud_monetaria = models.ForeignKey(Solicitud_Donacion_Monetaria, on_delete=models.CASCADE, null=True)
    monto = models.FloatField(max_length=100, null=False, blank=False)

    def save(self):
        super(Donacion_monetaria, self).save()
         
    class Meta:
        verbose_name_plural = 'donaciones_monetaria'


class Medio_Pago(ClaseModelo):
    nombre_pago = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='pothos', null=True, blank=True)

    def save(self):
        super(Medio_Pago, self).save()
         
    class Meta:
        verbose_name_plural = 'medios_pagos'
