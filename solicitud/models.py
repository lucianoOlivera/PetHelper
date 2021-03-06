from django.db import models
from bases.models import ClaseModelo
from organizaciones.models import Clinica, Veterinario

# Create your models here.
BANCOS = [
  (1, "Patagonia"),
  (2, "Supervielle"),
  (3, "ICBC"),
  (4, "Banco de la Nación Argentina"),
  (5, "Credicoop"),
  (6, "Comafi"),
  (7, "Santander"),
  (8, "HSBC")
]

ESTADOS = [
  (0, "Sin Validar"),
  (1, "Validado"),
  (2, "Rechazado")
]

class Solicitud_Donacion_Insumo(ClaseModelo):
    titulo = models.TextField(max_length=100, null=False, blank=False)
    pedido = models.ImageField(upload_to="solicitud",blank=True, null=True)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, null=True)
    EstadoSolicitudInsumo = models.PositiveSmallIntegerField(choices=ESTADOS,default="0")
     
    def save(self):
        super(Solicitud_Donacion_Insumo, self).save()
         
    class Meta:
        verbose_name_plural = 'solicitudes_insumos'


class Solicitud_Donacion_Monetaria(ClaseModelo):
    titulo = models.TextField(max_length=100, null=False, blank=False)
    pedido = models.ImageField(upload_to="solicitud",blank=True, null=True)
    monto = models.FloatField(max_length=100, null=False, blank=False)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, null=True)
    cbu = models.PositiveBigIntegerField(blank=True, null=True)
    alias = models.CharField(max_length=100, blank=True, null=True)
    nombre_titular = models.CharField(max_length=100, blank=True, null=True)
    nombre_banco = models.PositiveSmallIntegerField(choices=BANCOS, default="1")
    EstadoSolicitudMonetaria = models.PositiveSmallIntegerField(choices=ESTADOS,default="0")
     
    def save(self):
        super(Solicitud_Donacion_Monetaria, self).save()

    class Meta:
        verbose_name_plural = 'solicitudes_monetarias'


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


class Estado_Solicitud_Monetaria_Detalle(ClaseModelo):
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField()

    def save(self):
        super(Estado_Solicitud_Monetaria_Detalle, self).save()

    class Meta:
        verbose_name_plural = 'estados_solicitudes_monetarias_detalle'


class Estado_Solicitud_Insumo_Detalle(ClaseModelo):
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField()

    def save(self):
        super(Estado_Solicitud_Monetaria_Detalle, self).save()

    class Meta:
        verbose_name_plural = 'estados_solicitudes_monetarias_detalle'
