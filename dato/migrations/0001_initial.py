# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atributo', '0001_initial'),
        ('texto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteNoAtendido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes', models.IntegerField(db_column=b'DIM0CALMONTH')),
                ('localesMes', models.FloatField(default=0, db_column=b'KYF44LHLWIKYTSO')),
                ('localesTresMes', models.FloatField(default=0, db_column=b'KYF44LHLWIKYTS01')),
                ('localesNoAtendidos', models.FloatField(default=0, db_column=b'KYF4ZFQCJ8RYJ1L')),
                ('cliente', models.ForeignKey(to='atributo.AtributoCliente', db_column=b'DIMZCUSTOMER', db_index=False)),
                ('material', models.ForeignKey(to='atributo.AtributoMaterial', db_column=b'DIMZMATERIAL', db_index=False)),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/0CZCNA_COM',
                'verbose_name': b'Cliente No Atendido',
                'verbose_name_plural': b'Clientes No Atendidos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NivelServicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(db_column=b'CALDAY')),
                ('pedido', models.FloatField(default=0, db_column=b'/BIC/ZNTPECAN')),
                ('factura', models.FloatField(default=0, db_column=b'/BIC/ZNTFACAN')),
                ('demanda', models.FloatField(default=0, db_column=b'/BIC/ZNTDECAN')),
                ('medida', models.CharField(max_length=3, null=True, db_column=b'UNIT')),
                ('cliente', models.ForeignKey(to='atributo.AtributoCliente', db_column=b'/BIC/ZCUSTOMER', db_index=False)),
                ('grupoArticulo', models.ForeignKey(verbose_name=b'Grupo Articulo', to='texto.GrupoArticulo', db_column=b'EXTMATLGRP', db_index=False)),
                ('preventa', models.ForeignKey(to='atributo.AtributoInterlocutor', null=True, db_column=b'/BIC/ZCLPRVTA', db_index=False)),
                ('supervisor', models.ForeignKey(to='atributo.AtributoInterlocutor', null=True, db_column=b'/BIC/ZCLSUPER', db_index=False)),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHNVSER',
                'verbose_name': b'Nivel de Servicio',
                'verbose_name_plural': b'Nivel de Servicio',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VentaAcumulada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(db_column=b'DIM0CALDAY')),
                ('fuente', models.CharField(max_length=3, db_column=b'DIMZFNTEORG')),
                ('unidad', models.FloatField(default=0, db_column=b'KYF4ZABR2I1ILUF')),
                ('kilo', models.FloatField(default=0, db_column=b'KYF4ZABR2XEKJ1U')),
                ('neto', models.FloatField(default=0, db_column=b'KYF4Z6SI9QLJ980')),
                ('cliente', models.ForeignKey(to='atributo.AtributoCliente', db_column=b'DIMZCUSTOMER', db_index=False)),
                ('material', models.ForeignKey(to='atributo.AtributoMaterial', db_column=b'DIMZMATERIAL', db_index=False)),
                ('preventa', models.ForeignKey(to='atributo.AtributoInterlocutor', null=True, db_column=b'/BIC/ZCLPRVTA', db_index=False)),
                ('supervisor', models.ForeignKey(to='atributo.AtributoInterlocutor', null=True, db_column=b'/BIC/ZCLSUPER', db_index=False)),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/0CZVDLTSBW/ACUM',
                'verbose_name': b'Venta Acumulada',
                'verbose_name_plural': b'Venta Acumulada',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VentaDiaria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(db_column=b'DIM0CALDAY')),
                ('fuente', models.CharField(max_length=3, db_column=b'DIMZFNTEORG')),
                ('unidad', models.FloatField(default=0, db_column=b'KYF4ZABR2I1ILUF')),
                ('kilo', models.FloatField(default=0, db_column=b'KYF4ZABR2XEKJ1U')),
                ('neto', models.FloatField(default=0, db_column=b'KYF4Z6SI9QLJ980')),
                ('cliente', models.ForeignKey(to='atributo.AtributoCliente', db_column=b'DIMZCUSTOMER', db_index=False)),
                ('material', models.ForeignKey(to='atributo.AtributoMaterial', db_column=b'DIMZMATERIAL', db_index=False)),
                ('preventa', models.ForeignKey(to='atributo.AtributoInterlocutor', null=True, db_column=b'/BIC/ZCLPRVTA', db_index=False)),
                ('supervisor', models.ForeignKey(to='atributo.AtributoInterlocutor', null=True, db_column=b'/BIC/ZCLSUPER', db_index=False)),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/0CZVDLTSBW',
                'verbose_name': b'Venta Diaria',
                'verbose_name_plural': b'Venta Diaria',
            },
            bases=(models.Model,),
        ),
    ]
