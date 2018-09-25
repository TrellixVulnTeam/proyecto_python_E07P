from django.shortcuts import render, redirect 
from .models import *
from .forms import *

# Create your views here.
def vista_index(request):
	return render(request,'index.html')

def vista_lista_pelicula (request):
	lista = Pelicula.objects.filter()
	return render(request, 'lista_pelicula.html',locals())

def vista_agregar_pelicula(request):
	if request.method == 'POST':
		formulario = agregar_pelicula_form(request.POST, request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit = False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/lista_pelicula/')

	else:
		formulario = agregar_pelicula_form()
	return render(request, 'agregar_pelicula.html', locals())

def vista_editar_pelicula(request, id_prod):
	prod = Pelicula.objects.get(id=id_prod)
	if request.method == 'POST':
		formulario = agregar_pelicula_form(request.POST, request.FILES, instance=prod)
		if formulario.is_valid():
			prod = formulario.save()
			return redirect ('/lista_pelicula/')
	else:
		formulario = agregar_pelicula_form(instance = prod)
	return render(request, 'agregar_pelicula.html', locals())

def vista_eliminar_pelicula(request, id_prod):
	prod = Pelicula.objects.get(id=id_prod)
	prod.delete()
	return redirect ('/lista_pelicula/')