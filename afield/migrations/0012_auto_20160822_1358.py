# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afield', '0011_auto_20160822_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomaction',
            name='overrideDescription',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
    ]
