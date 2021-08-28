from organizaciones.models import Veterinario
from django.urls import path

from .views import OrganizacionView, OrganizacionNew, OrganizacionDel, OrganizacionEdit, ClinicaView, ClinicaNew, ClinicaDel, ClinicaEdit, VeterinarioView, VeterinarioNew, VeterinarioDel, VeterinarioEdit

urlpatterns = [
    path('organizaciones/', OrganizacionView.as_view(), name='organizaciones_list'),
    path('organizaciones/new', OrganizacionNew.as_view(), name='organizaciones_new'),
    path('organizaciones/delete/<int:pk>', OrganizacionDel.as_view(), name='organizaciones_del'),
    path('organizaciones/edit/<int:pk>', OrganizacionEdit.as_view(), name='organizaciones_edit'),
    path('clinicas/', ClinicaView.as_view(), name='clinicas_list'),
    path('clinicas/new', ClinicaNew.as_view(), name='clinicas_new'),
    path('clinicas/delete/<int:pk>', ClinicaDel.as_view(), name='clinicas_del'),
    path('clinicas/edit/<int:pk>', ClinicaEdit.as_view(), name='clinicas_edit'),
    path('veterinarios/', VeterinarioView.as_view(), name='veterinarios_list'),
    path('veterinarios/new', VeterinarioNew.as_view(), name='veterinarios_new'),
    path('veterinarios/delete/<int:pk>', VeterinarioDel.as_view(), name='veterinarios_del'),
    path('veterinarios/edit/<int:pk>', VeterinarioEdit.as_view(), name='veterinarios_edit'),

]