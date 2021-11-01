from django.db import models
from bases.models import ClaseModelo
from insumo.models import Insumo
from insumo.models import Solicitud_Donacion_Insumo


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
