from django.urls import path
from tienda.views import lista_productos, lista_detalle_producto, agregar_carrito, lista_carrito, Modificar_Carrito_View, Eliminar_Carrito_View
 
urlpatterns = [
    path('lista-productos/', lista_productos, name='lista_productos'),
    path('lista-detalle-producto/<int:producto_id>', lista_detalle_producto, name='lista_detalle_producto'),
    path('agregar-carrito/<int:producto_id>', agregar_carrito, name='agregar_carrito'),
    path('lista-carrito/', lista_carrito, name='lista_carrito'),
    path('modificar-carrito/<int:pk>', Modificar_Carrito_View.as_view(), name='modificar_carrito'),
    path('eliminar-carrito/<int:pk>', Eliminar_Carrito_View.as_view(), name='eliminar_carrito')
]
