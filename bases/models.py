from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=False)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey("usuario.Usuario", on_delete=models.CASCADE, default=None)
    um = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True