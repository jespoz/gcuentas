# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('migration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atributocliente',
            name='cadena',
            field=models.ForeignKey(to='migration.Cadena', null=True, db_column=b'/BIC/ZCADENA', db_index=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='atributocliente',
            name='subtipoCliente',
            field=models.ForeignKey(db_column=b'/BIC/ZSUBTICL', verbose_name=b'Subtipo de Cliente',
                                    to='migration.SubtipoCliente', null=True, db_index=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='atributocliente',
            name='tipoCliente',
            field=models.ForeignKey(db_column=b'/BIC/ZTIPCL', verbose_name=b'Tipo de Cliente',
                                    to='migration.TipoCliente', null=True, db_index=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='atributocliente',
            name='zonaReparto',
            field=models.ForeignKey(db_column=b'/BIC/ZLZONE', verbose_name=b'Zona de Reporte',
                                    to='migration.ZonaReparto', null=True, db_index=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='atributocliente',
            name='zonaVentas',
            field=models.ForeignKey(db_column=b'SALES_DIST', verbose_name=b'Zona de Ventas', to='migration.ZonaVentas',
                                    null=True, db_index=False),
            preserve_default=True,
        ),
    ]
