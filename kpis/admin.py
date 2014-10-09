from django.contrib import admin
from .models import *

@admin.register(NivelServicio)
class NivelServicioAdmin(admin.ModelAdmin):
    pass


@admin.register(VentaDiaria)
class VentaDiariaAdmin(admin.ModelAdmin):
    pass
