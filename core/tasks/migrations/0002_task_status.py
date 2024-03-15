# Generated by Django 4.0 on 2024-03-15 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('TODO', 'To Do'), ('IN_PROGRESS', 'In Progress'), ('DONE', 'Done')], default='TODO', max_length=20),
        ),
    ]