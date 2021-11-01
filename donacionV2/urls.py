   
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import DonacionInsumoNew


urlpatterns = [
    path('donacion_insumo/new/<int:pk>', login_required(DonacionInsumoNew.as_view()), name='donacion_insumo_new'),
]
