from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from .models import *

# from django.contrib.auth.models import User
User = get_user_model()

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'movies')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'title', 'content', 'rank', 'movie', 'user')

class ReviewSerializer(serializers.ModelSerializer):     
    comments = CommentSerializer(many=True, read_only=True)       
    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'rank', 'movie', 'user', 'comments')
        
class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    actor = ActorSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)    
    class Meta:
        model = Movie
        fields = ('id', 'title', 'title_en', 'img_url', 'description', 'director', 'actor', 'genre', 'users', 'open_date', 'reviews')

class UserSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'movies', 'is_staff')

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',)

