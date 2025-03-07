from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login
from django.contrib.auth import get_user_model
from usuarios.forms import (Login_Forms, Registro_Usuario_Forms, Editar_Usuario_Forms, Editar_Contrasenia_Forms)
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import InfoExtra

# Create your views here.


def login(request):
    if request.method == "POST":
        formulario = Login_Forms(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()

            django_login(request, usuario)

            InfoExtra.objects.get_or_create(user=usuario)

            return redirect("inicio")
    else:
        formulario = Login_Forms()

    return render(request, "usuarios/login.html", {"formulario": formulario})


def perfil_usuario(request):
    
    info_extra = request.user.infoextra
        
    return render(request, "usuarios/perfil-usuario.html", {"usuario": request.user,"info_extra":info_extra})


def registro_usuario(request):
    if request.method == "POST":
        formulario = Registro_Usuario_Forms(request.POST)
        if formulario.is_valid():
            formulario.save()

            return redirect("login")
    else:
        formulario = Registro_Usuario_Forms()

    return render(request, "usuarios/registro_usuario.html", {"formulario": formulario})


def editar_usuario(request):

    info_extra = request.user.infoextra

    if request.method == "POST":
        formulario = Editar_Usuario_Forms(
            request.POST, request.FILES, instance=request.user
        )
        if formulario.is_valid():

            if formulario.cleaned_data.get("avatar"):
                info_extra.avatar = formulario.cleaned_data.get("avatar")
                print(formulario.cleaned_data.get("avatar"))
                
            info_extra.fechra_nacimiento = formulario.cleaned_data.get("fechra_nacimiento")
                        
            info_extra.save()
            formulario.save()

            return redirect("inicio")
    else:
        formulario = Editar_Usuario_Forms(
            instance=request.user, initial={"avatar": info_extra.avatar, "fechra_nacimiento": info_extra.fechra_nacimiento}
        )

    return render(request, "usuarios/editar_usuario.html", {"formulario": formulario})


class editar_contrasenia(PasswordChangeView):
    template_name = "usuarios/editar-contrasenia.html"
    success_url = reverse_lazy("inicio")
    form_class = Editar_Contrasenia_Forms
    success_message = "Tu contraseña ha sido actualizada exitosamente."
