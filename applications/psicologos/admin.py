# psicologos/admin.py
from django.contrib import admin
from .models import Psicologo

@admin.register(Psicologo)
class PsicologoAdmin(admin.ModelAdmin):
    list_display = ('idPsicologo', 'nombrePsicologo', 'numeroTrabajador', 'bActivo')
    search_fields = ('nombrePsicologo', 'numeroTrabajador')
    list_filter = ('bActivo',)
    ordering = ('idPsicologo',)
