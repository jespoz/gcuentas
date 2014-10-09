# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nivel4',
            name='codigo',
            field=models.CharField(unique=True, max_length=11, db_column=b'RPA_WGH4'),
        ),
    ]
