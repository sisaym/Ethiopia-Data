# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_cropstatistics_data_missing'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='data_identifier',
            field=models.CharField(default='Crop', max_length=50, choices=[('Crop', 'Crop'), ('Sub', 'Crop_sub_group'), ('Major', 'Crop_major_group')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cropstatistics',
            name='data_missing',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
