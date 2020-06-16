from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from rest_framework.permissions import AllowAny # 회원가입은 인증 X

from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

# .../user/
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid():
        user=serializer.save()
        user.set_password(user.password)
        user.save()
        return Response(status=200, data={'message': '회원가입 성공'})

# .../user/user_pk/
@api_view(['GET'])
def user_info(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    user_serializer = UserSerializer(user)
    return Response(user_serializer.data)

@api_view(['GET'])
def userlist(request):
    users = User.objects.all()
    user_serializer = UserSerializer(users, many=True)
    return Response(user_serializer.data)

@api_view(['POST'])
def is_staff(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    user_serializer = UserSerializer(user, many=False)
    return Response(user_serializer)

# .../my_movies/
@api_view(['GET'])
def my_movies(request, user_pk):
    user = Review.objects.filter(user=user_pk)   
    user_serializer = ReviewSerializer(user, many=True)
    return Response(user_serializer.data)

# .../movie/
@api_view(['GET'])
def movie(request):
    movies = Movie.objects.all()
    movie_serializer = MovieSerializer(movies, many=True)
    return Response(movie_serializer.data)

@api_view(['GET'])
def weather_recommend(request):  
    if request.data['is_rain'] == 'true':
        movies = Movie.objects.filter(Q(genre = 3) | Q(genre = 6) | Q(genre = 8) | Q(genre = 8))
    else:
        if request.data['weather'] == '맑음':
            movies = Movie.objects.filter(Q(genre = 10) | Q(genre = 14) | Q(genre = 15))       
            
        elif request.data['weather'] == '구름많음':
            movies = Movie.objects.filter(Q(genre = 3) | Q(genre = 4))

        elif request.data['weather'] == '흐림':
            movies = Movie.objects.filter(Q(genre = 4) | Q(genre = 5) | Q(genre = 9))

    movie_serializer = MovieSerializer(movies, many=True)
    return Response(movie_serializer.data)

# .../movie/pk/
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie_detail_serializer = MovieSerializer(movie)
    return Response(movie_detail_serializer.data)

# .../actor/
@api_view(['GET'])
def actor(request):
    actors = Actor.objects.all()

    actors_serializer = ActorSerializer(actors, many=True)
    return Response(actors_serializer.data)

# .../actor/pk/
@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)

    actor_serializer = ActorSerializer(actor)
    return Response(actor_serializer.data)

# .../genre/
@api_view(['GET'])
def genre(request):
    genres = Genre.objects.all()
    genres_serializer = GenreSerializer(genres, many=True)
    return Response(genres_serializer.data)

# .../genre/pk/
@api_view(['GET'])
def genre_detail(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    genre_serializer = GenreSerializer(genre)
    return Response(genre_serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_review(request, movie_pk):
    reviews = Review.objects.filter(movie=movie_pk)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail_review_list(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(review, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)   
     
    serializer = ReviewSerializer(data=request.data)    
    if serializer.is_valid(raise_exception=True):
        serializer.movie = movie
        serializer.user = request.user
        serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_review(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)    
    review = get_object_or_404(Review, pk=review_pk)   
    serializer = ReviewSerializer(instance=review, data=request.data)    
    if serializer.is_valid() and request.user == review.user:
        serializer.movie = movie
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(False)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_review(request, review_pk):    
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        review.delete()
        return Response('REVIEW DELETE!!')
    else:
        return Response(False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def comment_list(request, review_pk):
    comments = Comment.objects.filter(review=review_pk)    
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, review_pk):    
    review = get_object_or_404(Review, pk=review_pk)    
    request.data['user'] = request.user
    serializer = CommentSerializer(data=request.data)    
    if serializer.is_valid(raise_exception=True):
        serializer.review = review
        serializer.user = request.user
        serializer.save()
    return Response(request.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_comment(request, comment_pk):    
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:        
        comment.delete()
        return Response('COMMENT DELETE!!')
    else:
        return Response(False)

