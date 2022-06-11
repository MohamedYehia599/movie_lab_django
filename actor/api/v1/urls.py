from django.urls import path
from .views import list,get_actor_details,create_actor,update_actor,delete_actor

urlpatterns = [
    path('/',list,name='list'),
    path('/create',create_actor,name='create_actor'),
    path('/<pk>/update',update_actor,name='update_actor'),
    path('/<pk>/delete',delete_actor,name='delete_actor'),
    path('/<pk>',get_actor_details,name='actor_details'),


]