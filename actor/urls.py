from django.urls import path
from .views import getActorsList,createActor,updateActor,deleteActor,showActor
app_name='actor'
urlpatterns = [
    path('',getActorsList,name='getActorsList'),
    path('create',createActor,name='createActor'),
    path('update/<pk>',updateActor,name='updateActor'),
    path('delete/<pk>',deleteActor,name='deleteActor'),
    path('<pk>',showActor,name='showActor'),


    # path('movies/',include('movie.urls'))
]