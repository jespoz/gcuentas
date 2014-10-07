# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('migration', '0002_auto_20141007_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtributoMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grupoArticulo', models.ForeignKey(db_column=b'EXTMATLGRP', verbose_name=b'Grupo Articulo',
                                                    to='migration.GrupoArticulo', null=True, db_index=False)),
                ('material', models.ForeignKey(db_column=b'/BIC/ZMATERIAL', to='migration.Material', unique=True)),
                ('nivel1', models.ForeignKey(to='migration.Nivel1', null=True, db_column=b'RPA_WGH1', db_index=False)),
                ('nivel2', models.ForeignKey(to='migration.Nivel2', null=True, db_column=b'RPA_WGH2', db_index=False)),
                ('nivel3', models.ForeignKey(to='migration.Nivel3', null=True, db_column=b'RPA_WGH3', db_index=False)),
                ('nivel4', models.ForeignKey(to='migration.Nivel4', null=True, db_column=b'RPA_WGH4', db_index=False)),
                ('sector',
                 models.ForeignKey(to='migration.Sector', null=True, db_column=b'/BIC/ZITORIGEN', db_index=False)),
            ],
            options={
                'db_table': b'/BIC/OHZOHMATATT',
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
                ('cliente', models.ForeignKey(to='migration.Cliente', db_column=b'/BIC/ZCUSTOMER', db_index=False)),
                ('grupoArticulo', models.ForeignKey(verbose_name=b'Grupo Articulo', to='migration.GrupoArticulo',
                                                    db_column=b'EXTMATLGRP', db_index=False)),
            ],
            options={
                'db_table': b'/BIC/OHZOHNVSER',
                'verbose_name': b'Nivel de Servicio',
                'verbose_name_plural': b'Nivel de Servicio',
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
                ('cliente', models.ForeignKey(to='migration.Cliente', db_column=b'DIMZCUSTOMER', db_index=False)),
                ('material', models.ForeignKey(to='migration.Material', db_column=b'DIMZMATERIAL', db_index=False)),
            ],
            options={
                'db_table': b'/BIC/0CZVDLTSBW',
                'verbose_name': b'Venta Diaria',
                'verbose_name_plural': b'Venta Diaria',
            },
            bases=(models.Model,),
        ),
    ]
