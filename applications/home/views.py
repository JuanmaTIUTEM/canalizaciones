from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from django.http import HttpResponse

# Create your views here.

class IndexView(TemplateView):
	#atributos de clase
	template_name = 'home.html'

class PruebaLista(ListView):
	#atributos de clase
	template_name = 'lista.html'
	queryset = ['A','B','C','D']
	context_object_name = 'lista_prueba'

def mostrar_tabla(request):
    # Datos proporcionados
    nombres = ["Juan", "María", "Carlos", "Ana", "Luis"]
    apellidos = ["Pérez", "González", "Ramírez", "López", "Martínez"]
    edades = [25, 30, 22, 28, 35]

    # Combinar los arrays en una lista de diccionarios
    personas = []
    for i in range(len(nombres)):
        persona = {
            'nombre': nombres[i],
            'apellido': apellidos[i],
            'edad': edades[i]
        }
        personas.append(persona)

    # Pasar los datos a la plantilla
    return render(request, 'mostrar_tabla.html', {'personas': personas})
