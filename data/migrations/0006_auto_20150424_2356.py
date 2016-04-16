# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20150424_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=60, verbose_name='Crop')),
                ('major_group', models.CharField(max_length=30, verbose_name='Major Group')),
                ('sub_group', models.CharField(max_length=30, verbose_name='Sub Group')),
                ('flag', models.ImageField(verbose_name='crop_flag', null=True, upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CropStatistics',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('production_in_quintal', models.FloatField(verbose_name='Production (Quintal)')),
                ('area_cultivate_in_hectares', models.FloatField(verbose_name='Area (Hectares)')),
                ('farmers_growing_crop', models.FloatField(verbose_name='Farmers growing the crop')),
                ('yield_in_quintal_per_hectare', models.FloatField(verbose_name='Yield-Qt/ha')),
                ('crop', models.ForeignKey(to='data.Crop')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50, verbose_name='Region')),
                ('flag', models.ImageField(verbose_name='region_flag', null=True, upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=60, verbose_name='Zone')),
                ('flag', models.ImageField(verbose_name='zone_flag', null=True, upload_to='')),
                ('region', models.ForeignKey(to='data.Region')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cropstatistics',
            name='region',
            field=models.ForeignKey(to='data.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cropstatistics',
            name='year',
            field=models.ForeignKey(to='data.Year'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cropstatistics',
            name='zone',
            field=models.ForeignKey(to='data.Zone'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='import',
            name='Volume_in_tons',
            field=models.FloatField(verbose_name='Volume-tons'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='import',
            name='cif_Value_in_etb',
            field=models.FloatField(verbose_name='Import CIF value in ETB', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='import',
            name='cif_Value_in_usd',
            field=models.FloatField(verbose_name='Import CIF value in USD'),
            preserve_default=True,
        ),
    ]
