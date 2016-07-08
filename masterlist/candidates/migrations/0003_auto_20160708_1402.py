# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_auto_20160708_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='mag_max',
            field=models.FloatField(verbose_name='Mag Max', null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='mag_min',
            field=models.FloatField(verbose_name='Mag Min', null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='mask_blue',
            field=models.FloatField(verbose_name='Mask Blue', null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='mask_red',
            field=models.FloatField(verbose_name='Mask Red', null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='position_angle',
            field=models.FloatField(verbose_name='position angle', null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='sb_max',
            field=models.FloatField(verbose_name='SB Max', null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='sb_min',
            field=models.FloatField(verbose_name='SB Min', null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='vis_end',
            field=models.FloatField(verbose_name='Vis End', null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='vis_start',
            field=models.FloatField(verbose_name='Vis Start', null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='dec',
            field=models.FloatField(verbose_name='Dec'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='ra',
            field=models.FloatField(verbose_name='RA'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='rank',
            field=models.IntegerField(verbose_name='Rank', null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='thumb',
            field=models.CharField(verbose_name='Image', max_length=255, null=True),
        ),
    ]
