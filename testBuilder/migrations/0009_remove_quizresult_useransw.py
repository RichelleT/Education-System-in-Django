# Generated by Django 3.2 on 2022-02-10 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testBuilder', '0008_quizresult_useransw'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizresult',
            name='userAnsw',
        ),
    ]
