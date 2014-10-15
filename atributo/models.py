from django.db import models
from texto.models import *


class AtributoCliente(models.Model):
    cliente = models.ForeignKey(Cliente, primary_key=True, null=False, db_column='/BIC/ZCUSTOMER')
    rut = models.CharField(max_length=11, null=True, db_column='TAX_NUMB2')
    direccion = models.CharField(max_length=35, null=True, db_column='STREET')
    poblacion = models.CharField(max_length=35, null=True, db_column='CITY')
    cadena = models.ForeignKey(Cadena, null=True, db_column='/BIC/ZCADENA', db_index=False)
    subcadena = models.ForeignKey(Subcadena, null=True, db_column='/BIC/ZSBCADENA', db_index=False)
    zonaReparto = models.ForeignKey(ZonaReparto, null=True, db_column='/BIC/ZLZONE', verbose_name='Zona de Reporte',
                                    db_index=False)
    tipoCliente = models.ForeignKey(TipoCliente, null=True, db_column='/BIC/ZTIPCL', verbose_name='Tipo de Cliente',
                                    db_index=False)
    subtipoCliente = models.ForeignKey(SubtipoCliente, null=True, db_column='/BIC/ZSUBTICL',
                                       verbose_name='Subtipo de Cliente', db_index=False)
    oficinaVentas = models.ForeignKey(OficinaVentas, null=True, db_column='SALES_OFF', verbose_name='Oficina de Ventas',
                                      db_index=False)
    zonaVentas = models.ForeignKey(ZonaVentas, null=True, db_column='SALES_DIST', verbose_name='Zona de Ventas',
                                   db_index=False)

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHCLIATT'
        verbose_name = 'Atributo de Cliente'
        verbose_name_plural = 'Atributos de Clientes'


class AtributoMaterial(models.Model):
    material = models.ForeignKey(Material, primary_key=True, null=False, db_column='/BIC/ZMATERIAL')
    sector = models.ForeignKey(Sector, null=True, db_column='/BIC/ZITORIGEN', db_index=False)
    grupoArticulo = models.ForeignKey(GrupoArticulo, null=True, db_column='EXTMATLGRP', verbose_name='Grupo Articulo',
                                      db_index=False)
    nivel1 = models.ForeignKey(Nivel1, null=True, db_column='RPA_WGH1', db_index=False)
    nivel2 = models.ForeignKey(Nivel2, null=True, db_column='RPA_WGH2', db_index=False)
    nivel3 = models.ForeignKey(Nivel3, null=True, db_column='RPA_WGH3', db_index=False)
    nivel4 = models.ForeignKey(Nivel4, null=True, db_column='RPA_WGH4', db_index=False)

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