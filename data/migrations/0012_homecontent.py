# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_auto_20150426_0827'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeContent',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=5000)),
                ('page_url', models.CharField(max_length=100)),
                ('sub_pages_url', models.CharField(help_text='Please insert comma separated list of pages urls', max_length=300, null=True)),
                ('bg_image', models.ImageField(upload_to='', null=True)),
                ('glyphicon_class', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('None', 'None'), ('Updated', 'Updated'), ('under_development', 'Under Development')], max_length=50, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
