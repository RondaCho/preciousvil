# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-12 06:38
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0010_auto_20171012_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='name',
            field=models.CharField(max_length=10, verbose_name='예약자'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='phone_number',
            field=models.CharField(help_text='연락 가능하신 번호를 빈칸없는 형태로 입력해주세요.', max_length=15, validators=[django.core.validators.RegexValidator(message='빈칸없이 번호를 입력하여 주세요.', regex='^\\+\\d{8,15}$')], verbose_name='연락처'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('r', '문의작성완료'), ('v', '찾아가는상담예약중'), ('s', '현장방문상담예약중'), ('c', '상담완료')], max_length=1),
        ),
    ]
