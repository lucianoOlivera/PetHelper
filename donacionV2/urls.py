from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import DonacionInsumoNew, DonacionmonetariaNew, MedioPagoNew, MedioPagoView, MedioPagoDel


urlpatterns = [
    path('donacion_insumo/new/<int:pk>', login_required(DonacionInsumoNew.as_view()), name='donacion_insumo_new'),

    path('donacion_monetaria/new/<int:pk>', login_required(DonacionmonetariaNew.as_view()), name='donacion_monetaria_new'),

    path('medioPago/', login_required(MedioPagoView.as_view()), name='medioPago_list'),
    path('medioPago/new', login_required(MedioPagoNew.as_view()), name='medioPago_new'),
    path('medioPago/delete/<int:pk>', login_required(MedioPagoDel.as_view()), name='medioPago_del'),
]
