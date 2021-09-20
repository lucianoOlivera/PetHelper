from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True,null=True)
    fm = models.DateTimeField(auto_now=True,null=True)
    uc = models.ForeignKey("usuario.Usuario", on_delete=models.CASCADE,null=True)
    um = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True