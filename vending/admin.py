from django.contrib import admin
from .models import NivelServicio


@admin.register(NivelServicio)
class NivelServicioAdmin(admin.ModelAdmin):
    pass
