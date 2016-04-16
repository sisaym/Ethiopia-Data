# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_auto_20150427_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecontent',
            name='bg_image',
            field=models.ImageField(upload_to='home_page', default=None, storage=django.core.files.storage.FileSystemStorage(location='/media/home_page'), null=True),
            preserve_default=True,
        ),
    ]
