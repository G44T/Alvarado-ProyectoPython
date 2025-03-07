from django.shortcuts import render, redirect
from django.utils import timezone
from productos.models import Producto
from tienda.models import Carrito
from productos.forms import BuscarProducto
from tienda.forms import Modificar_Cantidad_Form
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def lista_productos(request):
    productos = Producto.objects.all()
    formulario = BuscarProducto(request.GET)

    if formulario.is_valid():
        nombre_buscar = formulario.cleaned_data.get("nombre")
        categoria_buscar = formulario.cleaned_data.get("categoria")

        if nombre_buscar != "" and categoria_buscar == "":
            productos = Producto.objects.filter(nombre__icontains=nombre_buscar)
        elif nombre_buscar == "" and categoria_buscar != "":
            productos = Producto.objects.filter(categoria__icontains=categoria_buscar)
        elif nombre_buscar != "" and categoria_buscar != "":
            productos = Producto.objects.filter(
                nombre__icontains=nombre_buscar, categoria__icontains=categoria_buscar
            )

    return render(
        request,
        "lista_productos.html",
        {"Productos": productos, "formulario": formulario},
    )


def lista_detalle_producto(request, producto_id):

    productos = Producto.objects.get(id=producto_id)
    return render(request, "lista_detalle_producto.html", {"Producto": productos})


def agregar_carrito(request, producto_id):
    productos = Producto.objects.get(id=producto_id)

    if productos:
        nombre = productos.nombre
        categoria = productos.categoria
        precio = productos.precio
        precio_dolares = productos.precio_dolares
        fecha_compra = timezone.now().date()

        carrito = Carrito(
            nombre=nombre,
            categoria=categoria,
            precio=precio,
            precio_dolares=precio_dolares,
            fecha_compra=fecha_compra,
        )

        carrito.save()

    return redirect("lista_productos")


def lista_carrito(request):
    carrito = Carrito.objects.all()

    return render(request, "lista_carrito.html", {"Carritos": carrito})


class Modificar_Carrito_View(LoginRequiredMixin, UpdateView):
    model = Carrito
    template_name = "modificar_carrito.html"
    form_class = Modificar_Cantidad_Form
    success_url = reverse_lazy("lista_carrito")


class Eliminar_Carrito_View(LoginRequiredMixin, DeleteView):
    model = Carrito
    template_name = "eliminar_carrito.html"
    success_url = reverse_lazy("lista_carrito")
