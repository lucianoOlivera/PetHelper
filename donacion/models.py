from django.db import models
from bases.models import ClaseModelo
from organizaciones.models import Clinica, Veterinario
from usuario.models import Usuario


class Solicitud_Donacion_Monetaria(ClaseModelo):
    titulo = models.TextField(max_length=100, null=False)
    monto = models.FloatField(max_length=100, null=False, blank=False)
    """ en realidad la descripcion es la relacion con el modelo de usuario y con un veterinario o clinica """
    pedido = models.ImageField(blank=True, null=True)
    """ profesional = models.ForeignKey() """

    def save(self):
        super(Solicitud_Donacion_Monetaria, self).save()

    class Meta:
        verbose_name_plural = 'solicitudes_monetarias'


class Insumo(ClaseModelo):
    nombre = models.CharField(max_length=100)

    def save(self):
        super(Insumo, self).save()
                
    class Meta:
        verbose_name_plural = 'insumos'


class Solicitud_Donacion_Insumo(ClaseModelo):
    titulo = models.TextField(max_length=100, null=False, blank=False)
    pedido = models.ImageField(blank=True, null=True)
    """ cant_insumo = models.ForeignKey(Cantidad_Insumo, on_delete=models.CASCADE, null=True)  """
    

    def save(self):
        super(Solicitud_Donacion_Insumo, self).save()
         
    class Meta:
        verbose_name_plural = 'solicitudes_insumos'


class Cantidad_Insumo(ClaseModelo):
    solicitud_insumo = models.ForeignKey(Solicitud_Donacion_Insumo, on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField()
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, null=True) 

    def save(self):
        super(Cantidad_Insumo, self).save()
                
    class Meta:
        verbose_name_plural = 'cantidad_insumos'


class Estado_Solicitud_Monetaria(ClaseModelo):
    nombre = models.CharField(max_length=100)

    def save(self):
        super(Estado_Solicitud_Monetaria, self).save()

    class Meta:
        verbose_name_plural = 'estados_solicitudes_monetarias'


class Estado_Solicitud_Insumo(ClaseModelo):
    nombre = models.CharField(max_length=100)

    def save(self):
        super(Estado_Solicitud_Insumo, self).save()

    class Meta:
        verbose_name_plural = 'estados_solicitudes_insumos'


class Medio_Pago(ClaseModelo):
    nombre_pago = models.CharField(max_length=100)

    def save(self):
        super(Medio_Pago, self).save()
         
    class Meta:
        verbose_name_plural = 'medios_pagos'

    
class Donacion_Monetaria(ClaseModelo):
    monto = models.FloatField(max_length=100, null=False, blank=False)
    fechaCreacion = models.DateField(null=False)

    def save(self):
        super(Donacion_Monetaria, self).save()
         
    class Meta:
        verbose_name_plural = 'donaciones_monetarias'


class Donacion_Insumo(ClaseModelo):
    monto = models.FloatField(max_length=100, null=False, blank=False)
    fechaCreacion = models.DateField(null=False)

    def save(self):
        super(Donacion_Insumo, self).save()
         
    class Meta:
        verbose_name_plural = 'donaciones_insumos'