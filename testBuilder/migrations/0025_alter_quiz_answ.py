# Generated by Django 3.2 on 2022-02-08 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testBuilder', '0024_auto_20220208_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='answ',
            field=models.CharField(choices=[('option1', 'option1'), ('option2', 'option2'), ('option3', 'option3'), ('option4', 'option4')], default='', max_length=7),
        ),
    ]
