from django.db import models
from text.models import *


class AtributoCliente(models.Model):
    cliente = models.ForeignKey(Cliente, primary_key=True, null=False, db_column='/BIC/ZCUSTOMER')
    rut = models.CharField(max_length=11, null=True, db_column='TAX_NUMB2')
    direccion = models.CharField(max_length=35, null=True, db_column='STREET')
    poblacion = models.CharField(max_length=35, null=True, db_column='CITY')
    cadena = models.CharField(max_length=3, null=True, db_column='/BIC/ZCADENA')
    subcadena = models.CharField(max_length=3, null=True, db_column='/BIC/ZSBCADENA')
    zonaReparto = models.CharField(max_length=10, null=True, db_column='/BIC/ZLZONE', verbose_name='Zona de Reporte')
    tipoCliente = models.CharField(max_length=2, null=True, db_column='/BIC/ZTIPCL', verbose_name='Tipo de Cliente')
    subtipoCliente = models.CharField(max_length=2, null=True, db_column='/BIC/ZSUBTICL', verbose_name='Subtipo de Cliente')
    oficinaVentas = models.CharField(max_length=4, null=True, db_column='SALES_OFF', verbose_name='Oficina de Ventas')
    zonaVentas = models.CharField(max_length=6, null=True, db_column='SALES_DIST', verbose_name='Zona de Ventas')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHCLIATT'
        verbose_name = 'Atributo de Cliente'
        verbose_name_plural = 'Atributos de Clientes'


class AtributoMaterial(models.Model):
    material = models.ForeignKey(Material, primary_key=True, null=False, db_column='/BIC/ZMATERIAL')
    sector = models.CharField(max_length=5, null=True, db_column='/BIC/ZITORIGEN')
    grupoArticulo = models.CharField(max_length=18, null=True, db_column='EXTMATLGRP', verbose_name='Grupo Articulo')
    nivel1 = models.CharField(max_length=9, null=True, db_column='RPA_WGH1')
    nivel2 = models.CharField(max_length=9, null=True, db_column='RPA_WGH2')
    nivel3 = models.CharField(max_length=9, null=True, db_column='RPA_WGH3')
    nivel4 = models.CharField(max_length=11, null=True, db_column='RPA_WGH4')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHMATATT'
        verbose_name = 'Atributo de Material'
        verbose_name_plural = 'Atributos de Materiales'

    def __unicode__(self):
        return self.material.codigo


class AtributoInterlocutor(models.Model):
    interlocutor = models.ForeignKey(Cliente, primary_key=True, null=False, db_column='/BIC/ZCUSTOMER')
    rut = models.CharField(max_length=11, null=True, db_column='TAX_NUMB2')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHINTEAT'
        verbose_name = 'Atributo de Interlocutor'
        verbose_name_plural = 'Atributos de Interlocutores'

    def __unicode__(self):
        return self.interlocutor.cliente