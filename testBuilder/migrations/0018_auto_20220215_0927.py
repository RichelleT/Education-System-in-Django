# Generated by Django 3.2 on 2022-02-15 01:27

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('testBuilder', '0017_alter_quiz_quest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='op1',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='op2',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='op3',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='op4',
            field=tinymce.models.HTMLField(),
        ),
    ]
