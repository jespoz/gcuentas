# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpis', '0002_auto_20141010_1049'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientenoatendido',
            options={'verbose_name': b'Cliente No Atendido', 'verbose_name_plural': b'Clientes No Atendidos'},
        ),
    ]
