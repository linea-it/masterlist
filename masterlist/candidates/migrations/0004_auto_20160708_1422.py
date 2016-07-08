# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0003_auto_20160708_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='object_id',
            field=models.CharField(max_length=128, null=True, verbose_name='Object ID'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='vis_end',
            field=models.CharField(max_length=64, null=True, verbose_name='Vis End'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='vis_start',
            field=models.CharField(max_length=64, null=True, verbose_name='Vis Start'),
        ),
    ]
