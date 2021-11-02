from django.db import models
import geocoder

""" class BaseModel(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        abstract = True

class Ciudad(BaseModel):
    nombre = models.CharField(max_length=100)


class Departamento(BaseModel):
    nombre = models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE,null=True)

class Direccion(BaseModel):
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()
    departamento = models.ForeignKey(Ciudad, on_delete=models.CASCADE,null=True) """


class Direccion(models.Model):
    direccion = models.TextField()
    latitud = models.CharField(max_length=15,blank=True, null=True)
    longitud = models.CharField(max_length=15,blank=True, null=True)

    class Meta:
        verbose_name_plural = 'direcciones'
  
    def __str__(self):
        return '%s' % (self.direccion)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.direccion, key='pk.eyJ1IjoibWFyaWFsdXoiLCJhIjoiY2t2OG9jZmlhOXdtYjJvcWprYjhqOTFpaSJ9.vYDuCmCvJtO_hA6gYRUa5A')
        g = g.latlng
        self.latitud = g[0]
        self.longitud = g[1]
        return super(Direccion, self).save(*args, **kwargs)



