# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 14:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('afield', '0004_auto_20160822_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomaction',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='afield.Room'),
        ),
    ]
