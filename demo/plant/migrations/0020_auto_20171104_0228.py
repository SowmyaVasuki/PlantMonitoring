# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-03 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0019_auto_20171104_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actuator',
            name='wb_id',
            field=models.IntegerField(default=1),
        ),
    ]
