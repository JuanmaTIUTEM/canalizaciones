# carreras/admin.py
from django.contrib import admin
from .models import Carrera

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('idCarrera', 'cveCarrera', 'nombreCarrera', 'areaCarrera', 'planEstudios', 'bActivo')
    search_fields = ('cveCarrera', 'nombreCarrera', 'areaCarrera')
    list_filter = ('bActivo',)
    ordering = ('idCarrera',)
