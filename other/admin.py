from django.contrib import admin
from .models import *


@admin.register(TipoComision)
class TipoComisionAdmin(admin.ModelAdmin):
    pass


@admin.register(SubtipoComision)
class SubtipoComisionAdmin(admin.ModelAdmin):
    pass
