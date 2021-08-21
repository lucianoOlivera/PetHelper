from django.db import models

# Create your models here.

class Organizacion(ClaseModelo):
    descripcion = models.CharField(max_length=100, help_text='Descripcion de organizacion', unique=True)
    logo = models.ImageField(blank=True, null=True)
    nombre = models.CharField(max_length=100, null=False, default="")
    email = models.EmailField('Email', unique=True)
    cuit = models.CharField(max_length=100, null=False, default="")

     def clean(self):
        self.nombre = self.nombre.upper()
        if self.id:
            if self.cuit and len(
                Organizacion.objects.filter(
                    identificador__exact=self.identificador
                ).exclude(id__exact=self.id)
            ):
                raise ValidationError(
                    "El cuit indicado ya está en uso"
                )

            if self.nombre and len(
                Organizacion.objects.filter(nombre__exact=self.nombre,).exclude(
                    id__exact=self.id
                )
            ):
                raise ValidationError("El nombre indicado ya está en uso")
        else:
            if self.identificador and len(
                Organizacion.objects.filter(
                    identificador__exact=self.identificador
                )
            ):
                raise ValidationError(
                    "El cuit indicado ya está en uso"
                )

            if self.nombre and len(
                Organizacion.objects.filter(nombre__exact=self.nombre)
            ):
                raise ValidationError("El nombre indicado ya está en uso")

    def save(self):
        self.clean()
        self.descripcion = self.descripcion.upper()
        super(Organizaciones, self).save()

    class Meta:
        verbose_name_plural = 'Organizaciones'
    

class Clinica(ClaseModelo):
    descripcion = models.CharField(max_length=100, help_text='Descripcion de clinica', unique=True)
    logo = models.ImageField(blank=True, null=True)
    nombre = models.CharField(max_length=100, null=False, default="")
    email = models.EmailField('Email', unique=True)
    cuit = models.CharField(max_length=100, null=False, default="")

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Clinica, self).save()

    class Meta:
        verbose_name_plural = 'clinicas'


class Veterinario(ClaseModelo):
    descripcion = models.CharField(max_length=100, help_text='Descripcion de Veterinario', unique=True)
    logo = models.ImageField(blank=True, null=True)
    nombre = models.CharField(max_length=100, null=False, default="")
    email = models.EmailField('Email', unique=True)
    matricula = models.CharField(max_length=100, null=False, default="")

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Veterinario, self).save()

    class Meta:
        verbose_name_plural = 'Organizaciones'



