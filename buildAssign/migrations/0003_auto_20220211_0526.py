# Generated by Django 3.2 on 2022-02-10 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buildAssign', '0002_auto_20220210_0513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='question',
            new_name='assign_name',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='answer',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='created_date',
            field=models.DateTimeField(),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(default='', max_length=5000)),
                ('answer', models.TextField(default='', max_length=5000)),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('link_assign', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buildAssign.assignment')),
            ],
        ),
    ]
