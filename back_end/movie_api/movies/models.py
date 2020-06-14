from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    def __str__ (self): 
        return self.username
    pass

class Genre(models.Model):
    name = models.CharField(max_length=20)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='genres', blank=True)
    def __str__ (self): 
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=50)
    def __str__ (self): 
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=140)
    title_en = models.CharField(max_length=140)    
    director = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor, related_name='movies', blank=True)
    img_url = models.TextField()
    description = models.TextField()
    open_date = models.CharField(max_length=50)
    genre = models.ManyToManyField(Genre, related_name='movies', blank=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='movies', blank=True)

    def __str__ (self): 
        return self.title

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)    
    title = models.CharField(max_length = 100)
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)