# Generated by Django 2.0.5 on 2018-05-18 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vk', '0003_auto_20180518_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='group',
        ),
    ]
