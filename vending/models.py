from django.db import models
from atributes.models import *


class NivelServicio(models.Model):
    fecha = models.CharField(max_length=8, null=False, db_column='CALDAY')
    cliente = models.CharField(max_length=10, null=False, db_column='/BIC/ZCUSTOMER')
    grupoArticulo = models.CharField(max_length=18, null=False, db_column='EXTMATLGRP', verbose_name='Grupo Articulo')
    pedido = models.FloatField(default=0, db_column='/BIC/ZNTPECAN')
    factura = models.FloatField(default=0, db_column='/BIC/ZNTFACAN')
    demanda = models.FloatField(default=0, db_column='/BIC/ZNTDECAN')
    preventa = models.CharField(max_length=10, null=True, db_column='/BIC/ZCLPRVTA')
    supervisor = models.CharField(max_length=10, null=True, db_column='/BIC/ZCLSUPER')
    medida = models.CharField(max_length=3, null=True, db_column='UNIT')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/OHZOHNVSER'
        verbose_name = 'Nivel de Servicio'
        verbose_name_plural = 'Nivel de Servicio'


class VentaDiaria(models.Model):
    cliente = models.CharField(max_length=10, null=False, db_column='DIMZCUSTOMER')
    fecha = models.CharField(max_length=8, null=False, db_column='DIM0CALDAY')
    material = models.CharField(max_length=18, null=False, db_column='DIMZMATERIAL')
    fuente = models.CharField(max_length=3, null=False, db_column='DIMZFNTEORG')
    unidad = models.FloatField(default=0, db_column='KYF4ZABR2I1ILUF')
    kilo = models.FloatField(default=0, db_column='KYF4ZABR2XEKJ1U')
    neto = models.FloatField(default=0, db_column='KYF4Z6SI9QLJ980')
    preventa = models.CharField(max_length=10, null=True, db_column='/BIC/ZCLPRVTA')
    supervisor = models.CharField(max_length=10, null=True, db_column='/BIC/ZCLSUPER')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/0CZVDLTSBW'
        verbose_name = 'Venta Diaria'
        verbose_name_plural = 'Venta Diaria'


class VentaAcumulada(models.Model):
    cliente = models.CharField(max_length=10, null=False, db_column='DIMZCUSTOMER')
    fecha = models.CharField(max_length=8, null=False, db_column='DIM0CALDAY')
    material = models.CharField(max_length=18, null=False, db_column='DIMZMATERIAL')
    fuente = models.CharField(max_length=3, null=False, db_column='DIMZFNTEORG')
    unidad = models.FloatField(default=0, db_column='KYF4ZABR2I1ILUF')
    kilo = models.FloatField(default=0, db_column='KYF4ZABR2XEKJ1U')
    neto = models.FloatField(default=0, db_column='KYF4Z6SI9QLJ980')
    preventa = models.CharField(max_length=10, null=True, db_column='/BIC/ZCLPRVTA')
    supervisor = models.CharField(max_length=10, null=True, db_column='/BIC/ZCLSUPER')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/0CZVDLTSBW/ACUM'
        verbose_name = 'Venta Acumulada'
        verbose_name_plural = 'Venta Acumulada'


class ClienteNoAtendido(models.Model):
    cliente = models.CharField(max_length=10, null=False, db_column='DIMZCUSTOMER')
    mes = models.IntegerField(null=False, db_column='DIM0CALMONTH')
    material = models.CharField(max_length=18, null=False, db_column='DIMZMATERIAL')
    localesMes = models.FloatField(default=0, db_column='KYF44LHLWIKYTSO')
    localesTresMes = models.FloatField(default=0, db_column='KYF44LHLWIKYTS01')
    localesNoAtendidos = models.FloatField(default=0, db_column='KYF4ZFQCJ8RYJ1L')

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/0CZCNA_COM'
        verbose_name = 'Cliente No Atendido'
        verbose_name_plural = 'Clientes No Atendidos'