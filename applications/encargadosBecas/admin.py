# encargadosbecas/admin.py
from django.contrib import admin
from .models import EncargadoBeca

@admin.register(EncargadoBeca)
class EncargadoBecaAdmin(admin.ModelAdmin):
    list_display = ('idEncargado', 'nombreEncargado', 'numeroTrabajador', 'bActivo')
    search_fields = ('nombreEncargado', 'numeroTrabajador')
    list_filter = ('bActivo',)
    ordering = ('idEncargado',)
