# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('migration', '0003_atributomaterial_nivelservicio_ventadiaria'),
    ]

    operations = [
        migrations.AddField(
            model_name='atributocliente',
            name='oficinaVentas',
            field=models.ForeignKey(db_column=b'SALES_OFF', verbose_name=b'Oficina de Ventas',
                                    to='migration.OficinaVentas', null=True, db_index=False),
            preserve_default=True,
        ),
    ]
