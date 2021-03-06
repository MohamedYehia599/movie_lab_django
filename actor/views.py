from django.shortcuts import render, redirect , reverse


from .forms import ActorForm
from .models import Actor
from django.contrib.auth.decorators import login_required
def getActorsList(request):
    actors=Actor.objects.all()
    for actor in actors:
        print(f'from actors list {actor.picture}')
    return render(request,'actor/actors_list.html',context={'actors':actors})
@login_required
def createActor(request):
    method = 'create'
    print(request.method)
    if request.method == 'GET':
        actorForm = ActorForm(files=request.FILES)
    elif request.method == 'POST':
        actorForm = ActorForm(request.POST,files=request.FILES)
        if actorForm.is_valid():
            actorForm.save()
            return redirect(reverse('actor:getActorsList'))
    return render(request,'actor/actor_form.html',context={'form':actorForm,'method':method})

def deleteActor(request,pk):
    Actor.objects.get(pk=pk).delete()
    return redirect(reverse('actor:getActorsList'))

def updateActor(request,pk):
    method='update'
    actor = Actor.objects.get(pk=pk)
    if request.method == 'GET':
        actorForm = ActorForm(instance=actor,files=request.FILES)
        return render(request, 'actor/actor_form.html', context={'form': actorForm, 'method': method, 'actor': actor})
    elif request.method == 'POST':
         actorForm = ActorForm(request.POST,instance=actor,files=request.FILES)
         if actorForm.is_valid():
            actorForm.save()
            return redirect(reverse('actor:getActorsList'))


def showActor(request,pk):
    actor = Actor.objects.get(pk=pk)
    print(f'from show actor {actor.picture}')
    return render(request,'actor/actor_details.html',context={'actor':actor})