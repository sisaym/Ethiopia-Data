# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20150424_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='name_slug',
            field=models.SlugField(default='', max_length=110),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crop',
            name='major_group_slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crop',
            name='name_slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crop',
            name='sub_group_slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='region',
            name='name_slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zone',
            name='name_slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
