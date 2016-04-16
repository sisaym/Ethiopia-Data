# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_item_name_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name_slug',
            field=models.SlugField(max_length=300),
            preserve_default=True,
        ),
    ]
