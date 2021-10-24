from django.db import models
from bases.models import ClaseModelo
from donacion.models import Solicitud_Donacion_Insumo, Donacion_Insumo
# Create your models here.


class Insumo(ClaseModelo):
    nombre = models.CharField(max_length=100)

    def save(self):
        super(Insumo, self).save()
              
    class Meta:
        verbose_name_plural = 'insumos'
  
    def __str__(self):
        return '%s' % (self.nombre)


class Cantidad_Insumo(ClaseModelo):
    solicitud_insumo = models.ForeignKey(Solicitud_Donacion_Insumo, on_delete=models.CASCADE, null=True)
    cantidad = models.PositiveIntegerField()
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, null=True)
    donacion_insumo = models.ForeignKey(Donacion_Insumo, on_delete=models.CASCADE, null=True) 

    def save(self):
        super(Cantidad_Insumo, self).save()
             
    class Meta:
        verbose_name_plural = 'cantidad_insumos'
