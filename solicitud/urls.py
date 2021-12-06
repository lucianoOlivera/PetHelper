from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import SolicitudesListView, SolicitudDonacionInsumoNew, SolicitudDonacionMonetariaNew, EstadosMonetariosListView, EstadosMonetariosNew, EstadosMonetariosDel, EstadosInsumosDel, EstadosInsumosListView, EstadosInsumosNew

#urls asociadas a las vistas
urlpatterns = [
    path('solicitudes/', login_required(SolicitudesListView.as_view()), name='solicitud_list'),
    path('solicitud_insumo/new', login_required(SolicitudDonacionInsumoNew.as_view()), name='solicitud_insumo_new'),
    path('solicitud_monetaria/new', login_required(SolicitudDonacionMonetariaNew.as_view()), name='solicitud_monetaria_new'),

    path('EstadosSolicitudMonetaria/', login_required(EstadosMonetariosListView.as_view()), name='solicitud_estado_monetaria_list'),
    path('EstadosSolicitudMonetaria/new', login_required(EstadosMonetariosNew.as_view()), name='solicitud_estado_monetaria_new'),
    path('EstadosSolicitudMonetaria/delete/<int:pk>', login_required(EstadosMonetariosDel.as_view()), name='solicitud_estado_monetaria_del'),

    path('EstadosSolicitudInsumos/', login_required(EstadosInsumosListView.as_view()), name='solicitud_estado_insumo_list'),
    path('EstadosSolicitudInsumos/new', login_required(EstadosInsumosNew.as_view()), name='solicitud_estado_insumo_new'),
    path('EstadosSolicitudInsumos/delete/<int:pk>', login_required(EstadosInsumosDel.as_view()), name='solicitud_estado_insumo_del'),
]
