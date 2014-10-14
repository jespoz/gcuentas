# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientenoatendido',
            name='localesMes',
            field=models.FloatField(default=0, db_column=b'KYF44LHLWIKYTSO'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientenoatendido',
            name='localesNoAtendidos',
            field=models.FloatField(default=0, db_column=b'KYF4ZFQCJ8RYJ1L'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientenoatendido',
            name='localesTresMes',
            field=models.FloatField(default=0, db_column=b'KYF44LHLWIKYTS01'),
            preserve_default=True,
        ),
    ]
