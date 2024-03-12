from django.db import models

from offer.models import offer

# Create your models here.

class user(models.Model):
    user_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    instruments = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    years = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='photos_users/')
    description = models.TextField()
    location = models.CharField(max_length=50)


class project(models.Model):
    project_name = models.CharField(max_length=100)
    genre = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    photo_project = models.ImageField(upload_to='photos_projects/')
    description = models.TextField()
    num_events = models.IntegerField(default=0)
    num_integrants = models.IntegerField(default=1)
    offers = models.ManyToManyField(offer)