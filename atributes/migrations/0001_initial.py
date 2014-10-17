# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('text', '__latest__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtributoCliente',
            fields=[
                ('cliente', models.ForeignKey(primary_key=True, db_column=b'/BIC/ZCUSTOMER', serialize=False, to='text.Cliente')),
                ('rut', models.CharField(max_length=11, null=True, db_column=b'TAX_NUMB2')),
                ('direccion', models.CharField(max_length=35, null=True, db_column=b'STREET')),
                ('poblacion', models.CharField(max_length=35, null=True, db_column=b'CITY')),
                ('cadena', models.CharField(max_length=3, null=True, db_column=b'/BIC/ZCADENA')),
                ('subcadena', models.CharField(max_length=3, null=True, db_column=b'/BIC/ZSBCADENA')),
                ('zonaReparto', models.CharField(max_length=10, null=True, verbose_name=b'Zona de Reporte', db_column=b'/BIC/ZLZONE')),
                ('tipoCliente', models.CharField(max_length=2, null=True, verbose_name=b'Tipo de Cliente', db_column=b'/BIC/ZTIPCL')),
                ('subtipoCliente', models.CharField(max_length=2, null=True, verbose_name=b'Subtipo de Cliente', db_column=b'/BIC/ZSUBTICL')),
                ('oficinaVentas', models.CharField(max_length=4, null=True, verbose_name=b'Oficina de Ventas', db_column=b'SALES_OFF')),
                ('zonaVentas', models.CharField(max_length=6, null=True, verbose_name=b'Zona de Ventas', db_column=b'SALES_DIST')),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHCLIATT',
                'verbose_name': b'Atributo de Cliente',
                'verbose_name_plural': b'Atributos de Clientes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AtributoInterlocutor',
            fields=[
                ('interlocutor', models.ForeignKey(primary_key=True, db_column=b'/BIC/ZCUSTOMER', serialize=False, to='text.Cliente')),
                ('rut', models.CharField(max_length=11, null=True, db_column=b'TAX_NUMB2')),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHINTEAT',
                'verbose_name': b'Atributo de Interlocutor',
                'verbose_name_plural': b'Atributos de Interlocutores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AtributoMaterial',
            fields=[
                ('material', models.ForeignKey(primary_key=True, db_column=b'/BIC/ZMATERIAL', serialize=False, to='text.Material')),
                ('sector', models.CharField(max_length=5, null=True, db_column=b'/BIC/ZITORIGEN')),
                ('grupoArticulo', models.CharField(max_length=18, null=True, verbose_name=b'Grupo Articulo', db_column=b'EXTMATLGRP')),
                ('nivel1', models.CharField(max_length=9, null=True, db_column=b'RPA_WGH1')),
                ('nivel2', models.CharField(max_length=9, null=True, db_column=b'RPA_WGH2')),
                ('nivel3', models.CharField(max_length=9, null=True, db_column=b'RPA_WGH3')),
                ('nivel4', models.CharField(max_length=11, null=True, db_column=b'RPA_WGH4')),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHMATATT',
                'verbose_name': b'Atributo de Material',
                'verbose_name_plural': b'Atributos de Materiales',
            },
            bases=(models.Model,),
        ),
    ]
