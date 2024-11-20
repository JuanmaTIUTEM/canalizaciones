# pedagogos/admin.py
from django.contrib import admin
from .models import Pedagogo

@admin.register(Pedagogo)
class PedagogoAdmin(admin.ModelAdmin):
    list_display = ('idPedagogo', 'nombrePedagogo', 'numeroTrabajador', 'bActivo')
    search_fields = ('nombrePedagogo', 'numeroTrabajador')
    list_filter = ('bActivo',)
    ordering = ('idPedagogo',)
