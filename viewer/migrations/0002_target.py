# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orientation', models.CharField(max_length=10)),
                ('shape', models.CharField(max_length=10)),
                ('alphanumeric', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
            ],
        ),
    ]
