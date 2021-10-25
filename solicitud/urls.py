from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import SolicitudDonacionInsumoView, SolicitudDonacionInsumoNew

urlpatterns = [
    path('solicitud/', login_required(SolicitudDonacionInsumoView.as_view()), name='solicitud_insumo_list'),
    path('solicitud/new', login_required(SolicitudDonacionInsumoNew.as_view()), name='solicitud_insumo_new'),
    ]