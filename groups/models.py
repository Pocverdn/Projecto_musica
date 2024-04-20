from django.db import models


class Group(models.Model):
    name = models.CharField(max_length = 45)
    description = models.CharField(max_length = 250)
    genre = models.CharField(max_length = 10)
    location = models.CharField(max_length = 10)
    img = models.ImageField(upload_to = 'groups/images/')

