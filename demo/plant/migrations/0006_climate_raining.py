# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-11 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0005_auto_20171006_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='climate',
            name='raining',
            field=models.IntegerField(default=0),
        ),
    ]