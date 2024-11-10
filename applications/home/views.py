from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.

class IndexView(TemplateView):
	#atributos de clase
	template_name = 'home.html'