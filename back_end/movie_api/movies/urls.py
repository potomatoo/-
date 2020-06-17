from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('user/', views.signup, name='signup'),
    path('<int:user_pk>/user_update/', views.user_update, name='user_update'),
    path('userList/', views.userlist, name='userlist'),
    path('is_staff/<int:user_pk>/', views.is_staff, name='is_staff'),
    path('my_movies/', views.my_movies, name='my_movies'),
    path('movie/', views.movie, name='movie'),
    path('movie/<int:movie_pk>/', views.movie_detail, name='movie_detail'),

    path('actor/', views.actor, name='actor'),
    path('actor/<int:actor_pk>/', views.actor_detail, name='actor_detail'),

    path('genre/', views.genre, name='genre'),
    path('genre/<int:genre_pk>/', views.genre_detail, name='genre_detail'),

    path('review/', views.review_list, name='review_list'),
    path('movie/<int:movie_pk>/review/', views.movie_review, name='movie_review'),
    path('review/<int:review_pk>/', views.detail_review_list, name='detail_review_list'),
    path('<int:movie_pk>/review/create/', views.create_review, name='create_review'),    
    path('<int:movie_pk>/review/<int:review_pk>/update/', views.update_review, name='update_review'),
    path('review/<int:review_pk>/delete/', views.delete_review, name='delete_review'),

    path('review/<int:review_pk>/comment/', views.comment_list, name='comment_list'),
    path('review/<int:review_pk>/comment/create/', views.create_comment, name='create_comment'),
    path('comment/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),

    path('weather_recommend/', views.weather_recommend, name='weather_recommend'),
    path('actor_recommend/', views.actor_recommend, name="actor_recommend"),
    path('<int:user_pk>/like_genre/', views.like_genre, name='like_genre'),
    path('worldcup_recommend/', views.worldcup_recommend, name='worldcup_recommend'),
]
