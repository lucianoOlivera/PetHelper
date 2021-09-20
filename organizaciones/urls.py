from organizaciones.models import Veterinario
from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import OrganizacionView, OrganizacionNew, OrganizacionDel, OrganizacionEdit, ClinicaView, ClinicaNew, ClinicaDel, ClinicaEdit, VeterinarioView, VeterinarioNew, VeterinarioDel, VeterinarioEdit, VeterinarioClinicaView

urlpatterns = [
    path('organizaciones/', login_required(OrganizacionView.as_view()), name='organizaciones_list'),
    path('organizaciones/new', login_required(OrganizacionNew.as_view()), name='organizaciones_new'),
    path('organizaciones/delete/<int:pk>', login_required(OrganizacionDel.as_view()), name='organizaciones_del'),
    path('organizaciones/edit/<int:pk>', login_required(OrganizacionEdit.as_view()), name='organizaciones_edit'),
    path('clinicas/', login_required(ClinicaView.as_view()), name='clinicas_list'),
    path('clinicas/new', login_required(ClinicaNew.as_view()), name='clinicas_new'),
    path('clinicas/delete/<int:pk>', login_required(ClinicaDel.as_view()), name='clinicas_del'),
    path('clinicas/edit/<int:pk>', login_required(ClinicaEdit.as_view()), name='clinicas_edit'),
    path('veterinarios/', login_required(VeterinarioView.as_view()), name='veterinarios_list'),
    path('veterinarios/new', login_required(VeterinarioNew.as_view()), name='veterinarios_new'),
    path('veterinarios/delete/<int:pk>', login_required(VeterinarioDel.as_view()), name='veterinarios_del'),
    path('veterinarios/edit/<int:pk>', login_required(VeterinarioEdit.as_view()), name='veterinarios_edit'),
    path('profesionales/', login_required(VeterinarioClinicaView.as_view()), name='profesionales_list'),
]