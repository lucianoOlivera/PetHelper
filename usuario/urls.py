from django.urls import path
from django.contrib.auth.decorators import login_required
from usuario.views import RegistroUsuario, UsuarioDetail, UsuarioEdit

urlpatterns = [
      path('registrar/', RegistroUsuario.as_view(), name='registrar'),
      path('usuario/profile/<int:pk>', login_required(UsuarioDetail.as_view()), name='usuario_profile'),
      path('usuario/editar/<int:pk>', login_required(UsuarioEdit.as_view()), name='usuario_edit') 
]
