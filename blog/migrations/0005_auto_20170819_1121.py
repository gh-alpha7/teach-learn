# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170819_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=250)),
                ('user_name', models.CharField(max_length=250)),
                ('answer', models.CharField(max_length=10000)),
            ],
        ),
        migrations.DeleteModel(
            name='answers',
        ),
    ]
