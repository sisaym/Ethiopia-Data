# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_zone_geo_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zone',
            name='geo_choices',
            field=models.CharField(max_length=10, default='Zonal', choices=[('Zonal', 'Zonal'), ('Regional', 'Regional'), ('National', 'National')]),
            preserve_default=True,
        ),
    ]
