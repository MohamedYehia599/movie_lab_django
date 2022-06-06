from django.urls import path
from .views import getMoviesList , createMovie,deleteMovie,updateMovie,showMovie
app_name='movie'

urlpatterns = [
    path('',getMoviesList,name='getMoviesList'),
    path('create',createMovie, name='createMovie'),
    path('delete/<pk>',deleteMovie,name='deleteMovie'),
    path('update/<pk>',updateMovie,name='updateMovie'),
    path('<pk>',showMovie,name='showMovie')


]