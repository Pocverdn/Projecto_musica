# Generated by Django 4.1.13 on 2024-04-21 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_graph'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]