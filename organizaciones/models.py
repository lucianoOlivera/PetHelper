from django.core.validators import RegexValidator
from django.db import models
from bases.models import ClaseModelo

# Create your models here.

class Organizacion(ClaseModelo):
    descripcion = models.CharField(max_length=100, help_text='Descripcion de organizacion')
    logo = models.ImageField(blank=True, null=True)
    nombre = models.CharField(max_length=100, null=False, default="", unique=True)
    email = models.EmailField('Email', unique=True)
    cuit = models.CharField(max_length=100, null=False, default="", unique=True)
    telefono = models.CharField(max_length=7, null=False, default="")
    
    class Meta:
        verbose_name_plural = 'organizaciones'

class Clinica(ClaseModelo):
    descripcion = models.CharField(max_length=100, help_text='Descripcion de clinica')
    logo = models.ImageField(blank=True, null=True)
    nombre = models.CharField(max_length=100, null=False, default="",unique=True)
    email = models.EmailField('Email', unique=True)
    cuit = models.CharField(max_length=100, null=False, default="")
    #phone_regex = RegexValidator(regex=r'/^(?:(?:00)?549?)?0?(?:11|[2368]\d)(?:(?=\d{0,2}15)\d{2})??\d{8}$/', message="Debe ingresar un número de celular válido para Argentina")
    whatsapp = models.CharField( max_length=17, blank=True)
    telefono = models.CharField(max_length=7, null=False, default="")

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Clinica, self).save()

    class Meta:
        verbose_name_plural = 'clinicas'


class Veterinario(ClaseModelo):
    descripcion = models.CharField(max_length=100, help_text='Descripcion de Veterinario')
    logo = models.ImageField(blank=True, null=True)
    nombre = models.CharField(max_length=100, null=False, default="",unique=True)
    apellido = models.CharField(max_length=100, null=False, default="",unique=True)
    email = models.EmailField('Email', unique=True)
    matricula = models.CharField(max_length=100, null=False, default="", unique=True)
    whatsapp = models.CharField( max_length=17, blank=True)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Veterinario, self).save()

    class Meta:
        verbose_name_plural = 'veterinarios'



