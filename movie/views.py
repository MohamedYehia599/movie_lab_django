from django.shortcuts import render, redirect
from django.urls import reverse
from actor.models import Actor
from .models import Movie
from .forms import MovieForm
from django.http.response import HttpResponse, JsonResponse
# Create your views here.
def getMoviesList(request):
    movies = Movie.objects.all()
    # actors = movies.actor.all()
    # print(actors)
    # movie=Movie.objects.get(pk=1)
    # print(movies)
    # actors=Actor.objects.filter(movie_id=1)
    # mov=Movie.objects.filter(actor__name='ahmed')
    # print(mov.actor.all())

    return render(request, 'movie/movies_list.html',context={'movies':movies})
    # return JsonResponse(movies)
def createMovie(request):
    method='create'
    if request.method =='GET' :
        movieForm = MovieForm()
    elif    request.method == 'POST' :
        movieForm = MovieForm(request.POST)
        if movieForm.is_valid():
            movieForm.save()
            return redirect(reverse('movie:getMoviesList'))
    return render(request,'movie/movie_form.html',context={'form':movieForm,'method':method})


def deleteMovie(request,pk):

    Movie.objects.get(pk=pk).delete()
    return(getMoviesList(request))

def updateMovie(request,pk):
    method='update'
    movie= Movie.objects.get(pk=pk)
    if request.method == 'GET':
        movieForm = MovieForm(instance=movie)
    elif request.method == 'POST':
        movieForm = MovieForm(request.POST, instance=movie)
        if movieForm.is_valid():
            movieForm.save()
            return redirect(reverse('movie:getMoviesList'))
    return render(request, 'movie/movie_form.html', context={'form': movieForm,'movie':movie,'method':method})

def showMovie(request,pk):
    movie=Movie.objects.get(pk=pk)
    return render(request,'movie/movie_details.html',context={'movie':movie})