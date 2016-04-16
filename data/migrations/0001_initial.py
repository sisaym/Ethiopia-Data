# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Export',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('Volume_in_tons', models.IntegerField()),
                ('fob_Value_in_usd', models.IntegerField(verbose_name='Export FOB value in USD')),
                ('destination', models.ForeignKey(to='data.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Import',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('Volume_in_tons', models.IntegerField()),
                ('cif_Value_in_usd', models.IntegerField(verbose_name='Import CIF value in USD')),
                ('origin', models.ForeignKey(to='data.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=1000)),
                ('commodity', models.ForeignKey(to='data.Commodity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('year_code', models.IntegerField(primary_key=True, serialize=False)),
                ('ethiopian_year', models.CharField(max_length=7)),
                ('european_year', models.CharField(max_length=7)),
                ('eth_year', models.IntegerField()),
                ('eur_year', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='import',
            name='year',
            field=models.ForeignKey(to='data.Year'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='export',
            name='year',
            field=models.ForeignKey(to='data.Year'),
            preserve_default=True,
        ),
    ]
