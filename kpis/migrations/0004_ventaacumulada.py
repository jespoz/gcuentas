# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '__latest__'),
        ('kpis', '0003_auto_20141010_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='VentaAcumulada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(db_column=b'DIM0CALDAY')),
                ('fuente', models.CharField(max_length=3, db_column=b'DIMZFNTEORG')),
                ('unidad', models.FloatField(default=0, db_column=b'KYF4ZABR2I1ILUF')),
                ('kilo', models.FloatField(default=0, db_column=b'KYF4ZABR2XEKJ1U')),
                ('neto', models.FloatField(default=0, db_column=b'KYF4Z6SI9QLJ980')),
                ('cliente', models.ForeignKey(to='maestros.AtributoCliente', db_column=b'DIMZCUSTOMER', db_index=False)),
                ('material', models.ForeignKey(to='maestros.AtributoMaterial', db_column=b'DIMZMATERIAL', db_index=False)),
            ],
            options={
                'db_table': b'GCUENTAS"."/BIC/0CZVDLTSBW/ACUM',
                'verbose_name': b'Venta Acumulada',
                'verbose_name_plural': b'Venta Acumulada',
            },
            bases=(models.Model,),
        ),
    ]
