from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import SolicitudesListView, SolicitudDonacionInsumoNew, SolicitudDonacionMonetariaNew
urlpatterns = [
    path('solicitudes/', login_required(SolicitudesListView.as_view()), name='solicitud_list'),
    path('solicitud_insumo/new', login_required(SolicitudDonacionInsumoNew.as_view()), name='solicitud_insumo_new'),
    path('solicitud_monetaria/new', login_required(SolicitudDonacionMonetariaNew.as_view()), name='solicitud_monetaria_new'),
    ]