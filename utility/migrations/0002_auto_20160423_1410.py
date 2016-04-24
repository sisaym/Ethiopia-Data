# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-23 11:10
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('page_url', models.CharField(blank=True, max_length=100)),
                ('bg_image', models.ImageField(default=None, null=True, storage=django.core.files.storage.FileSystemStorage(location='/media/home_page'), upload_to='home_page')),
                ('glyphicon_class', models.CharField(default=None, max_length=100, null=True)),
                ('status', models.CharField(choices=[('None', 'None'), ('Updated', 'Updated'), ('under_development', 'Under Development')], default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubPages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('page_url', models.CharField(max_length=50)),
                ('homepage', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='utility.HomePage')),
            ],
        ),
        migrations.DeleteModel(
            name='HomeContent',
        ),
    ]