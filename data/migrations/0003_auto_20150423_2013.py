# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20150423_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='export',
            name='fob_Value_in_etb',
            field=models.IntegerField(null=True, verbose_name='Export FOB value in ETB'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='export',
            name='item',
            field=models.ForeignKey(to='data.Item', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='import',
            name='cif_Value_in_etb',
            field=models.IntegerField(null=True, verbose_name='Import CIF value in ETB'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='import',
            name='consignment',
            field=models.ForeignKey(to='data.Country', null=True, related_name='consignment_origin', verbose_name='Country of consignment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='import',
            name='item',
            field=models.ForeignKey(to='data.Item', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='export',
            name='Volume_in_tons',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='import',
            name='Volume_in_tons',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='import',
            name='origin',
            field=models.ForeignKey(to='data.Country', verbose_name='Country of origin', related_name='origin_country'),
            preserve_default=True,
        ),
    ]
