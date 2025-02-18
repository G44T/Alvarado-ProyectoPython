from django.urls import path
from productos.views import *

urlpatterns = [
    path('',inicio, name='inicio'),
    path('registrar-producto/', registrar_producto, name='registrar_producto'),
    path('mostrar-producto/', mostrar_producto, name='mostrar_producto'),
]
