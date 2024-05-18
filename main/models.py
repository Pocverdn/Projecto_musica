from django.db import models

from offer.models import offer

# Create your models here.

class user(models.Model):
    user_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    instruments = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    years = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='photos_users/')
    description = models.TextField()
    location = models.CharField(max_length=50)
    bands = models.CharField(max_length=1000, blank=True, null=True)
    email = models.EmailField(unique=True, default="correo@dominio.com")


    def add_bands(self, band):
        if self.bands:
            bands_list = self.bands.split(',')
            if band not in bands_list:
                bands_list.append(band)
        else:
            bands_list = [band]

        self.bands = ','.join(bands_list)
        self.save()

    def delete_band(self, band):
        if self.bands:
            bands_list = self.bands.split(',')
            if band in bands_list:
                bands_list.remove(band)


            self.bands = ','.join(bands_list)
            print(self.bands)
            self.save()

    def __str__(self):
        return self.user_name


class project(models.Model):
    project_name = models.CharField(max_length=100)
    genre = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    photo_project = models.ImageField(upload_to='photos_projects/')
    description = models.TextField()
    num_events = models.IntegerField(default=0)
    num_integrants = models.IntegerField(default=1)
    email = models.EmailField(default="correo@dominio.com")

    def __str__(self):
        return self.project_name