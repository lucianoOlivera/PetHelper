from django.urls import path

from .views import OrganizacionView, OrganizacionNew, OrganizacionDel,OrganizacionEdit

urlpatterns = [
    path('organizaciones/', OrganizacionView.as_view(), name='organizaciones_list'),
    path('organizaciones/new', OrganizacionNew.as_view(), name='organizaciones_new'),
    path('organizaciones/delete/<int:pk>', OrganizacionDel.as_view(), name='organizaciones_del'),
    path('organizaciones/edit/<int:pk>', OrganizacionEdit.as_view(), name='organizaciones_edit'),
]