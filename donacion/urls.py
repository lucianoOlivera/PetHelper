from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import SolicitudDonacionMonetariaView, SolicitudDonacionMonetariaNew, SolicitudDonacionMonetariaDel, SolicitudDonacionMonetariaEdit, SolicitudDonacionInsumoView, SolicitudDonacionInsumoNew, SolicitudDonacionInsumoDel, SolicitudDonacionInsumoEdit

urlpatterns = [
    path('solicitudes/', login_required(SolicitudDonacionMonetariaView.as_view(), SolicitudDonacionInsumoView.as_view()), name='solicitudes_list'),
    path('solicitud_monetaria/new', login_required(SolicitudDonacionMonetariaNew.as_view()), name='solicitud_monetaria_new'),
    path('solicitud_insumo/new', login_required(SolicitudDonacionInsumoNew.as_view()), name='solicitud_insumo_new'),
    path('solicitud_monetaria/delete/<int:pk>', login_required(SolicitudDonacionMonetariaDel.as_view()), name='solicitud_monetaria_del'),
    path('solicitud_insumo/delete/<int:pk>', login_required(SolicitudDonacionInsumoDel.as_view()), name='solicitud_insumo_del'),
    path('solicitud_monetaria/edit/<int:pk>', login_required(SolicitudDonacionMonetariaEdit.as_view()), name='solicitud_monetaria__edit'),
    path('solicitud_insumo/edit/<int:pk>', login_required(SolicitudDonacionInsumoEdit.as_view()), name='solicitud_insumo_edit'),

]