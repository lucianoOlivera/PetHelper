   
from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import SolicitudInsumoMonetariaView, SolicitudDonacionMonetariaNew, SolicitudDonacionMonetariaDel, SolicitudDonacionMonetariaEdit, SolicitudDonacionInsumoNew, SolicitudDonacionInsumoDel, SolicitudDonacionInsumoEdit, DonacionMonetariaView, DonacionMonetariaNew, DonacionMonetariaDel, DonacionMonetariaEdit, DonacionInsumoView, DonacionInsumoNew, DonacionInsumoDel, DonacionInsumoEdit   

urlpatterns = [
    path('solicitud_monetaria/new', login_required(SolicitudDonacionMonetariaNew.as_view()), name='solicitud_monetaria_new'),
    path('solicitud_monetaria/delete/<int:pk>', login_required(SolicitudDonacionMonetariaDel.as_view()), name='solicitud_monetaria_del'),
    path('solicitud_insumo/delete/<int:pk>', login_required(SolicitudDonacionInsumoDel.as_view()), name='solicitud_insumo_del'),
    path('solicitud_monetaria/edit/<int:pk>', login_required(SolicitudDonacionMonetariaEdit.as_view()), name='solicitud_monetaria__edit'),
    path('solicitud_insumo/edit/<int:pk>', login_required(SolicitudDonacionInsumoEdit.as_view()), name='solicitud_insumo_edit'),

    path('donacion_monetaria/new', login_required(DonacionMonetariaNew.as_view()), name='donacion_monetaria_new'),
    path('donacion_insumo/new', login_required(DonacionInsumoNew.as_view()), name='donacion_insumo_new'),
    path('donacion_monetaria/delete/<int:pk>', login_required(DonacionMonetariaDel.as_view()), name='donacion_monetaria_del'),
    path('donacion_insumo/delete/<int:pk>', login_required(DonacionInsumoDel.as_view()), name='donacion_insumo_del'),
    path('donacion_monetaria/edit/<int:pk>', login_required(DonacionMonetariaEdit.as_view()), name='donacion_monetaria__edit'),
    path('donacion_insumo/edit/<int:pk>', login_required(DonacionInsumoEdit.as_view()), name='donacion_insumo__edit'),

]