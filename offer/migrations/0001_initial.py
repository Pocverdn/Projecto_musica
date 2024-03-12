# Generated by Django 4.1.13 on 2024-03-06 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle_offer', models.CharField(max_length=200)),
                ('description_offer', models.TextField()),
                ('group_name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=50)),
                ('instruments', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('years', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
