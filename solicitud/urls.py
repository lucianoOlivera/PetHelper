from django.urls import path
from django.contrib.auth.decorators import login_required

<<<<<<< HEAD
from .views import SolicitudesListView, SolicitudDonacionInsumoNew

urlpatterns = [
<<<<<<< HEAD
    path('solicitudes/', login_required(SolicitudesListView.as_view()), name='solicitudes_list'),
    path('solicitud_insumo/new', login_required(SolicitudDonacionInsumoNew.as_view()), name='solicitud_insumo_new'),
=======
    path('solicitud/', login_required(SolicitudesListView.as_view()), name='solicitud_list'),
    path('solicitud/new', login_required(SolicitudDonacionInsumoNew.as_view()), name='solicitud_insumo_new'),
>>>>>>> e240275 (terminado)
=======
from .views import SolicitudDonacionInsumoView, SolicitudDonacionInsumoNew

urlpatterns = [
    path('solicitud/', login_required(SolicitudDonacionInsumoView.as_view()), name='solicitud_insumo_list'),
    path('solicitud/new', login_required(SolicitudDonacionInsumoNew.as_view()), name='solicitud_insumo_new'),
>>>>>>> 5e90ae5 (primero iteracion de solicitud)
    ]