from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from actor.models import Actor
from .serializer import ActorSerializer,ActorCreateSerializer
from rest_framework.decorators import permission_classes
from .permissions import GroupPermission

@api_view(['GET'])
@permission_classes([GroupPermission])
def list(request):

    actors = Actor.objects.all()
    ser=ActorSerializer(instance=actors,many=True)
    return Response(data=ser.data, status=status.HTTP_200_OK)

@api_view(['Get'])
def get_actor_details(request,pk):
    actor = Actor.objects.get(pk=pk)
    ser = ActorSerializer(instance=actor)
    return Response(data=ser.data, status=status.HTTP_200_OK)
@api_view(['POST'])
def create_actor(request):

        serializer = ActorCreateSerializer(data=request.data)

        if (serializer.is_valid()):
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','PATCH'])
def update_actor(request,pk):
        actor = Actor.objects.get(pk=pk)
        if(request.method == 'PUT'):
            serializer = ActorCreateSerializer(data=request.data,instance=actor)
        else:
            serializer = ActorCreateSerializer(data=request.data, instance=actor,partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_actor(request,pk):
    if Actor.objects.get(pk=pk).delete():
        return Response(data={'detail':'actor deleted successfully'},status=status.HTTP_204_NO_CONTENT)
