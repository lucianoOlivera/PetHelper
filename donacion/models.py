from django.db import models

# clases relacionadas a las donaciones


# clases relacionadas a las solicitudes

class Solicitud_Donacion_Monetaria(models.Model):
   id=models.IntegerField(primary_key=True)
   titulo=models.TextField(max_length=100,null=True)
   tipo_donacion=models.TextField(max_length=10,null=True)
   descripcion=models.TextField(max_length=500,null=True)
   fecha=models.DateField(null=True)

   def __str__(self):
       return self.titulo

class Solicitud_Donacion_Insumo(models.Model):
   id=models.IntegerField(primary_key=True)
   titulo=models.TextField(max_length=100)
   tipo_donacion=models.TextField(max_length=10)
   descripcion=models.TextField(max_length=500)
   fecha=models.DateField()
   #pedido=models.ImageField()
 
   def __str__(self):
       return self.titulo
