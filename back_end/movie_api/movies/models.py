from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    pass

class Genre(models.Model):
    name = models.CharField(max_length=20)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='genres', blank=True)

class Actor(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=140)
<<<<<<< HEAD
    title_en = models.CharField(max_length=140)
    rate = models.CharField(max_length=100)
=======
    title_en = models.CharField(max_length=140)    
>>>>>>> 9ddd8c4f0ef1203053298a3fb11bce6adefcb411
    director = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor, related_name='movies', blank=True)
    img_url = models.TextField()
    description = models.TextField()
    open_date = models.CharField(max_length=50)
    genre = models.ManyToManyField(Genre, related_name='movies', blank=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='movies', blank=True)
    
