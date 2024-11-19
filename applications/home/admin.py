from django.contrib import admin
#importar modelo
from .models import Edades
# Register your models here.
#codigo para interactuar con base de datos

admin.site.register(Edades)


#para que se pueda visualizar el usuario debemos generar un nuevo usuario:
#python manage.py createsuperuser
#:user
#:pass