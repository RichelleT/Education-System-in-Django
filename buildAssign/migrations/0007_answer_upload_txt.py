# Generated by Django 3.2 on 2022-02-11 05:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildAssign', '0006_remove_assignresult_linked_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='upload_txt',
            field=models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['txt'])]),
        ),
    ]
