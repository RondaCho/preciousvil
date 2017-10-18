# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-18 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0018_auto_20171018_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='password',
            field=models.CharField(blank=True, help_text='(선택항목)문의글을 잠그시려면 비밀번호를 입력해주세요(30자이내)', max_length=30, verbose_name='비밀번호'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(default='1111-11-11', help_text='2018-01-03 와 같은 형식으로 입력해주세요. 더 많은 날짜는 하단의 추가사항에 입력해주세요.', verbose_name='상담예약일'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='type_set',
            field=models.ManyToManyField(blank=True, help_text='(선택항목/다수선택가능)관심있는 타입을 작성해주세요', to='welcome.Type', verbose_name='관심타입'),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]