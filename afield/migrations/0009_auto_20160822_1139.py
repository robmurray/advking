# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afield', '0008_auto_20160822_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(default='', max_length=200),
        ),
    ]
