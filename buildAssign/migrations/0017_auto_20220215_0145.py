# Generated by Django 3.2 on 2022-02-14 17:45

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('buildAssign', '0016_auto_20220214_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=django_quill.fields.QuillField(),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=django_quill.fields.QuillField(),
        ),
    ]
