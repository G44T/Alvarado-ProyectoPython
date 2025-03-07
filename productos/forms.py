from django import forms
from productos.models import Producto


class RegistrarProducto(forms.Form):
    nombre = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"}), required=False
    )
    categoria = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    precio = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    precio_dolares = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    productos_img = forms.ImageField(
        required=False
    )


class BuscarProducto(forms.Form):
    nombre = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False,
    )
    categoria = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False,
    )


class ModificarProducto(forms.ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control"}),
            "categoria": forms.TextInput(attrs={"class": "form-control"}),
            "precio": forms.TextInput(attrs={"class": "form-control"}),
            "precio_dolares": forms.TextInput(attrs={"class": "form-control"}),
        }
