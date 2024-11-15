from django.shortcuts import render

from django.views.generic import TemplateView, ListView
# Create your views here.

class IndexView(TemplateView):
	#atributos de clase
	template_name = 'home.html'

class PruebaLista(ListView):
	#atributos de clase
	template_name = 'lista.html'
	queryset = ['A','B','C','D']
	context_object_name = 'lista_prueba'
