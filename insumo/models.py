from django.db import models
from django.forms import forms
from bases.models import ClaseModelo
<<<<<<< HEAD
from solicitud.models import Solicitud_Donacion_Insumo
from django.core.exceptions import ValidationError
=======
from donacion.models import Donacion_Insumo
>>>>>>> 5e90ae5 (primero iteracion de solicitud)
from solicitud.models import Solicitud_Donacion_Insumo
# Create your models here.


class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    a = models.CharField(max_length=100)

    def save(self):
        super(Insumo, self).save()
              
    class Meta:
        verbose_name_plural = 'insumos'
  
    def __str__(self):
        return '%s' % (self.nombre)


class Cantidad_Insumo(models.Model):
    solicitud_insumo = models.ForeignKey(Solicitud_Donacion_Insumo, on_delete=models.CASCADE, null=True)
    cantidad = models.PositiveIntegerField()
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, null=True)

    def save(self):
        super(Cantidad_Insumo, self).save()
        
    class Meta:
        verbose_name_plural = 'cantidad_insumos'

    def clean(self):
        if self.cantidad < 0:
            raise forms.ValidationError('Negative price..... seriously?')
        return self.cantidad
