from django.db import models


class Cadena(models.Model):
    codigo = models.CharField(max_length=3, unique=True, db_column='/BIC/ZCADENA', )
    cadena = models.CharField(max_length=40, null=True, db_column='TXTMD')

    class Meta:
        db_table = '/BIC/OHZOHCADTXT'

    def __unicode__(self):
        return self.cadena


class Cliente(models.Model):
    codigo = models.CharField(max_length=10, unique=True, null=False, db_column='/BIC/ZCUSTOMER', )
    cliente = models.CharField(max_length=40, null=True, db_column='TXTMD')

    class Meta:
        db_table = '/BIC/OHZOHCLITXT'

    def __unicode__(self):
        return self.cliente


class GrupoArticulo(models.Model):
    codigo = models.CharField(max_length=18, unique=True, null=False, db_column='EXTMATLGRP', )
    grupoArticulo = models.CharField(max_length=40, null=True, db_column='TXTMD', verbose_name='Grupo Articulo')

    class Meta:
        db_table = '/BIC/OHZOHGEXTTX'
        verbose_name = 'Grupo Articulo Externo'
        verbose_name_plural = 'Grupo Articulo Externo'

    def __unicode__(self):
        return self.grupoArticulo


class Marca(models.Model):
    codigo = models.CharField(max_length=3, unique=True, null=False, db_column='/BIC/ZITMARCA', )
    marca = models.CharField(max_length=20, null=True, db_column='TXTSH')

    class Meta:
        db_table = '/BIC/OHZOHMARCTX'

    def __unicode__(self):
        return self.marca


class Material(models.Model):
    codigo = models.CharField(max_length=18, unique=True, null=False, db_column='/BIC/ZMATERIAL', )
    material = models.CharField(max_length=40, null=True, db_column='TXTMD')

    class Meta:
        db_table = '/BIC/OHZOHMATTXT'
        verbose_name_plural = 'Materiales'

    def __unicode__(self):
        return self.material


class Nivel1(models.Model):
    codigo = models.CharField(max_length=9, unique=True, null=False, db_column='RPA_WGH1', )
    nivel1 = models.CharField(max_length=40, null=True, db_column='TXTMD', verbose_name='Nivel 1')

    class Meta:
        db_table = '/BIC/OHZOHNIV1TX'
        verbose_name = 'Nivel 1'
        verbose_name_plural = 'Nivel 1'

    def __unicode__(self):
        return self.nivel1


class Nivel2(models.Model):
    codigo = models.CharField(max_length=9, unique=True, null=False, db_column='RPA_WGH2', )
    nivel2 = models.CharField(max_length=40, null=True, db_column='TXTMD', verbose_name='Nivel 2')

    class Meta:
        db_table = '/BIC/OHZOHNIV2TX'
        verbose_name = 'Nivel 2'
        verbose_name_plural = 'Nivel 2'

    def __unicode__(self):
        return self.nivel2


class Nivel3(models.Model):
    codigo = models.CharField(max_length=9, unique=True, null=False, db_column='RPA_WGH3', )
    nivel3 = models.CharField(max_length=40, null=True, db_column='TXTMD', verbose_name='Nivel 3')

    class Meta:
        db_table = '/BIC/OHZOHNIV3TX'
        verbose_name = 'Nivel 3'
        verbose_name_plural = 'Nivel 3'

    def __unicode__(self):
        return self.nivel3


class Nivel4(models.Model):
    codigo = models.CharField(max_length=9, unique=True, null=False, db_column='RPA_WGH4', )
    nivel4 = models.CharField(max_length=40, null=True, db_column='TXTMD', verbose_name='Nivel 4')

    class Meta:
        db_table = '/BIC/OHZOHNIV4TX'
        verbose_name = 'Nivel 4'
        verbose_name_plural = 'Nivel 4'

    def __unicode__(self):
        return self.nivel4


class Sector(models.Model):
    codigo = models.CharField(max_length=5, unique=True, null=False, db_column='/BIC/ZITORIGEN', )
    sector = models.CharField(max_length=40, null=True, db_column='TXTMD')

    class Meta:
        db_table = '/BIC/OHZOHSECTXT'
        verbose_name_plural = 'Sectores'

    def __unicode__(self):
        return self.sector


class Subcadena(models.Model):
    codigo = models.CharField(max_length=3, unique=True, null=False, db_column='/BIC/ZSBCADENA', )
    subcadena = models.CharField(max_length=40, null=True, db_column='TXTMD')

    class Meta:
        db_table = '/BIC/OHZOHSCADTX'

    def __unicode__(self):
        return self.subcadena


class SubtipoCliente(models.Model):
    codigo = models.CharField(max_length=2, unique=True, null=False, db_column='/BIC/ZSUBTICL', )
    subtipoCliente = models.CharField(max_length=40, null=True, db_column='TXTMD', verbose_name='Subtipo Cliente')

    class Meta:
        db_table = '/BIC/OHZOHSTCLIT'
        verbose_name = 'Subtipo Cliente'
        verbose_name_plural = 'Subtipo Cliente'

    def __unicode__(self):
        return self.subtipoCliente


class TipoCliente(models.Model):
    codigo = models.CharField(max_length=2, unique=True, null=False, db_column='/BIC/ZTIPCL', )
    tipoCliente = models.CharField(max_length=40, null=True, db_column='TXTMD', verbose_name='Tipo Cliente')

    class Meta:
        db_table = '/BIC/OHZOHTCLITX'
        verbose_name = 'Tipo Cliente'
        verbose_name_plural = 'Tipo Cliente'

    def __unicode__(self):
        return self.tipoCliente


class ZonaReparto(models.Model):
    codigo = models.CharField(max_length=10, unique=True, null=False, db_column='/BIC/ZLZONE', )
    zonaReparto = models.CharField(max_length=40, null=True, db_column='TXTMD', verbose_name='Zona de Reparto')

    class Meta:
        db_table = '/BIC/OHZOHZONRTX'
        verbose_name = 'Zona de Reparto'
        verbose_name_plural = 'Zona de Reparto'

    def __unicode__(self):
        return self.zonaReparto


class ZonaVentas(models.Model):
    codigo = models.CharField(max_length=6, unique=True, null=False, db_column='SALES_DIST')
    zonaVentas = models.CharField(max_length=20, null=True, db_column='TXTSH', verbose_name='Zona de Ventas')

    class Meta:
        db_table = '/BIC/OHZOHZONVTX'
        verbose_name = 'Zona de Ventas'
        verbose_name_plural = 'Zona de Ventas'

    def __unicode__(self):
        return self.zonaVentas


class OficinaVentas(models.Model):
    codigo = models.CharField(max_length=4, unique=True, null=False, db_column='SALES_OFF')
    oficinaVentas = models.CharField(max_length=40, null=True, db_column='TXTMD', verbose_name='Oficina de Ventas')

    class Meta:
        db_table = '/BIC/OHZOHIFVTXT'
        verbose_name = 'Oficina de Ventas'
        verbose_name_plural = 'Oficina de Ventas'

    def __unicode__(self):
        return self.oficinaVentas


class AtributoCliente(models.Model):
    cliente = models.ForeignKey(Cliente, unique=True, null=False, db_column='/BIC/ZCUSTOMER')
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
        db_table = '/BIC/OHZOHCLIATT'
        verbose_name = 'Atributo de Cliente'
        verbose_name_plural = 'Atributos de Clientes'


class AtributoMaterial(models.Model):
    material = models.ForeignKey(Material, unique=True, null=False, db_column='/BIC/ZMATERIAL')
    sector = models.ForeignKey(Sector, null=True, db_column='/BIC/ZITORIGEN', db_index=False)
    grupoArticulo = models.ForeignKey(GrupoArticulo, null=True, db_column='EXTMATLGRP', verbose_name='Grupo Articulo',
                                      db_index=False)
    nivel1 = models.ForeignKey(Nivel1, null=True, db_column='RPA_WGH1', db_index=False)
    nivel2 = models.ForeignKey(Nivel2, null=True, db_column='RPA_WGH2', db_index=False)
    nivel3 = models.ForeignKey(Nivel3, null=True, db_column='RPA_WGH3', db_index=False)
    nivel4 = models.ForeignKey(Nivel4, null=True, db_column='RPA_WGH4', db_index=False)

    class Meta:
        db_table = '/BIC/OHZOHMATATT'
        verbose_name = 'Atributo de Material'
        verbose_name_plural = 'Atributos de Materiales'

    def __unicode__(self):
        return self.material.codigo


class NivelServicio(models.Model):
    fecha = models.DateField(null=False, db_column='CALDAY')
    cliente = models.ForeignKey(Cliente, null=False, db_column='/BIC/ZCUSTOMER', db_index=False)
    grupoArticulo = models.ForeignKey(GrupoArticulo, null=False, db_column='EXTMATLGRP', verbose_name='Grupo Articulo',
                                      db_index=False)
    pedido = models.FloatField(default=0, db_column='/BIC/ZNTPECAN')
    factura = models.FloatField(default=0, db_column='/BIC/ZNTFACAN')
    demanda = models.FloatField(default=0, db_column='/BIC/ZNTDECAN')

    class Meta:
        db_table = '/BIC/OHZOHNVSER'
        verbose_name = 'Nivel de Servicio'
        verbose_name_plural = 'Nivel de Servicio'


class VentaDiaria(models.Model):
    cliente = models.ForeignKey(Cliente, null=False, db_column='DIMZCUSTOMER', db_index=False)
    fecha = models.DateField(null=False, db_column='DIM0CALDAY')
    material = models.ForeignKey(Material, null=False, db_column='DIMZMATERIAL', db_index=False)
    fuente = models.CharField(max_length=3, null=False, db_column='DIMZFNTEORG')
    unidad = models.FloatField(default=0, db_column='KYF4ZABR2I1ILUF')
    kilo = models.FloatField(default=0, db_column='KYF4ZABR2XEKJ1U')
    neto = models.FloatField(default=0, db_column='KYF4Z6SI9QLJ980')

    class Meta:
        db_table = '/BIC/0CZVDLTSBW'
        verbose_name = 'Venta Diaria'
        verbose_name_plural = 'Venta Diaria'
