from django.urls import path
from usuarios.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',login, name='login'),
    path('logout/',LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('registro-usuario/',registro_usuario, name='registro_usuario'),
    path('editar-usuario/', editar_usuario, name='editar_usuario'),
    path('editar-usuario/editar-contrasenia/', editar_contrasenia.as_view(), name='editar_contrasenia'),
    path('perfil-usuario/',perfil_usuario,name='perfil_usuario')
]
