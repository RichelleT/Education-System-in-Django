# Generated by Django 3.2 on 2022-02-09 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='programme',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='school_faculty',
            field=models.TextField(blank=True, default='', max_length=150),
        ),
    ]
