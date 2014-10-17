# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteNoAtendido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cliente', models.CharField(max_length=10, db_column=b'DIMZCUSTOMER')),
                ('mes', models.IntegerField(db_column=b'DIM0CALMONTH')),
                ('material', models.CharField(max_length=18, db_column=b'DIMZMATERIAL')),
                ('localesMes', models.FloatField(default=0, db_column=b'KYF44LHLWIKYTSO')),
                ('localesTresMes', models.FloatField(default=0, db_column=b'KYF44LHLWIKYTS01')),
                ('localesNoAtendidos', models.FloatField(default=0, db_column=b'KYF4ZFQCJ8RYJ1L')),
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
                ('fecha', models.CharField(max_length=8, db_column=b'CALDAY')),
                ('cliente', models.CharField(max_length=10, db_column=b'/BIC/ZCUSTOMER')),
                ('grupoArticulo', models.CharField(max_length=18, verbose_name=b'Grupo Articulo', db_column=b'EXTMATLGRP')),
                ('pedido', models.FloatField(default=0, db_column=b'/BIC/ZNTPECAN')),
                ('factura', models.FloatField(default=0, db_column=b'/BIC/ZNTFACAN')),
                ('demanda', models.FloatField(default=0, db_column=b'/BIC/ZNTDECAN')),
                ('preventa', models.CharField(max_length=10, null=True, db_column=b'/BIC/ZCLPRVTA')),
                ('supervisor', models.CharField(max_length=10, null=True, db_column=b'/BIC/ZCLSUPER')),
                ('medida', models.CharField(max_length=3, null=True, db_column=b'UNIT')),
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
                ('cliente', models.CharField(max_length=10, db_column=b'DIMZCUSTOMER')),
                ('fecha', models.CharField(max_length=8, db_column=b'DIM0CALDAY')),
                ('material', models.CharField(max_length=18, db_column=b'DIMZMATERIAL')),
                ('fuente', models.CharField(max_length=3, db_column=b'DIMZFNTEORG')),
                ('unidad', models.FloatField(default=0, db_column=b'KYF4ZABR2I1ILUF')),
                ('kilo', models.FloatField(default=0, db_column=b'KYF4ZABR2XEKJ1U')),
                ('neto', models.FloatField(default=0, db_column=b'KYF4Z6SI9QLJ980')),
                ('preventa', models.CharField(max_length=10, null=True, db_column=b'/BIC/ZCLPRVTA')),
                ('supervisor', models.CharField(max_length=10, null=True, db_column=b'/BIC/ZCLSUPER')),
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
                ('cliente', models.CharField(max_length=10, db_column=b'DIMZCUSTOMER')),
                ('fecha', models.CharField(max_length=8, db_column=b'DIM0CALDAY')),
                ('material', models.CharField(max_length=18, db_column=b'DIMZMATERIAL')),
                ('fuente', models.CharField(max_length=3, db_column=b'DIMZFNTEORG')),
                ('unidad', models.FloatField(default=0, db_column=b'KYF4ZABR2I1ILUF')),
                ('kilo', models.FloatField(default=0, db_column=b'KYF4ZABR2XEKJ1U')),
                ('neto', models.FloatField(default=0, db_column=b'KYF4Z6SI9QLJ980')),
                ('preventa', models.CharField(max_length=10, null=True, db_column=b'/BIC/ZCLPRVTA')),
                ('supervisor', models.CharField(max_length=10, null=True, db_column=b'/BIC/ZCLSUPER')),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/0CZVDLTSBW',
                'verbose_name': b'Venta Diaria',
                'verbose_name_plural': b'Venta Diaria',
            },
            bases=(models.Model,),
        ),
    ]
