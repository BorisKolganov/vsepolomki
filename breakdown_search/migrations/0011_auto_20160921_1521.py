# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 12:21
from __future__ import unicode_literals

from django.db import migrations


def make_many_roots(apps, schema_editor):
    Node = apps.get_model('breakdown_search', 'Node')
    for node in Node.objects.all():
        if node.root_node:
            node.root_nodes.add(node.root_node)


class Migration(migrations.Migration):

    dependencies = [
        ('breakdown_search', '0010_auto_20160921_1521'),
    ]

    operations = [
        migrations.RunPython(make_many_roots)
    ]
