# Generated by Django 3.2 on 2022-02-08 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testBuilder', '0028_auto_20220208_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizresult',
            name='a_time',
        ),
    ]