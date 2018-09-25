from django.db import models

# Create your models here.

class Genero (models.Model):
	nombre	=models.CharField(max_length = 100)
	descripcion	= models.TextField(max_length = 500)

	def __str__(self):
		return self.nombre

class Director (models.Model):
	nombre	= models.CharField(max_length = 100)
	edad	= models.IntegerField()

	def __str__(self):
		return self.nombre

class Pelicula (models.Model):
	nombre	= models.CharField(max_length = 100)
	año	=	models.IntegerField()
	duracion	=	models.CharField(max_length = 10)
	director	=	models.ForeignKey(Director, on_delete=models.CASCADE)
	genero		=	models.ManyToManyField(Genero, null = True, blank = True)
	imagen		=	models.ImageField(upload_to='../img/', null = True)

	def __str__(self):
		return self.nombre
