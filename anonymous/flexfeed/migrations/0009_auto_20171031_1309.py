# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 17:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flexfeed', '0008_member_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='stock',
            field=models.ForeignKey(blank=True, help_text='Select a stock for this member', null=True, on_delete=django.db.models.deletion.CASCADE, to='flexfeed.Stock'),
        ),
    ]