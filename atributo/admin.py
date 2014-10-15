from django.contrib import admin
from .models import *


@admin.register(AtributoCliente)
class AtributoClienteAdmin(admin.ModelAdmin):
    pass


@admin.register(AtributoMaterial)
class AtributoMaterialAdmin(admin.ModelAdmin):
    list_display = ['material','sector','nivel2','nivel3']
    list_filter = ['sector', 'nivel2']
    search_fields = ['sector']


@admin.register(AtributoInterlocutor)
class AtributoInterlocutorAdmin(admin.ModelAdmin):
    pass
