from django.urls import path, include
from bases.views import Home, HomeSinPrivilegios
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path
    ('login/',
     auth_views.LoginView.as_view(template_name='bases/login.html'),
     name='login'),
    path
    ('logout/',
     auth_views.LogoutView.as_view(template_name='bases/login.html'),
     name='logout'),
    path('oauth/', include(('social_django.urls', 'social'), namespace='social')),
    path('sin_privilegios/', HomeSinPrivilegios.as_view(), name='sin_privilegios'),
]
