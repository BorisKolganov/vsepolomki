# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-19 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_work_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='latitude',
            field=models.FloatField(default=0, verbose_name='\u0448\u0438\u0440\u043e\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='service',
            name='longitude',
            field=models.FloatField(default=0, verbose_name='\u0434\u043e\u043b\u0433\u043e\u0442\u0430'),
        ),
    ]
