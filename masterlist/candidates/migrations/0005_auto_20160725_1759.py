# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0004_auto_20160708_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='mask_blue',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='mask_red',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='sb_max',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='sb_min',
        ),
        migrations.AddField(
            model_name='candidate',
            name='data_season',
            field=models.CharField(max_length=64, null=True, verbose_name=b'DES data season'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='dec_field',
            field=models.FloatField(null=True, verbose_name=b'Dec Field'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='followup_date',
            field=models.CharField(max_length=64, null=True, verbose_name=b'followup date'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='followup_facility',
            field=models.CharField(max_length=64, null=True, verbose_name=b'followup facility'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='followup_success',
            field=models.CharField(max_length=64, null=True, verbose_name=b'followup success'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='lens_class',
            field=models.CharField(max_length=64, null=True, verbose_name=b'Lens (Y/N)'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='ra_field',
            field=models.FloatField(null=True, verbose_name=b'RA Field'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='system_type',
            field=models.CharField(max_length=64, null=True, verbose_name=b'Type of Candidate (gal or qso)'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='z_phot_lens',
            field=models.FloatField(null=True, verbose_name=b'Z photo lens'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='z_spec_src',
            field=models.FloatField(null=True, verbose_name=b'Z spec source '),
        ),
    ]
