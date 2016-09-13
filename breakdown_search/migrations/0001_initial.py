# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-10 21:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstructionStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=1000)),
                ('next_step', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='breakdown_search.InstructionStep')),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_text', models.TextField(blank=True, max_length=1000)),
                ('child', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='breakdown_search.Node')),
                ('instruction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='breakdown_search.InstructionStep')),
            ],
        ),
    ]