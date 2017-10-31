# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexfeed', '0007_remove_member_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='profile_picture',
            field=models.URLField(default='', max_length=20000),
        ),
    ]