from django.db import models
from bases.models import ClaseModelo

# Create your models here.

class Organizacion(ClaseModelo):
    descripcion = models.CharField(max_length=100, help_text='Descripcion de organizacion')
    logo = models.ImageField(blank=True, null=True)
    nombre = models.CharField(max_length=100, null=False, default="", unique=True)
    email = models.EmailField('Email', unique=True)
    cuit = models.CharField(max_length=100, null=False, default="")

class Clinica(ClaseModelo):
    descripcion = models.CharField(max_length=100, help_text='Descripcion de clinica')
    logo = models.ImageField(blank=True, null=True)
    nombre = models.CharField(max_length=100, null=False, default="",unique=True)
    email = models.EmailField('Email', unique=True)
    cuit = models.CharField(max_length=100, null=False, default="")

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Clinica, self).save()

    class Meta:
        verbose_name_plural = 'clinicas'


class Veterinario(ClaseModelo):
    descripcion = models.CharField(max_length=100, help_text='Descripcion de Veterinario')
    logo = models.ImageField(blank=True, null=True)
    nombre = models.CharField(max_length=100, null=False, default="",unique=True)
    email = models.EmailField('Email', unique=True)
    matricula = models.CharField(max_length=100, null=False, default="")

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Veterinario, self).save()

    class Meta:
        verbose_name_plural = 'Organizaciones'



