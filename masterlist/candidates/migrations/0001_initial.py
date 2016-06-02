# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('thumb', models.CharField(max_length=255, verbose_name=b'Image')),
                ('id', models.IntegerField(serialize=False, verbose_name=b'ID', primary_key=True)),
                ('ra', models.FloatField()),
                ('dec', models.FloatField()),
                ('rank', models.IntegerField(verbose_name=b'Rank')),
            ],
        ),
    ]
