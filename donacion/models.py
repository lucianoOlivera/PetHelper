from django.db import models
from bases.models import ClaseModelo
from organizaciones.models import Clinica, Veterinario
from usuario.models import Usuario


class Solicitud_Donacion_Monetaria(ClaseModelo):
    titulo = models.TextField(max_length=100, null=False)
    monto = models.FloatField(max_length=100, null=False, blank=False)
    pedido = models.ImageField(blank=True, null=True)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, null=True)

    def save(self):
        super(Solicitud_Donacion_Monetaria, self).save()

    class Meta:
        verbose_name_plural = 'solicitudes_monetarias'


class Insumo(models.Model):
    nombre = models.CharField(max_length=100)

    def save(self):
        super(Insumo, self).save()
                
    class Meta:
        verbose_name_plural = 'insumos'
    
    def __str__(self):
        return '%s' % (self.nombre)


class Solicitud_Donacion_Insumo(ClaseModelo):
    titulo = models.TextField(max_length=100, null=False, blank=False)
    pedido = models.ImageField(blank=True, null=True)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, null=True)
     
    def save(self):
        super(Solicitud_Donacion_Insumo, self).save()
         
    class Meta:
        verbose_name_plural = 'solicitudes_insumos'



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
    fechaCreacion = models.DateField(auto_now_add=True)
    solicitud_monetaria = models.ForeignKey(Solicitud_Donacion_Monetaria, on_delete=models.CASCADE, null=True)

    def save(self):
        super(Donacion_Monetaria, self).save()
         
    class Meta:
        verbose_name_plural = 'donaciones_monetarias'


class Donacion_Insumo(ClaseModelo):
    monto = models.FloatField(max_length=100, null=True, blank=True)
    fechaCreacion = models.DateField(auto_now_add=True)
    solicitud_insumo = models.ForeignKey(Solicitud_Donacion_Insumo, on_delete=models.CASCADE, null=True)


    def save(self):
        super(Donacion_Insumo, self).save()
         
    class Meta:
        verbose_name_plural = 'donaciones_insumos'


class Cantidad_Insumo(models.Model):
    solicitud_insumo = models.PositiveIntegerField(null=True, blank=True)
    cantidad = models.PositiveIntegerField(null=True, blank=True)
    insumo = models.PositiveIntegerField(null=True, blank=True)
    donacion_insumo = models.PositiveIntegerField(null=True, blank=True)

    def save(self):
        super(Cantidad_Insumo, self).save()
                
    class Meta:
        verbose_name_plural = 'cantidad_insumos'