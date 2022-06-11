from rest_framework import serializers
from movie.models import Movie
from actor.api.v1.serializer import ActorSerializer
class MovieSerializer(serializers.ModelSerializer):
      actor = ActorSerializer(many=True)
      class Meta:
          model = Movie
          fields = '__all__'
          depth=1


class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'