# Generated by Django 4.1.13 on 2024-03-14 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_project_offers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='offers',
        ),
    ]
