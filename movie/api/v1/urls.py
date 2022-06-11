from django.urls import path
from .views import hello,list,get_movie_details,create_movie,update_movie,delete_movie

urlpatterns = [
    path('/hello',hello, name='hello'),
    path('/',list,name='list'),
    path('/create',create_movie,name='create_movie'),
    path('/<pk>/update',update_movie,name='update_movie'),
    path('/<pk>/delete',delete_movie,name='delete_movie'),
    path('/<pk>',get_movie_details,name='movie_details'),


]