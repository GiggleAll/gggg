# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-27 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_courseorganization_organization_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorganization',
            name='study_number',
            field=models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u4eba\u6570'),
        ),
    ]