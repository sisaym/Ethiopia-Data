# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20150425_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropstatistics',
            name='data_missing',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
