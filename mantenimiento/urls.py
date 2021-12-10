from django.urls import path
from mantenimiento import views
from .views import BackupView, RestoreView


urlpatterns = [
    path('mantenimiento/', BackupView.as_view(), name='backups'),
    path('restore/', RestoreView.as_view(), name="restore"),
]