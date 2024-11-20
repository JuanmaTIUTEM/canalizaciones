# grupos/admin.py
from django.contrib import admin
from .models import Grupo

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('idGrupo', 'cveGrupo', 'nombreGrupo', 'cuatrimestreGrupo', 'aulaNombre', 'aulaUbicacion', 'bActivo')
    search_fields = ('cveGrupo', 'nombreGrupo')
    list_filter = ('bActivo',)
    ordering = ('idGrupo',)
