from django.http import Httpresponse

def index(request):
	return Httpresponse("Hola desde archivo Python")