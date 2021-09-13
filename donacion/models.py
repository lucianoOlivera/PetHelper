from django.db import models
from bases.models import ClaseModelo

# clases relacionadas a las donaciones
# clases relacionadas a las solicitudes


class Solicitud_Donacion_Monetaria(ClaseModelo):
    titulo = models.TextField(max_length=100, null=False)
    monto = models.FloatField(max_length=100, null=False, blank=False)
    tipo_donacion = models.TextField(max_length=10, null=False)
    """ en realidad la descripcion es la relacion con el modelo de usuario y con un veterinario o clinica """
    descripcion = models.TextField(max_length=500, null=True)
    fecha = models.DateField(null=False)
    pedido = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'solicitudes_monetarias'

    def save(self):
        super(Solicitud_Donacion_Monetaria, self).save()


class Solicitud_Donacion_Insumo(ClaseModelo):
    titulo = models.TextField(max_length=100, null=False, blank=False)
    tipo_donacion = models.TextField(max_length=10, null=False, blank=False)
    descripcion = models.TextField(max_length=500, null=False, blank=False)
    fecha = models.DateField(null=False)
    pedido = models.ImageField(blank=True, null=True)
    """ falta la relacion con insumos """

    class Meta:
        verbose_name_plural = 'solicitudes_insumos'

    def save(self):
        super(Solicitud_Donacion_Insumo, self).save()


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
