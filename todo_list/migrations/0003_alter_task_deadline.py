# Generated by Django 5.1.7 on 2025-03-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_alter_tag_name_alter_task_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True),
        ),
    ]
