# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-14 08:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20170114_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
