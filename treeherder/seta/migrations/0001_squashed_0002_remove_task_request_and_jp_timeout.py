# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPriority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testtype', models.CharField(max_length=128)),
                ('buildsystem', models.CharField(max_length=64)),
                ('buildtype', models.CharField(max_length=64)),
                ('platform', models.CharField(max_length=64)),
                ('priority', models.IntegerField()),
                ('expiration_date', models.DateTimeField(null=True)),
            ],
        ),
    ]
