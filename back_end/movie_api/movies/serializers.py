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
        fields = ('id', 'name', 'img_url')

class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff')

class CommentSerializer(serializers.ModelSerializer):          
    class Meta:
        model = Comment
        fields = ('id', 'review', 'content', 'user')

class ReviewSerializer(serializers.ModelSerializer):     
    comments = CommentSerializer(many=True, read_only=True, required=False)      
    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'rank', 'movie', 'user', 'comments')

class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True, required=False)
    actors = ActorSerializer(many=True, read_only=True, required=False)
    reviews = ReviewSerializer(many=True, read_only=True, required=False)
    like_users = UserSerializer(many=True, read_only=True, required=False)           
    class Meta:
        model = Movie
        fields = ('id', 'title', 'title_en', 'img_url', 'description', 'director', 'actors', 'genre', 'like_users', 'open_date', 'reviews')

class ReviewListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True, required=False)
    comments = CommentSerializer(many=True, read_only=True, required=False)
    user = UserSerializer(read_only=True, required=False)
    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'rank', 'movie', 'user', 'comments')

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',)

class WorldcupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worldcup
        fields = ('id', 'actors')