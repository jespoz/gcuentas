# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0002_auto_20141009_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtributoInterlocutor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rut', models.CharField(max_length=11, null=True, db_column=b'TAX_NUMB2')),
                ('interlocutor', models.ForeignKey(db_column=b'/BIC/ZCUSTOMER', to='maestros.Cliente', unique=True)),
            ],
            options={
                'db_table': b'/BIC/OHZOHINTEAT',
                'verbose_name': b'Atributo de Interlocutor',
                'verbose_name_plural': b'Atributos de Interlocutores',
            },
            bases=(models.Model,),
        ),
    ]
