# Generated by Django 3.0.5 on 2020-10-12 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0002_remove_todo_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='name',
            field=models.CharField(default='', max_length=10),
        ),
    ]