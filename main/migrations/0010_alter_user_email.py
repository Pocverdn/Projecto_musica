# Generated by Django 4.1.13 on 2024-05-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='correo@dominio.com', max_length=254, unique=True),
        ),
    ]