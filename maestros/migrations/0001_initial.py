# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadena',
            fields=[
                ('codigo', models.CharField(max_length=3, unique=True, serialize=False, primary_key=True, db_column=b'/BIC/ZCADENA')),
                ('cadena', models.CharField(max_length=40, null=True, db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHCADTXT',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codigo', models.CharField(max_length=10, unique=True, serialize=False, primary_key=True, db_column=b'/BIC/ZCUSTOMER')),
                ('cliente', models.CharField(max_length=40, null=True, db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHCLITXT',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AtributoInterlocutor',
            fields=[
                ('interlocutor', models.ForeignKey(primary_key=True, db_column=b'/BIC/ZCUSTOMER', serialize=False, to='maestros.Cliente')),
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
            name='AtributoCliente',
            fields=[
                ('cliente', models.ForeignKey(primary_key=True, db_column=b'/BIC/ZCUSTOMER', serialize=False, to='maestros.Cliente')),
                ('rut', models.CharField(max_length=11, null=True, db_column=b'TAX_NUMB2')),
                ('direccion', models.CharField(max_length=35, null=True, db_column=b'STREET')),
                ('poblacion', models.CharField(max_length=35, null=True, db_column=b'CITY')),
                ('cadena', models.ForeignKey(to='maestros.Cadena', null=True, db_column=b'/BIC/ZCADENA', db_index=False)),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHCLIATT',
                'verbose_name': b'Atributo de Cliente',
                'verbose_name_plural': b'Atributos de Clientes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GrupoArticulo',
            fields=[
                ('codigo', models.CharField(max_length=18, unique=True, serialize=False, primary_key=True, db_column=b'EXTMATLGRP')),
                ('grupoArticulo', models.CharField(max_length=40, null=True, verbose_name=b'Grupo Articulo', db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHGEXTTX',
                'verbose_name': b'Grupo Articulo Externo',
                'verbose_name_plural': b'Grupo Articulo Externo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('codigo', models.CharField(max_length=3, unique=True, serialize=False, primary_key=True, db_column=b'/BIC/ZITMARCA')),
                ('marca', models.CharField(max_length=20, null=True, db_column=b'TXTSH')),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHMARCTX',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('codigo', models.CharField(max_length=18, unique=True, serialize=False, primary_key=True, db_column=b'/BIC/ZMATERIAL')),
                ('material', models.CharField(max_length=40, null=True, db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHMATTXT',
                'verbose_name_plural': b'Materiales',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AtributoMaterial',
            fields=[
                ('material', models.ForeignKey(primary_key=True, db_column=b'/BIC/ZMATERIAL', serialize=False, to='maestros.Material')),
                ('grupoArticulo', models.ForeignKey(db_column=b'EXTMATLGRP', verbose_name=b'Grupo Articulo', to='maestros.GrupoArticulo', null=True, db_index=False)),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHMATATT',
                'verbose_name': b'Atributo de Material',
                'verbose_name_plural': b'Atributos de Materiales',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nivel1',
            fields=[
                ('codigo', models.CharField(max_length=9, unique=True, serialize=False, primary_key=True, db_column=b'RPA_WGH1')),
                ('nivel1', models.CharField(max_length=40, null=True, verbose_name=b'Nivel 1', db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHNIV1TX',
                'verbose_name': b'Nivel 1',
                'verbose_name_plural': b'Nivel 1',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='atributomaterial',
            name='nivel1',
            field=models.ForeignKey(to='maestros.Nivel1', null=True, db_column=b'RPA_WGH1', db_index=False),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Nivel2',
            fields=[
                ('codigo', models.CharField(max_length=9, unique=True, serialize=False, primary_key=True, db_column=b'RPA_WGH2')),
                ('nivel2', models.CharField(max_length=40, null=True, verbose_name=b'Nivel 2', db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHNIV2TX',
                'verbose_name': b'Nivel 2',
                'verbose_name_plural': b'Nivel 2',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='atributomaterial',
            name='nivel2',
            field=models.ForeignKey(to='maestros.Nivel2', null=True, db_column=b'RPA_WGH2', db_index=False),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Nivel3',
            fields=[
                ('codigo', models.CharField(max_length=9, unique=True, serialize=False, primary_key=True, db_column=b'RPA_WGH3')),
                ('nivel3', models.CharField(max_length=40, null=True, verbose_name=b'Nivel 3', db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHNIV3TX',
                'verbose_name': b'Nivel 3',
                'verbose_name_plural': b'Nivel 3',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='atributomaterial',
            name='nivel3',
            field=models.ForeignKey(to='maestros.Nivel3', null=True, db_column=b'RPA_WGH3', db_index=False),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Nivel4',
            fields=[
                ('codigo', models.CharField(max_length=11, unique=True, serialize=False, primary_key=True, db_column=b'RPA_WGH4')),
                ('nivel4', models.CharField(max_length=40, null=True, verbose_name=b'Nivel 4', db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHNIV4TX',
                'verbose_name': b'Nivel 4',
                'verbose_name_plural': b'Nivel 4',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='atributomaterial',
            name='nivel4',
            field=models.ForeignKey(to='maestros.Nivel4', null=True, db_column=b'RPA_WGH4', db_index=False),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='OficinaVentas',
            fields=[
                ('codigo', models.CharField(max_length=4, unique=True, serialize=False, primary_key=True, db_column=b'SALES_OFF')),
                ('oficinaVentas', models.CharField(max_length=40, null=True, verbose_name=b'Oficina de Ventas', db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHIFVTXT',
                'verbose_name': b'Oficina de Ventas',
                'verbose_name_plural': b'Oficina de Ventas',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='atributocliente',
            name='oficinaVentas',
            field=models.ForeignKey(db_column=b'SALES_OFF', verbose_name=b'Oficina de Ventas', to='maestros.OficinaVentas', null=True, db_index=False),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('codigo', models.CharField(max_length=5, unique=True, serialize=False, primary_key=True, db_column=b'/BIC/ZITORIGEN')),
                ('sector', models.CharField(max_length=40, null=True, db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHSECTXT',
                'verbose_name_plural': b'Sectores',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='atributomaterial',
            name='sector',
            field=models.ForeignKey(to='maestros.Sector', null=True, db_column=b'/BIC/ZITORIGEN', db_index=False),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Subcadena',
            fields=[
                ('codigo', models.CharField(max_length=3, unique=True, serialize=False, primary_key=True, db_column=b'/BIC/ZSBCADENA')),
                ('subcadena', models.CharField(max_length=40, null=True, db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHSCADTX',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='atributocliente',
            name='subcadena',
            field=models.ForeignKey(to='maestros.Subcadena', null=True, db_column=b'/BIC/ZSBCADENA', db_index=False),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='SubtipoCliente',
            fields=[
                ('codigo', models.CharField(max_length=2, unique=True, serialize=False, primary_key=True, db_column=b'/BIC/ZSUBTICL')),
                ('subtipoCliente', models.CharField(max_length=40, null=True, verbose_name=b'Subtipo Cliente', db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHSTCLIT',
                'verbose_name': b'Subtipo Cliente',
                'verbose_name_plural': b'Subtipo Cliente',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='atributocliente',
            name='subtipoCliente',
            field=models.ForeignKey(db_column=b'/BIC/ZSUBTICL', verbose_name=b'Subtipo de Cliente', to='maestros.SubtipoCliente', null=True, db_index=False),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('codigo', models.CharField(max_length=2, unique=True, serialize=False, primary_key=True, db_column=b'/BIC/ZTIPCL')),
                ('tipoCliente', models.CharField(max_length=40, null=True, verbose_name=b'Tipo Cliente', db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHTCLITX',
                'verbose_name': b'Tipo Cliente',
                'verbose_name_plural': b'Tipo Cliente',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='atributocliente',
            name='tipoCliente',
            field=models.ForeignKey(db_column=b'/BIC/ZTIPCL', verbose_name=b'Tipo de Cliente', to='maestros.TipoCliente', null=True, db_index=False),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='ZonaReparto',
            fields=[
                ('codigo', models.CharField(max_length=10, unique=True, serialize=False, primary_key=True, db_column=b'/BIC/ZLZONE')),
                ('zonaReparto', models.CharField(max_length=40, null=True, verbose_name=b'Zona de Reparto', db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHZONRTX',
                'verbose_name': b'Zona de Reparto',
                'verbose_name_plural': b'Zona de Reparto',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='atributocliente',
            name='zonaReparto',
            field=models.ForeignKey(db_column=b'/BIC/ZLZONE', verbose_name=b'Zona de Reporte', to='maestros.ZonaReparto', null=True, db_index=False),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='ZonaVentas',
            fields=[
                ('codigo', models.CharField(max_length=6, unique=True, serialize=False, primary_key=True, db_column=b'SALES_DIST')),
                ('zonaVentas', models.CharField(max_length=20, null=True, verbose_name=b'Zona de Ventas', db_column=b'TXTSH')),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/OHZOHZONVTX',
                'verbose_name': b'Zona de Ventas',
                'verbose_name_plural': b'Zona de Ventas',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='atributocliente',
            name='zonaVentas',
            field=models.ForeignKey(db_column=b'SALES_DIST', verbose_name=b'Zona de Ventas', to='maestros.ZonaVentas', null=True, db_index=False),
            preserve_default=True,
        ),
    ]
