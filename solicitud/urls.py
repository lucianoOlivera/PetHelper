from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import SolicitudesListView, SolicitudDonacionInsumoNew, AddSolicitud, AddAsistencia

urlpatterns = [
    path('solicitudes/', login_required(SolicitudesListView.as_view()), name='solicitudes_list'),
    path('solicitud_insumo/new', login_required(SolicitudDonacionInsumoNew.as_view()), name='solicitud_insumo_new'),
    path('solicitudes/test', login_required(AddSolicitud.as_view()), name='solicitudes_add'),
    path('solicitudes/test2', login_required(AddAsistencia.as_view()), name='solicitudes_add2'),
    ]