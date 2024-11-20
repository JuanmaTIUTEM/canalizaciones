# docentes/admin.py
from django.contrib import admin
from .models import Docente

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('idDocente', 'nombreDocente', 'numeroTrabajador', 'bActivo')
    search_fields = ('nombreDocente', 'numeroTrabajador')
    list_filter = ('bActivo',)
    ordering = ('idDocente',)
