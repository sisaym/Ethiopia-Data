# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_auto_20150426_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone',
            name='geo_choices',
            field=models.CharField(choices=[('Zonal', 'Zonal'), ('Regional', 'Regional'), ('National', 'National')], max_length=10, default='Crop'),
            preserve_default=True,
        ),
    ]
