# Generated by Django 3.2 on 2022-02-10 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buildAssign', '0004_answer_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignresult',
            name='a_time',
        ),
        migrations.AddField(
            model_name='assignresult',
            name='link_ques',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buildAssign.answer'),
        ),
        migrations.AlterField(
            model_name='assignresult',
            name='attempted_time',
            field=models.DateTimeField(),
        ),
    ]
