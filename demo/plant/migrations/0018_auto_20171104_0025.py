# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-03 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0017_auto_20171104_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actuator',
            name='mode',
            field=models.CharField(default='Automatic', max_length=10),
        ),
        migrations.AlterField(
            model_name='actuator',
            name='status',
            field=models.CharField(default='OFF', max_length=10),
        ),
    ]
