# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afield', '0010_auto_20160822_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomaction',
            name='description',
        ),
        migrations.AddField(
            model_name='roomaction',
            name='overrideDescription',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
