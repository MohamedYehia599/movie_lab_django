from django.contrib import admin

from django.contrib import admin
from movie.models import Movie
from .models import Director
from actor.models import Actor



class MovieInline(admin.TabularInline):
    model=Movie
    extra = 1


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    search_fields = ['movie__name']
    list_display = ['name','gender','age','my_func']
    inlines = [MovieInline]
    def my_func(self,obj):
        movie_name = ','.join([movie.name for movie in obj.movie_set.all()])

        return f"Movies Names: {movie_name}"




# admin.site.register(Movie)