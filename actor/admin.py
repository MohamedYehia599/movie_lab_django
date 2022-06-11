import datetime


from django.contrib import admin
from .models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['gender',]
    list_display = ['name','gender','calculate_age','get_movies_count','get_actor_movies']

    def calculate_age(self,obj):
        current_year = datetime.datetime.now().year
        return f'age : {current_year - obj.birth_date.year}'

    calculate_age.short_description = 'Age'
    def get_movies_count(self,obj):
        movies = obj.movie_set.count()
        print(movies)
        return f'{movies}'

    get_movies_count.short_description = 'Movies count'
    def get_actor_movies(self,obj):
        movies = ', '.join([movie.name for movie in obj.movie_set.all()])
        return f'movies : {movies}'

    get_actor_movies.short_description = 'Movies '