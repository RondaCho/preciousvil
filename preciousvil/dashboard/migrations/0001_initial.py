# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 04:47
from __future__ import unicode_literals

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Simple(57)', '57'), ('Harmonious(65)', '65'), ('Perfect(68)', '68'), ('Luxury(77)', '77')], max_length=20)),
                ('address', models.CharField(help_text='A-1과 같은 형식으로 입력해주세요', max_length=3, unique=True)),
                ('total_land', models.IntegerField()),
                ('your_land', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='House_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='본 포스팅의 제목을 입력해주세요.', max_length=100, validators=[dashboard.models.min_length_10_validators], verbose_name='제목')),
                ('content', models.TextField(verbose_name='상세 내용')),
                ('photo', models.ImageField(upload_to='progress/%Y/%m/%d')),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='progress',
            name='tag_set',
            field=models.ManyToManyField(blank=True, to='dashboard.Tag'),
        ),
        migrations.AddField(
            model_name='house',
            name='house_tag_set',
            field=models.ManyToManyField(blank=True, to='dashboard.House_Tag'),
        ),
    ]
