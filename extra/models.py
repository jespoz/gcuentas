from django.db import models
from texto.models import TipoCliente


class TipoComision(models.Model):
    tipoComision = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/TIPO/COMISION'
        verbose_name = 'Tipo de Comision'
        verbose_name_plural = 'Tipo de Comision'

    def __unicode__(self):
        return self.tipoComision


class SubtipoComision(models.Model):
    subtipoComision = models.CharField(max_length=144, null=False)
    tipoComision = models.ForeignKey(TipoComision, null=False, db_index=False)
    tipoCliente = models.ForeignKey(TipoCliente, null=False, db_index=False)
    query = models.TextField(null=False)

    class Meta:
        db_table = 'GCUENTAS\".\"/BIC/SUBTIPO/COMISION'
        verbose_name = 'Subtipo de Comision'
        verbose_name_plural = 'Subtipo de Comision'

    def __unicode__(self):
        return self.subtipoComision