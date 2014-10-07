from django.contrib import admin

from .models import *


@admin.register(Cadena)
class CadenaAdmin(admin.ModelAdmin):
    pass


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass


@admin.register(GrupoArticulo)
class GrupoArticuloAdmin(admin.ModelAdmin):
    pass


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    pass


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(Nivel1)
class Nivel1Admin(admin.ModelAdmin):
    pass


@admin.register(Nivel2)
class Nivel2Admin(admin.ModelAdmin):
    pass


@admin.register(Nivel3)
class Nivel3Admin(admin.ModelAdmin):
    pass


@admin.register(Nivel4)
class Nivel4Admin(admin.ModelAdmin):
    pass


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    pass


@admin.register(Subcadena)
class SubcadenaAdmin(admin.ModelAdmin):
    pass


@admin.register(SubtipoCliente)
class SubtipoClienteAdmin(admin.ModelAdmin):
    pass


@admin.register(TipoCliente)
class TipoClienteAdmin(admin.ModelAdmin):
    pass


@admin.register(ZonaReparto)
class ZonaRepartoAdmin(admin.ModelAdmin):
    pass


@admin.register(ZonaVentas)
class ZonaVentasAdmin(admin.ModelAdmin):
    pass


@admin.register(OficinaVentas)
class OficinaVentasAdmin(admin.ModelAdmin):
    pass


@admin.register(AtributoCliente)
class AtributoClienteAdmin(admin.ModelAdmin):
    pass


@admin.register(AtributoMaterial)
class AtributoMaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(NivelServicio)
class NivelServicioAdmin(admin.ModelAdmin):
    pass


@admin.register(VentaDiaria)
class VentaDiariaAdmin(admin.ModelAdmin):
    pass