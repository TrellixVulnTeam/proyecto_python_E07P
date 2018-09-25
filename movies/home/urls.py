from django.urls import path
from .views import *
from .models import *


urlpatterns = [
	path('index/',vista_index),
	path('lista_pelicula/',vista_lista_pelicula, name='vista_lista_pelicula'),
	path('agregar_pelicula/',vista_agregar_pelicula, name='vista_agregar_pelicula'),
	path('editar_pelicula/<int:id_prod>/', vista_editar_pelicula, name='vista_editar_pelicula'),
	path('eliminar_pelicula/<int:id_prod>/', vista_eliminar_pelicula, name='vista_eliminar_pelicula'),
]