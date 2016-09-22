# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breakdown_search', '0013_auto_20160921_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='low_mileage',
            field=models.IntegerField(default=10000000, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u043d\u043e\u0434\u0443, \u0435\u0441\u043b\u0438 \u043f\u0440\u043e\u0431\u0435\u0433 \u043c\u0435\u043d\u044c\u0448\u0435'),
        ),
        migrations.AlterField(
            model_name='node',
            name='mileage',
            field=models.IntegerField(default=0, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u043d\u043e\u0434\u0443, \u0435\u0441\u043b\u0438 \u043f\u0440\u043e\u0431\u0435\u0433 \u0431\u043e\u043b\u044c\u0448\u0435'),
        ),
    ]