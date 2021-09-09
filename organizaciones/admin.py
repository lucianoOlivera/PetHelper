from django.contrib import admin
from .models import Pais, Departamento, Ciudad

# Register your models here.
@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
	list_display =['id', 'nombre']

@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
	list_display = ['id', 'nombre', 'pais']

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ['id', 'nombre', 'ciudad']
