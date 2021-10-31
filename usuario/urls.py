from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from usuario.views import RegistroUsuario, UsuarioDetail, UsuarioEdit, UsuarioPasswordEdit, UsuarioPasswordReset, UsuarioPasswordResetComplete, UsuarioPasswordResetConfirm, UsuarioPasswordResetDone

urlpatterns = [
      path('registrar/', RegistroUsuario.as_view(), name='registrar'),
      path('usuario/profile/<int:pk>', login_required(UsuarioDetail.as_view()), name='usuario_profile'),
      path('usuario/editar/<int:pk>', login_required(UsuarioEdit.as_view()), name='usuario_edit'),
      path('usuario/cambiar_contraseña/', login_required(UsuarioPasswordEdit.as_view()), name='usuario_cambiar_contraseña'),
      path('resetear_contraseña/', UsuarioPasswordReset.as_view(), name='resetear_contraseña'),
      path('resetear_contraseña_confirm/<uidb64>/<token>', UsuarioPasswordResetConfirm.as_view(), name='password_reset_confirm'),
      path('resetear_contraseña_sent/', UsuarioPasswordResetDone.as_view(), name='password_reset_done'),
      path('resetear_contraseña_complete/', UsuarioPasswordResetComplete.as_view(), name='password_reset_complete'),
]
