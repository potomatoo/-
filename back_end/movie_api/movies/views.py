from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q, Value
from rest_framework.permissions import AllowAny # 회원가입은 인증 X

from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

import random
import urllib
import json

def random_sampling(movies):
    sample = []
    random_movie = []

    while len(random_movie) != 5:
        new_number = random.randint(0, len(movies)-1)
        if new_number not in random_movie:
            random_movie.append(new_number)

    for index in random_movie:
        sample.append(movies[index])

    return sample

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
@api_view(['POST'])
def user_update(request, user_pk):    
    user = get_object_or_404(User, pk=user_pk)   
    serializer = UserSerializer(user, data=request.data)    
    if serializer.is_valid(raise_exception=True):
        
        serializer.save()
        return Response(serializer.data)
    
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

@api_view(['GET', 'POST'])
def weather_recommend(request):   
    ServiceKey = '7r002FWJrOZmqbjLfrDYopN40a1SRIbj9FycuHMeYBjc89qpG%2BMxPpH8HsJGui2edG23nhfPz9OVUWQRqW0QyA%3D%3D'
    request = json.loads(request.body)
    code = request['location_code']
    
    url = f'http://apis.data.go.kr/1360000/VilageFcstMsgService/getLandFcst?serviceKey={ServiceKey}&pageNo=1&numOfRows=10&dataType=JSON&regId={code}&'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    
    if(rescode==200):
        response_body = response.read()
        dict = json.loads(response_body.decode('utf-8'))        
    else:
        print("Error Code:" + rescode)

    is_rain = dict['response']['body']['items']['item'][1]['wf']

    weather_status = dict['response']['body']['items']['item'][1]['rnYn']
    # is_rain = 0
    # weather_status = '흐림'    
    if is_rain != 0:
        movies = Movie.objects.filter(Q(genre = 3) | Q(genre = 6) | Q(genre = 8)).distinct()
        sample = random_sampling(movies)
    else:
        if weather_status == '맑음':
            movies = Movie.objects.filter(Q(genre = 15) | Q(genre = 10) | Q(genre = 14)).distinct()           
            sample = random_sampling(movies)

        elif weather_status == '구름많음':
            movies = Movie.objects.filter(Q(genre = 1) | Q(genre = 2) | Q(genre = 11) | Q(genre = 12) | Q(genre = 7)).distinct()            
            sample = random_sampling(movies)

        elif weather_status == '흐림':
            movies = Movie.objects.filter(Q(genre = 4) | Q(genre = 5) | Q(genre = 9) | Q(genre = 13)).distinct()            
            sample = random_sampling(movies)
    
    movie_serializer = MovieSerializer(sample, many=True, required=False)
    return Response(movie_serializer.data)

@api_view(['GET'])
def like_genre(request, user_pk):
    over_4_reviews = Review.objects.filter(Q(user=request.user) & Q(rank__gte = 4))
    
    like_genre = [0 for _ in range(16)]
    for recommend in over_4_reviews:
        
        movies = Movie.objects.get(id=recommend.movie_id).genre.values()
        for movie in movies:
            like_genre[movie['id']] += 1
    
    recommend_genre = like_genre.index(max(like_genre))
    result_movies = Movie.objects.filter(genre=recommend_genre)

    movie_serializer = MovieSerializer(result_movies, many=True)
    return Response(movie_serializer.data)

 # .../worldcup/
@api_view(['GET'])
def worldcup_recommend(request):
    actors = Actor.objects.filter(~Q(img_url = 'https://image.flaticon.com/icons/svg/1077/1077114.svg'))
    random_actors = random.sample(list(actors), 32)
    worldcup = Worldcup()
    worldcup.save()
    worldcup.actors.set(random_actors)
    worldcup_serializer = WorldcupSerializer(worldcup)
    return Response(worldcup_serializer.data)


@api_view(['POST'])
def actor_recommend(request):
    movies = Movie.objects.filter(actors=request.data['actor'])
    print(request.data['actor'])
    movie_serializer = MovieSerializer(movies, many=True, required=False)
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
    reviews = Review.objects.all().order_by('-id')
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
    if serializer.is_valid():
        serializer.movie = movie
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(False)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_review(request, review_pk):    
    review = get_object_or_404(Review, pk=review_pk)
    review.delete()
    return Response('REVIEW DELETE!!')

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
    
    serializer = CommentSerializer(data=request.data)    
    if serializer.is_valid(raise_exception=True):
        serializer.review = review
        serializer.user = request.user
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_comment(request, comment_pk):    
    comment = get_object_or_404(Comment, pk=comment_pk)   
    comment.delete()
    return Response('COMMENT DELETE!!')
