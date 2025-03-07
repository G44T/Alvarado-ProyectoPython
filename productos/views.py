from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from productos.models import Producto
from productos.forms import *


# Create your views here.
def inicio(request):
    # return HttpResponse("<h1>Hola soy la vista!</h1>")

    return render(request, "inicio.html")


@login_required
def registrar_producto(request):

    formulario = RegistrarProducto()

    if request.method == "POST":
        formulario = RegistrarProducto(request.POST, request.FILES)
                
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get("nombre")
            descripcion = formulario.cleaned_data.get("descripcion")
            categoria = formulario.cleaned_data.get("categoria")
            precio = formulario.cleaned_data.get("precio")
            precio_dolares = formulario.cleaned_data.get("precio_dolares")
            productos_img = formulario.cleaned_data.get("productos_img")                       

            producto = Producto(
                nombre=nombre,
                descripcion=descripcion,
                categoria=categoria,
                precio=precio,
                precio_dolares=precio_dolares,
                productos_img=productos_img
            )
            
            producto.save()

            return redirect("mostrar_producto")

    return render(request, "registrar_producto.html", {"formulario": formulario})


def mostrar_producto(request):

    Productos = Producto.objects.all()
    formulario = BuscarProducto(request.GET)

    if formulario.is_valid():
        nombre_buscar = formulario.cleaned_data.get("nombre")
        categoria_buscar = formulario.cleaned_data.get("categoria")

        if nombre_buscar != "" and categoria_buscar == "":
            Productos = Producto.objects.filter(nombre__icontains=nombre_buscar)
        elif nombre_buscar == "" and categoria_buscar != "":
            Productos = Producto.objects.filter(categoria__icontains=categoria_buscar)
        elif nombre_buscar != "" and categoria_buscar != "":
            Productos = Producto.objects.filter(
                nombre__icontains=nombre_buscar, categoria__icontains=categoria_buscar
            )
    return render(
        request,
        "mostrar_producto.html",
        {"Productos": Productos, "formulario": formulario},
    )


@login_required
def eliminar_producto(request, producto_id):
    Productos = Producto.objects.get(id=producto_id)
    Productos.delete()
    return redirect("mostrar_producto")


def detalle_producto(request, producto_id):
    Productos = Producto.objects.get(id=producto_id)
    return render(request, "detalle_producto.html", {"Producto": Productos})


@login_required
def modificar_producto(request, producto_id):

    Productos = Producto.objects.get(id=producto_id)

    if request.method == "POST":
        formulario = ModificarProducto(request.POST, request.FILES, instance=Productos)
        if formulario.is_valid():
            formulario.save()
            return redirect("mostrar_producto")
    else:
        formulario = ModificarProducto(instance=Productos)

    return render(request, "modificar_producto.html", {"formulario": formulario, 'producto': Productos})


def about(request):
    return render(request, "about.html")
