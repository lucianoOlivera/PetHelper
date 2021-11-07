from django.contrib import admin
from .models import Organizacion, Clinica, Veterinario

# Register your models here.


admin.site.register(Organizacion)
admin.site.register(Clinica)
admin.site.register(Veterinario)
