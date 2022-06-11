from django.contrib import admin
from .models import Movie
from actor.models import Actor



@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name','production_year','creation_time','get_movie_actors']

    def get_movie_actors(self,obj):
        actors = ', '.join([actor.name for actor in obj.actor.all()])
        print( f'object is {obj.director}')
        return f'actors : {actors}'


