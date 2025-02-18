from django.shortcuts import render, redirect
from productos.models import Producto
from productos.forms import *


# Create your views here.
def inicio(request):
    # return HttpResponse("<h1>Hola soy la vista!</h1>")

    return render(request, "inicio.html")


def registrar_producto(request):

    formulario = RegistrarProducto()

    if request.method == "POST":
        formulario = RegistrarProducto(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get("nombre")
            descripcion = formulario.cleaned_data.get("descripcion")
            categoria = formulario.cleaned_data.get("categoria")
            precio = formulario.cleaned_data.get("precio")
            precio_dolares = formulario.cleaned_data.get("precio_dolares")

            producto = Producto(
                nombre=nombre,
                descripcion=descripcion,
                categoria=categoria,
                precio=precio,
                precio_dolares=precio_dolares,
            )

            producto.save()

            return redirect("mostrar_producto")

    return render(request, "registrar_producto.html", {"formulario": formulario})


def mostrar_producto(request):

    Productos = Producto.objects.all()

    formulario = BuscarAuto(request.GET)
    
    if formulario.is_valid():
        nombre_buscar = formulario.cleaned_data.get("nombre")
        categoria_buscar = formulario.cleaned_data.get("categoria")
        
        if nombre_buscar!="" and categoria_buscar=="":
            Productos = Producto.objects.filter(nombre__icontains=nombre_buscar)
        elif nombre_buscar=="" and categoria_buscar!="":
            Productos = Producto.objects.filter(categoria__icontains=categoria_buscar)
        elif nombre_buscar!="" and categoria_buscar!="":
            Productos = Producto.objects.filter(nombre__icontains=nombre_buscar, categoria__icontains=categoria_buscar)
    return render(
        request,
        "mostrar_producto.html",
        {"Productos": Productos, "formulario": formulario},
    )
