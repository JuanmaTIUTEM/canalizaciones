from django.db import models

# Create your models here.

class Edades(models.Model):
	nombre = models.CharField(max_length = 30)
	apellidos = models.CharField(max_length = 50)
	edad = models.IntegerField()

#revisar si hay algun cambio en los modelos: python manage.py makemigrations
#crear tabla en BD conectada: python manage.py migrate
