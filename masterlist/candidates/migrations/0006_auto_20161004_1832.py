# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0005_auto_20160725_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='dec_field',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='mag_max',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='mag_min',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='position_angle',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='ra_field',
        ),
    ]
