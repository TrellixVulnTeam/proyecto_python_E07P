from django import forms
from .models import *

class agregar_pelicula_form(forms.ModelForm):
	class Meta:
		model = Pelicula
		fields = '__all__'

