from django.db import models
from bases.models import ClaseModelo
from organizaciones.models import Clinica, Veterinario

# Create your models here.


class Solicitud_Donacion_Insumo(ClaseModelo):
    titulo = models.TextField(max_length=100, null=False, blank=False)
    pedido = models.ImageField(blank=True, null=True)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, null=True)
     
    def save(self):
        super(Solicitud_Donacion_Insumo, self).save()
         
    class Meta:
        verbose_name_plural = 'solicitudes_insumos'