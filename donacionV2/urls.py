from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    DonacionInsumoNew, DonacionmonetariaNew, MedioPagoNew, MedioPagoView, MedioPagoDel,
    EstadosInsumosListView, EstadosInsumosNew, EstadosInsumosDel,
    EstadosMonetariosListView, EstadosMonetariosDel, EstadosMonetariosNew, MercadoPagoView, TransferenciaView
    )


urlpatterns = [
    path('donacion_insumo/new/<int:pk>', login_required(DonacionInsumoNew.as_view()), name='donacion_insumo_new'),
    path('donacion_monetaria/new/<int:pk>', login_required(DonacionmonetariaNew.as_view()), name='donacion_monetaria_new'),

    path('medioPago/', login_required(MedioPagoView.as_view()), name='medioPago_list'),
    path('medioPago/new', login_required(MedioPagoNew.as_view()), name='medioPago_new'),
    path('medioPago/delete/<int:pk>', login_required(MedioPagoDel.as_view()), name='medioPago_del'),
    path('medioPago/mercadopago', login_required(MercadoPagoView.as_view()), name='medioPago_mercadopago'),
    path('medioPago/transferencia', login_required(TransferenciaView.as_view()), name='medioPago_transferencia'),

    path('EstadosDonacionMonetaria/', login_required(EstadosMonetariosListView.as_view()), name='donacion_estado_monetaria_list'),
    path('EstadosDonacionMonetaria/new', login_required(EstadosMonetariosNew.as_view()), name='donacion_estado_monetaria_new'),
    path('EstadosDonacionMonetaria/delete/<int:pk>', login_required(EstadosMonetariosDel.as_view()), name='donacion_estado_monetaria_del'),

    path('EstadosDonacionInsumos/', login_required(EstadosInsumosListView.as_view()), name='donacion_estado_insumo_list'),
    path('EstadosDonacionInsumos/new', login_required(EstadosInsumosNew.as_view()), name='donacion_estado_insumo_new'),
    path('EstadosDonacionInsumos/delete/<int:pk>', login_required(EstadosInsumosDel.as_view()), name='donacion_estado_insumo_del'),
]
