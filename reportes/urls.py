from django.urls import path

from reportes.views import ReporteUsuariosView

urlpatterns = [
    path('reportes/', ReporteUsuariosView.as_view(), name='reportes_list'),
]
