# Generated by Django 4.1.13 on 2024-03-11 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='offers',
            field=models.ManyToManyField(to='offer.offer'),
        ),
    ]
