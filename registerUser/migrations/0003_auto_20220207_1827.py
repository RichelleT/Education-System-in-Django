# Generated by Django 3.2 on 2022-02-07 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerUser', '0002_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='programme_name',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='school_faculty',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]