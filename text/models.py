from django.db import models


class Cadena(models.Model):
    codigo = models.CharField(primary_key=True, max_length=3, unique=True, db_column='/BIC/ZCADENA', )
    cadena = models.CharField(max_length=40, null=True, db_column='TXTMD')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHCADTXT'

    def __unicode__(self):
        return self.cadena


class Cliente(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10, unique=True, null=False, db_column='/BIC/ZCUSTOMER', )
    cliente = models.CharField(max_length=40, null=True, db_column='TXTMD')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHCLITXT'

    def __unicode__(self):
        return self.cliente


class GrupoArticulo(models.Model):
    codigo = models.CharField(primary_key=True, max_length=18, unique=True, null=False, db_column='EXTMATLGRP', )
    grupoArticulo = models.CharField(max_length=40, null=True, db_column='TXTMD', verbose_name='Grupo Articulo')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHGEXTTX'
        verbose_name = 'Grupo Articulo Externo'
        verbose_name_plural = 'Grupo Articulo Externo'

    def __unicode__(self):
        return self.grupoArticulo


class Marca(models.Model):
    codigo = models.CharField(primary_key=True, max_length=3, unique=True, null=False, db_column='/BIC/ZITMARCA', )
    marca = models.CharField(max_length=20, null=True, db_column='TXTSH')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHMARCTX'

    def __unicode__(self):
        return self.marca


class Material(models.Model):
    codigo = models.CharField(primary_key=True, max_length=18, unique=True, null=False, db_column='/BIC/ZMATERIAL')
    material = models.CharField(max_length=40, null=True, db_column='TXTMD')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHMATTXT'
        verbose_name_plural = 'Materiales'

    def __unicode__(self):
        return self.material


class Nivel1(models.Model):
    codigo = models.CharField(primary_key=True, max_length=9, unique=True, null=False, db_column='RPA_WGH1', )
    nivel1 = models.CharField(max_length=40, null=True, db_column='TXTMD', verbose_name='Nivel 1')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHNIV1TX'
        verbose_name = 'Nivel 1'
        verbose_name_plural = 'Nivel 1'

    def __unicode__(self):
        return self.nivel1


class Nivel2(models.Model):
    codigo = models.CharField(primary_key=True, max_length=9, unique=True, null=False, db_column='RPA_WGH2', )
    nivel2 = models.CharField(max_length=40, null=True, db_column='TXTMD', verbose_name='Nivel 2')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHNIV2TX'
        verbose_name = 'Nivel 2'
        verbose_name_plural = 'Nivel 2'

    def __unicode__(self):
        return self.nivel2


class Nivel3(models.Model):
    codigo = models.CharField(primary_key=True, max_length=9, unique=True, null=False, db_column='RPA_WGH3', )
    nivel3 = models.CharField(max_length=40, null=True, db_column='TXTMD', verbose_name='Nivel 3')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHNIV3TX'
        verbose_name = 'Nivel 3'
        verbose_name_plural = 'Nivel 3'

    def __unicode__(self):
        return self.nivel3


class Nivel4(models.Model):
    codigo = models.CharField(primary_key=True, max_length=11, unique=True, null=False, db_column='RPA_WGH4', )
    nivel4 = models.CharField(max_length=40, null=True, db_column='TXTMD', verbose_name='Nivel 4')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHNIV4TX'
        verbose_name = 'Nivel 4'
        verbose_name_plural = 'Nivel 4'

    def __unicode__(self):
        return self.nivel4


class Sector(models.Model):
    codigo = models.CharField(primary_key=True, max_length=5, unique=True, null=False, db_column='/BIC/ZITORIGEN', )
    sector = models.CharField(max_length=40, null=True, db_column='TXTMD')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHSECTXT'
        verbose_name_plural = 'Sectores'

    def __unicode__(self):
        return self.sector


class Subcadena(models.Model):
    codigo = models.CharField(primary_key=True, max_length=3, unique=True, null=False, db_column='/BIC/ZSBCADENA', )
    subcadena = models.CharField(max_length=40, null=True, db_column='TXTMD')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHSCADTX'

    def __unicode__(self):
        return self.subcadena


class SubtipoCliente(models.Model):
    codigo = models.CharField(primary_key=True, max_length=2, unique=True, null=False, db_column='/BIC/ZSUBTICL', )
    subtipoCliente = models.CharField(max_length=40, null=True, db_column='TXTMD', verbose_name='Subtipo Cliente')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHSTCLIT'
        verbose_name = 'Subtipo Cliente'
        verbose_name_plural = 'Subtipo Cliente'

    def __unicode__(self):
        return self.subtipoCliente


class TipoCliente(models.Model):
    codigo = models.CharField(primary_key=True, max_length=2, unique=True, null=False, db_column='/BIC/ZTIPCL', )
    tipoCliente = models.CharField(max_length=40, null=True, db_column='TXTMD', verbose_name='Tipo Cliente')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHTCLITX'
        verbose_name = 'Tipo Cliente'
        verbose_name_plural = 'Tipo Cliente'

    def __unicode__(self):
        return self.tipoCliente


class ZonaReparto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10, unique=True, null=False, db_column='/BIC/ZLZONE', )
    zonaReparto = models.CharField(max_length=40, null=True, db_column='TXTMD', verbose_name='Zona de Reparto')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHZONRTX'
        verbose_name = 'Zona de Reparto'
        verbose_name_plural = 'Zona de Reparto'

    def __unicode__(self):
        return self.zonaReparto


class ZonaVentas(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6, unique=True, null=False, db_column='SALES_DIST')
    zonaVentas = models.CharField(max_length=20, null=True, db_column='TXTSH', verbose_name='Zona de Ventas')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHZONVTX'
        verbose_name = 'Zona de Ventas'
        verbose_name_plural = 'Zona de Ventas'

    def __unicode__(self):
        return self.zonaVentas


class OficinaVentas(models.Model):
    codigo = models.CharField(primary_key=True, max_length=4, unique=True, null=False, db_column='SALES_OFF')
    oficinaVentas = models.CharField(max_length=40, null=True, db_column='TXTMD', verbose_name='Oficina de Ventas')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHIFVTXT'
        verbose_name = 'Oficina de Ventas'
        verbose_name_plural = 'Oficina de Ventas'

    def __unicode__(self):
        return self.oficinaVentas