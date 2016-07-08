# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='id',
            field=models.IntegerField(serialize=False, verbose_name='ID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='rank',
            field=models.IntegerField(verbose_name='Rank'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='thumb',
            field=models.CharField(max_length=255, verbose_name='Image'),
        ),
    ]
