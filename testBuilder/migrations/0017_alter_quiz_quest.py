# Generated by Django 3.2 on 2022-02-14 19:38

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('testBuilder', '0016_auto_20220215_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='quest',
            field=tinymce.models.HTMLField(),
        ),
    ]