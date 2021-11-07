from django.shortcuts import render
from django.views import generic

class ReporteUsuariosView(generic.TemplateView):
    template_name = 'reportes/reportes_list.html'
    
