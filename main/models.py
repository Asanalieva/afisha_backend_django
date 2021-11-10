from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cinema(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    cinema = models.ForeignKey(Cinema,on_delete=models.CASCADE,null=True) #ForeignKey
    genres = models.ManyToManyField(Genre,null=True, blank=True) #ManyToManyField


    def __str__(self):
        return self.title

class Review(models.Model):

    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,null=True) #ForeignKey


    def __str__(self):
        return self.text

