# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-01 20:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_remove_courseorganization_course'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='organization',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrganization', verbose_name='\u8bfe\u7a0b\u673a\u6784\u5916\u952e'),
            preserve_default=False,
        ),
    ]
