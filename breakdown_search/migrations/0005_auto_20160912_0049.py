# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-11 21:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('breakdown_search', '0004_node_answer_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='node',
            old_name='child',
            new_name='root_node',
        ),
    ]