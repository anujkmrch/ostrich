# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-09 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ostrich', '0003_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='mobile',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]