# Generated by Django 2.0.5 on 2018-05-18 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vk', '0002_auto_20180518_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='groupss',
            new_name='group',
        ),
    ]