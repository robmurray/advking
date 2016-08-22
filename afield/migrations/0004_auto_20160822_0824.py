# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 13:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('afield', '0003_auto_20160820_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('description', models.CharField(default='', max_length=200)),
                ('createDate', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='date created')),
            ],
        ),
        migrations.AlterField(
            model_name='room',
            name='createDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='roomaction',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afield.Room'),
        ),
    ]
