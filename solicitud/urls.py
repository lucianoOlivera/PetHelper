from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import SolicitudesListView, SolicitudDonacionInsumoNew

urlpatterns = [
    path('solicitudes/', login_required(SolicitudesListView.as_view()), name='solicitudes_list'),
    path('solicitud_insumo/new', login_required(SolicitudDonacionInsumoNew.as_view()), name='solicitud_insumo_new'),
    ]