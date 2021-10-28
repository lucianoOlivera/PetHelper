from django.contrib.auth.decorators import login_required
from django.urls.conf import path

from .views import MapaList

urlpatterns = [
    path('mapa/', login_required(MapaList.as_view()), name='mapa_new'),
]
