# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-19 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0021_auto_20171119_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='farmerid',
            field=models.IntegerField(default=0),
        ),
    ]
