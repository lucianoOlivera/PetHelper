from django.db import models
import geocoder


class Direccion(models.Model):
    direccion = models.TextField()
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.direccion, key='pk.eyJ1IjoibWFyaWFsdXoiLCJhIjoiY2t2OG9jZmlhOXdtYjJvcWprYjhqOTFpaSJ9.vYDuCmCvJtO_hA6gYRUa5A')
        g = g.latlng
        self.latitud = g[0]
        self.longitud = g[1]
        return super(Direccion, self).save(*args, **kwargs)



