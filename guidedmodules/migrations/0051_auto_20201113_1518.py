# Generated by Django 3.0.7 on 2020-11-13 15:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guidedmodules', '0050_auto_20201108_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appsource',
            name='available_to_individual',
            field=models.ManyToManyField(blank=True, help_text='If available_to_all_individuals is False, list the individuals who can start projects defined by Modules provided by this AppSource.', related_name='individual', to=settings.AUTH_USER_MODEL),
        ),
    ]
