# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '__latest__'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubtipoComision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subtipoComision', models.CharField(max_length=144)),
                ('query', models.TextField()),
                ('tipoCliente', models.ForeignKey(to='maestros.TipoCliente', db_index=False)),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/SUBTIPO/COMISION',
                'verbose_name': b'Tipo de Comision',
                'verbose_name_plural': b'Tipo de Comision',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoComision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipoComision', models.CharField(max_length=100)),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/TIPO/COMISION',
                'verbose_name': b'Tipo de Comision',
                'verbose_name_plural': b'Tipo de Comision',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='subtipocomision',
            name='tipoComision',
            field=models.ForeignKey(to='comisiones.TipoComision', db_index=False),
            preserve_default=True,
        ),
    ]
