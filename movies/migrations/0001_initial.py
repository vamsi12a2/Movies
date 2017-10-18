# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-15 14:45
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('movies_list', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]