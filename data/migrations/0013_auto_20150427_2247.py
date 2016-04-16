# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_homecontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecontent',
            name='bg_image',
            field=models.ImageField(default=None, null=True, upload_to='', storage=django.core.files.storage.FileSystemStorage(location='/media/home_page')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homecontent',
            name='glyphicon_class',
            field=models.CharField(default=None, null=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homecontent',
            name='status',
            field=models.CharField(default=None, choices=[('None', 'None'), ('Updated', 'Updated'), ('under_development', 'Under Development')], max_length=50, null=True),
            preserve_default=True,
        ),
    ]
