from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from movie.models import Movie
from .serializer import MovieSerializer,MovieCreateSerializer
@api_view(['GET'])
def hello (request):
    return Response(data={},status=status.HTTP_200_OK)

@api_view(['GET'])
def list(request):

    movies = Movie.objects.all()
    ser=MovieSerializer(instance=movies,many=True)
    return Response(data=ser.data, status=status.HTTP_200_OK)

@api_view(['Get'])
def get_movie_details(request,pk):
    movie = Movie.objects.get(pk=pk)
    ser = MovieSerializer(instance=movie)
    return Response(data=ser.data, status=status.HTTP_200_OK)
@api_view(['POST'])
def create_movie(request):

        serializer = MovieCreateSerializer(data=request.data)

        if (serializer.is_valid()):
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','PATCH'])
def update_movie(request,pk):
        movie = Movie.objects.get(pk=pk)
        if(request.method == 'PUT'):
            serializer = MovieCreateSerializer(data=request.data,instance=movie)
        else:
            serializer = MovieCreateSerializer(data=request.data, instance=movie,partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED_OK)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_movie(request,pk):
    if Movie.objects.get(pk=pk).delete():
        return Response(data={'detail':'movie deleted successfully'},status=status.HTTP_204_NO_CONTENT)
