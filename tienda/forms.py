from django import forms
from .models import Carrito


class Modificar_Cantidad_Form(forms.ModelForm):    
    
    class Meta:
        model = Carrito
        fields = ["cantidad"]
        widgets = {
            "cantidad": forms.TextInput(attrs={"class": "form-control"}),
        }
        
