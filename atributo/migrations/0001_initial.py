# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('texto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtributoCliente',
            fields=[
                ('cliente', models.ForeignKey(primary_key=True, db_column=b'/BIC/ZCUSTOMER', serialize=False, to='texto.Cliente')),
                ('rut', models.CharField(max_length=11, null=True, db_column=b'TAX_NUMB2')),
                ('direccion', models.CharField(max_length=35, null=True, db_column=b'STREET')),
                ('poblacion', models.CharField(max_length=35, null=True, db_column=b'CITY')),
                ('cadena', models.ForeignKey(to='texto.Cadena', null=True, db_column=b'/BIC/ZCADENA', db_index=False)),
                ('oficinaVentas', models.ForeignKey(db_column=b'SALES_OFF', verbose_name=b'Oficina de Ventas', to='texto.OficinaVentas', null=True, db_index=False)),
                ('subcadena', models.ForeignKey(to='texto.Subcadena', null=True, db_column=b'/BIC/ZSBCADENA', db_index=False)),
                ('subtipoCliente', models.ForeignKey(db_column=b'/BIC/ZSUBTICL', verbose_name=b'Subtipo de Cliente', to='texto.SubtipoCliente', null=True, db_index=False)),
                ('tipoCliente', models.ForeignKey(db_column=b'/BIC/ZTIPCL', verbose_name=b'Tipo de Cliente', to='texto.TipoCliente', null=True, db_index=False)),
                ('zonaReparto', models.ForeignKey(db_column=b'/BIC/ZLZONE', verbose_name=b'Zona de Reporte', to='texto.ZonaReparto', null=True, db_index=False)),
                ('zonaVentas', models.ForeignKey(db_column=b'SALES_DIST', verbose_name=b'Zona de Ventas', to='texto.ZonaVentas', null=True, db_index=False)),
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
                ('interlocutor', models.ForeignKey(primary_key=True, db_column=b'/BIC/ZCUSTOMER', serialize=False, to='texto.Cliente')),
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
                ('material', models.ForeignKey(primary_key=True, db_column=b'/BIC/ZMATERIAL', serialize=False, to='texto.Material')),
                ('grupoArticulo', models.ForeignKey(db_column=b'EXTMATLGRP', verbose_name=b'Grupo Articulo', to='texto.GrupoArticulo', null=True, db_index=False)),
                ('nivel1', models.ForeignKey(to='texto.Nivel1', null=True, db_column=b'RPA_WGH1', db_index=False)),
                ('nivel2', models.ForeignKey(to='texto.Nivel2', null=True, db_column=b'RPA_WGH2', db_index=False)),
                ('nivel3', models.ForeignKey(to='texto.Nivel3', null=True, db_column=b'RPA_WGH3', db_index=False)),
                ('nivel4', models.ForeignKey(to='texto.Nivel4', null=True, db_column=b'RPA_WGH4', db_index=False)),
                ('sector', models.ForeignKey(to='texto.Sector', null=True, db_column=b'/BIC/ZITORIGEN', db_index=False)),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHMATATT',
                'verbose_name': b'Atributo de Material',
                'verbose_name_plural': b'Atributos de Materiales',
            },
            bases=(models.Model,),
        ),
    ]
