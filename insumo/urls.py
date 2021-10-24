from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import InsumoView, InsumoNew, InsumoDel, CantidadInsumoNew, CantdadIsumoList

urlpatterns = [
    path('insumos/', login_required(InsumoView.as_view()), name='insumo_list'),
    path('insumo/new', login_required(InsumoNew.as_view()), name='insumo_new'),
    path('insumo/delete/<int:pk>', login_required(InsumoDel.as_view()), name='insumo_del'),
    path('cantidad_insumo/new', login_required(CantidadInsumoNew.as_view()), name='cantidad_insumo_new'),
    path('cantidad_insumo/', login_required(CantdadIsumoList.as_view()), name='cantidad_insumo_list')
    ]