from django.urls import path
from productos.views import *

urlpatterns = [
    path('',inicio, name='inicio'),
    path('registrar-producto/', registrar_producto, name='registrar_producto'),
    path('acerca-de-mi/about', about, name='about'),
    path('mostrar-producto/', mostrar_producto, name='mostrar_producto'),
    path('modificar-producto/<int:producto_id>', modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<int:producto_id>', eliminar_producto, name='eliminar_producto'),
    path('detalle-producto/<int:producto_id>', detalle_producto, name='detalle_producto'),
]
