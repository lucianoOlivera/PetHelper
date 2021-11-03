from django.db import models
from bases.models import ClaseModelo
from organizaciones.models import Clinica, Veterinario

# Create your models here.


class Solicitud_Donacion_Insumo(ClaseModelo):
    titulo = models.TextField(max_length=100, null=False, blank=False)
    pedido = models.ImageField(upload_to="solicitud",blank=True, null=True)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, null=True)
     
    def save(self):
        super(Solicitud_Donacion_Insumo, self).save()
         
    class Meta:
        verbose_name_plural = 'solicitudes_insumos'


class Solicitud_Donacion_Monetaria(ClaseModelo):
    titulo = models.TextField(max_length=100, null=False, blank=False)
    pedido = models.ImageField(upload_to="solicitud",blank=True, null=True)
    monto = models.FloatField(max_length=100, null=False, blank=False)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, null=True)
     
    def save(self):
        super(Solicitud_Donacion_Monetaria, self).save()

    class Meta:
        verbose_name_plural = 'solicitudes_monetarias'


