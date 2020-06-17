from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=20)
    def __str__ (self): 
        return self.name    

class Actor(models.Model):
    name = models.CharField(max_length=50)
    img_url = models.TextField()
    def __str__ (self): 
        return self.name    

class User(AbstractUser):  
    is_staff = models.BooleanField(default=False)      
    def __str__ (self): 
        return self.username
            
class Movie(models.Model):
    title = models.CharField(max_length=140)
    title_en = models.CharField(max_length=140)    
    director = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor, related_name='movie_actors', blank=True)
    img_url = models.TextField()
    description = models.TextField()
    open_date = models.CharField(max_length=50)
    genre = models.ManyToManyField(Genre, related_name='movie_genres', blank=True)    
    
    def __str__ (self): 
        return self.title

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_review', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)    
    title = models.CharField(max_length = 100)
    rank = models.FloatField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comment_user', on_delete=models.CASCADE)    
    review = models.ForeignKey(Review, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Worldcup(models.Model):
    actors = models.ManyToManyField(Actor, related_name='worldcups', blank=True)

    
