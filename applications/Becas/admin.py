# becas/admin.py
from django.contrib import admin
from .models import Encargado

@admin.register(Encargado)
class EncargadoBecaAdmin(admin.ModelAdmin):
    list_display = ('idEncargado', 'nombreEncargado', 'numeroTrabajador', 'bActivo')
    search_fields = ('nombreEncargado', 'numeroTrabajador')
    list_filter = ('bActivo',)
    ordering = ('idEncargado',)
