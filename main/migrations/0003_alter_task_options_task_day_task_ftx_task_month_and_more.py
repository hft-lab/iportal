# Generated by Django 4.1 on 2022-09-07 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_task_created_at_task_updated_at_alter_task_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Отчет'},
        ),
        migrations.AddField(
            model_name='task',
            name='day',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='ftx',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='month',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='waves',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.TextField(blank=True),
        ),
    ]
