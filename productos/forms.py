from django import forms


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


class BuscarAuto(forms.Form):
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
