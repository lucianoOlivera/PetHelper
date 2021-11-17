from datetime import time
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.db import models
from bases.models import ClaseModelo
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

phone_regex = RegexValidator(regex=r"(?:(?:00)?549?)?0?(?:11|[2368]\d)(?:(?=\d{0,2}15)\d{2})??\d{8}", message="Debe ingresar un número válido para Argentina")
DIAS = [
  (1, "Lunes"),
  (2, "Martes"),
  (3, "Miercoles"),
  (4, "Jueves"),
  (5, "Viernes"),
  (6, "Sabado"),
  (7, "Domingo"),
]
HORAS_DE_DIA_24 = [(i,i) for i in range(1,25)]

class Organizacion(ClaseModelo):
    descripcion = models.CharField(max_length=100, null=False)
    logo = models.ImageField(upload_to="organizacion",blank=True, null=True)
    nombre = models.CharField(max_length=100, null=False, default="")
    email = models.EmailField('Email', unique=True, null=False)
    cuit = models.CharField(max_length=11, null=False, default="", unique=True)
    telefono = models.CharField(max_length=11, null=False, default="", unique=True, validators=[phone_regex], help_text="Ejemplo: 2614247398")
    direccion = models.CharField(max_length=50, null=True, help_text="Ejemplo: Maipu 123, Godoy Cruz, Mendoza")
    dia_desde = models.PositiveSmallIntegerField(choices=DIAS, default="1")
    dia_hasta = models.PositiveSmallIntegerField(choices=DIAS, default="5")
    hora_desde = models.PositiveSmallIntegerField(choices=HORAS_DE_DIA_24, default="9")
    hora_hasta = models.PositiveSmallIntegerField(choices=HORAS_DE_DIA_24, default="18")
    
    class Meta:
        verbose_name_plural = 'organizaciones'

class Clinica(ClaseModelo):
    descripcion = models.CharField(max_length=100, null=False)
    logo = models.ImageField(upload_to="clinica",blank=True, null=True)
    nombre = models.CharField(max_length=100, null=False, default="")
    email = models.EmailField('Email', unique=True, null=False)
    cuit = models.CharField(max_length=11, null=False, default="",unique=True)
    whatsapp = models.CharField(max_length=17, blank=False, unique=True, validators=[phone_regex], help_text="Ejemplo: 26127483945")
    telefono = models.CharField(max_length=10, null=False, default="",unique=True, validators=[phone_regex], help_text="Ejemplo: 2614247398")
    direccion = models.CharField(max_length=50, null=True, help_text="Ejemplo: Maipu 123, Godoy Cruz, Mendoza")
    dia_desde = models.PositiveSmallIntegerField(choices=DIAS, default="1")
    dia_hasta = models.PositiveSmallIntegerField(choices=DIAS, default="5")
    hora_desde = models.PositiveSmallIntegerField(choices=HORAS_DE_DIA_24, default="9")
    hora_hasta = models.PositiveSmallIntegerField(choices=HORAS_DE_DIA_24, default="18")

    def save(self):
        super(Clinica, self).save()

    class Meta:
        verbose_name_plural = 'clinicas'


class Veterinario(ClaseModelo):
    descripcion = models.CharField(max_length=100, null=False)
    logo = models.ImageField(upload_to="veterinario",blank=True, null=True)
    nombre = models.CharField(max_length=100, null=False, default="")
    apellido = models.CharField(max_length=100, null=False, default="")
    email = models.EmailField('Email', unique=True, null=False)
    matricula = models.CharField(max_length=4, null=False, default="", unique=True)
    whatsapp = models.CharField( max_length=17, null=False, unique=True, validators=[phone_regex], help_text="Ejemplo: 2614247398")
    direccion = models.CharField(max_length=50, null=True, help_text="Ejemplo: Maipu 123, Godoy Cruz, Mendoza")
    dia_desde = models.PositiveSmallIntegerField(choices=DIAS, default="1")
    dia_hasta = models.PositiveSmallIntegerField(choices=DIAS, default="5")
    hora_desde = models.PositiveSmallIntegerField(choices=HORAS_DE_DIA_24, default="9")
    hora_hasta = models.PositiveSmallIntegerField(choices=HORAS_DE_DIA_24, default="18")
    calificacion = models.PositiveIntegerField(null=True, blank=True,default=0, 
        validators=[ MinValueValidator(0),
                    MaxValueValidator(5)
        ])
    calificacion_total = models.PositiveSmallIntegerField(null= True, blank=True,default=0)

    def save(self):
        super(Veterinario, self).save()

    class Meta:
        verbose_name_plural = 'veterinarios'
    

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.apellido, self.matricula)

