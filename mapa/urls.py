from django.contrib.auth.decorators import login_required
from django.urls.conf import path

from .views import MapaClinicasList, MapaList, MapaOrganizacionesList, MapaVeterinariosList

urlpatterns = [
    path('mapa/', login_required(MapaList.as_view()), name='mapa_list'),
    path('mapa/veterinarios', login_required(MapaVeterinariosList.as_view()), name='mapa_veterinarios'),
    path('mapa/clinicas', login_required(MapaClinicasList.as_view()), name='mapa_clinicas'),
    path('mapa/organizaciones', login_required(MapaOrganizacionesList.as_view()), name='mapa_organizaciones'),
]
