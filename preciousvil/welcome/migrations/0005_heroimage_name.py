# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-09 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0004_heroimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroimage',
            name='name',
            field=models.CharField(default='히어로이미지', max_length=20),
        ),
    ]
