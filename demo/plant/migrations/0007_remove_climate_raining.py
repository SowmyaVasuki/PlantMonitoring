# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-11 15:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0006_climate_raining'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='climate',
            name='raining',
        ),
    ]