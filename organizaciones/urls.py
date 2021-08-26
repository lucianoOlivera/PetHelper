from django.urls import path

from .views import OrganizacionView, OrganizacionNew, OrganizacionDel, OrganizacionEdit, ClinicaView, ClinicaNew, ClinicaDel, ClinicaEdit

urlpatterns = [
    path('organizaciones/', OrganizacionView.as_view(), name='organizaciones_list'),
    path('organizaciones/new', OrganizacionNew.as_view(), name='organizaciones_new'),
    path('organizaciones/delete/<int:pk>', OrganizacionDel.as_view(), name='organizaciones_del'),
    path('organizaciones/edit/<int:pk>', OrganizacionEdit.as_view(), name='organizaciones_edit'),
    path('clinicas/', ClinicaView.as_view(), name='clinicas_list'),
    path('clinicas/new', ClinicaNew.as_view(), name='clinicas_new'),
    path('clinicas/delete/<int:pk>', ClinicaDel.as_view(), name='clinicas_del'),
    path('clinicas/edit/<int:pk>', ClinicaEdit.as_view(), name='clinicas_edit'),

]