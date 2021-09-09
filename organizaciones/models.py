from django.db import models
from bases.models import ClaseModelo
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
class BaseModel(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        abstract = True

class Pais(BaseModel):
    pass


class Ciudad(BaseModel):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE,null=True)

class Departamento(BaseModel):
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE,null=True)


class Organizacion(ClaseModelo):
    descripcion = models.CharField(max_length=100, help_text='Descripcion de organizacion')
    logo = models.ImageField(blank=True, null=True)
    nombre = models.CharField(max_length=100, null=False, default="", unique=True)
    email = models.EmailField('Email', unique=True)
    cuit = models.CharField(max_length=100, null=False, default="")
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True)
    departamento = ChainedForeignKey(Departamento, chained_field='ciudad', chained_model_field='ciudad',null=True)
    ciudad = ChainedForeignKey(Ciudad, chained_field='pais', chained_model_field='pais', null=True)

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

