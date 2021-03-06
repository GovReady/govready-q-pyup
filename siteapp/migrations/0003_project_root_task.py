# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-03 18:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guidedmodules', '0003_auto_20160603_1828'),
        ('siteapp', '0002_project_is_account_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='root_task',
            field=models.ForeignKey(blank=True, help_text='The root Task of this Project, which defines the structure of the Project.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='root_of', to='guidedmodules.Task'),
        ),
    ]
