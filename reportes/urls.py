from django.urls import path

from reportes.views import DonacionesPDFiew, ReporteSolicitudesView, SolicitudesPDFiew, UsuariosPDFiew

urlpatterns = [
    path('reportes/', ReporteSolicitudesView.as_view(), name='reportes_list'),
    path('reportes/solicitudes_pdf/', SolicitudesPDFiew.as_view(), name='reporte_solicitudes_pdf'),
    path('reportes/donaciones_pdf', DonacionesPDFiew.as_view(), name='reporte_donaciones_pdf'),
    path('reportes/usuarios_pdf', UsuariosPDFiew.as_view(), name='reporte_usuarios_pdf'),
]
