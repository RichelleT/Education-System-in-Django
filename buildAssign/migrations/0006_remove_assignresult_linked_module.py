# Generated by Django 3.2 on 2022-02-11 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildAssign', '0005_auto_20220211_0628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignresult',
            name='linked_module',
        ),
    ]
