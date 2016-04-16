# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20150423_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name_slug',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
