from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from usuario.views import RegistroUsuario, UsuarioDetail, UsuarioEdit, UsuarioPasswordEdit

urlpatterns = [
      path('registrar/', RegistroUsuario.as_view(), name='registrar'),
      path('usuario/profile/<int:pk>', login_required(UsuarioDetail.as_view()), name='usuario_profile'),
      path('usuario/editar/<int:pk>', login_required(UsuarioEdit.as_view()), name='usuario_edit'),
      path('usuario/cambiar_password/', login_required(UsuarioPasswordEdit.as_view()), name='usuario_cambiar_contraseña'),
]
