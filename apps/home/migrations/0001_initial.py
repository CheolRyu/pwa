# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-16 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=225)),
                ('last_name', models.CharField(max_length=225)),
                ('gender', models.CharField(max_length=225)),
                ('age', models.IntegerField(default=0)),
                ('email', models.TextField(max_length=225)),
                ('hashed_pw', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]