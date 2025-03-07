from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User

class Login_Forms(AuthenticationForm):
    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    
    class Meta:
        model = User
        fields = ['username','password']
        
class Registro_Usuario_Forms(UserCreationForm):
    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {field: '' for field in fields}
        
class Perfil_Usuario_Forms(forms.ModelForm):
    
    class Meta:
        model = User
        fields = "__all__"

class Editar_Usuario_Forms(UserChangeForm):
    
    password = None
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={"class": "form-control"}))    
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    avatar = forms.ImageField(required=False)
    fechra_nacimiento = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date',"class": "form-control"}))
    
    class Meta:
        model = User
        fields = ['email', 'first_name','last_name','fechra_nacimiento','avatar']

class Editar_Contrasenia_Forms(PasswordChangeForm):
    
    old_password  = forms.CharField(label='Contraseña Antigua',widget=forms.PasswordInput(attrs={"class": "form-control"}))
    new_password1  = forms.CharField(label='Nueva Contraseña',widget=forms.PasswordInput(attrs={"class": "form-control"}))
    new_password2 = forms.CharField(label='Repetir Nueva Contraseña',widget=forms.PasswordInput(attrs={"class": "form-control"}))
    
    class Meta:
        model = User
        fields = ['old_password', 'new_password1','new_password2']
    