# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtributoCliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rut', models.CharField(max_length=11, null=True, db_column=b'TAX_NUMB2')),
                ('direccion', models.CharField(max_length=35, null=True, db_column=b'STREET')),
                ('poblacion', models.CharField(max_length=35, null=True, db_column=b'CITY')),
            ],
            options={
                'db_table': b'/BIC/OHZOHCLIATT',
                'verbose_name': b'Atributo de Cliente',
                'verbose_name_plural': b'Atributos de Clientes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AtributoMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': b'/BIC/OHZOHMATATT',
                'verbose_name': b'Atributo de Material',
                'verbose_name_plural': b'Atributos de Materiales',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cadena',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=3, db_column=b'/BIC/ZCADENA')),
                ('cadena', models.CharField(max_length=40, null=True, db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'/BIC/OHZOHCADTXT',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='atributocliente',
            name='cadena',
            field=models.ForeignKey(to='maestros.Cadena', null=True, db_column=b'/BIC/ZCADENA', db_index=False),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=10, db_column=b'/BIC/ZCUSTOMER')),
                ('cliente', models.CharField(max_length=40, null=True, db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'/BIC/OHZOHCLITXT',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='atributocliente',
            name='cliente',
            field=models.ForeignKey(db_column=b'/BIC/ZCUSTOMER', to='maestros.Cliente', unique=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='GrupoArticulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=18, db_column=b'EXTMATLGRP')),
                ('grupoArticulo', models.CharField(max_length=40, null=True, verbose_name=b'Grupo Articulo', db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'/BIC/OHZOHGEXTTX',
                'verbose_name': b'Grupo Articulo Externo',
                'verbose_name_plural': b'Grupo Articulo Externo',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='atributomaterial',
            name='grupoArticulo',
            field=models.ForeignKey(db_column=b'EXTMATLGRP', verbose_name=b'Grupo Articulo', to='maestros.GrupoArticulo', null=True, db_index=False),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=3, db_column=b'/BIC/ZITMARCA')),
                ('marca', models.CharField(max_length=20, null=True, db_column=b'TXTSH')),
            ],
            options={
                'db_table': b'/BIC/OHZOHMARCTX',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=18, db_column=b'/BIC/ZMATERIAL')),
                ('material', models.CharField(max_length=40, null=True, db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'/BIC/OHZOHMATTXT',
                'verbose_name_plural': b'Materiales',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='atributomaterial',
            name='material',
            field=models.ForeignKey(db_column=b'/BIC/ZMATERIAL', to='maestros.Material', unique=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Nivel1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=9, db_column=b'RPA_WGH1')),
                ('nivel1', models.CharField(max_length=40, null=True, verbose_name=b'Nivel 1', db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'/BIC/OHZOHNIV1TX',
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=9, db_column=b'RPA_WGH2')),
                ('nivel2', models.CharField(max_length=40, null=True, verbose_name=b'Nivel 2', db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'/BIC/OHZOHNIV2TX',
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=9, db_column=b'RPA_WGH3')),
                ('nivel3', models.CharField(max_length=40, null=True, verbose_name=b'Nivel 3', db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'/BIC/OHZOHNIV3TX',
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=9, db_column=b'RPA_WGH4')),
                ('nivel4', models.CharField(max_length=40, null=True, verbose_name=b'Nivel 4', db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'/BIC/OHZOHNIV4TX',
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=4, db_column=b'SALES_OFF')),
                ('oficinaVentas', models.CharField(max_length=40, null=True, verbose_name=b'Oficina de Ventas', db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'/BIC/OHZOHIFVTXT',
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=5, db_column=b'/BIC/ZITORIGEN')),
                ('sector', models.CharField(max_length=40, null=True, db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'/BIC/OHZOHSECTXT',
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=3, db_column=b'/BIC/ZSBCADENA')),
                ('subcadena', models.CharField(max_length=40, null=True, db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'/BIC/OHZOHSCADTX',
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=2, db_column=b'/BIC/ZSUBTICL')),
                ('subtipoCliente', models.CharField(max_length=40, null=True, verbose_name=b'Subtipo Cliente', db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'/BIC/OHZOHSTCLIT',
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=2, db_column=b'/BIC/ZTIPCL')),
                ('tipoCliente', models.CharField(max_length=40, null=True, verbose_name=b'Tipo Cliente', db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'/BIC/OHZOHTCLITX',
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=10, db_column=b'/BIC/ZLZONE')),
                ('zonaReparto', models.CharField(max_length=40, null=True, verbose_name=b'Zona de Reparto', db_column=b'TXTMD')),
            ],
            options={
                'db_table': b'/BIC/OHZOHZONRTX',
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=6, db_column=b'SALES_DIST')),
                ('zonaVentas', models.CharField(max_length=20, null=True, verbose_name=b'Zona de Ventas', db_column=b'TXTSH')),
            ],
            options={
                'db_table': b'/BIC/OHZOHZONVTX',
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
