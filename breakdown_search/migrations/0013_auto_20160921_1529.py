# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breakdown_search', '0012_remove_node_root_node'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='root_nodes',
            field=models.ManyToManyField(blank=True, to='breakdown_search.Node'),
        ),
    ]