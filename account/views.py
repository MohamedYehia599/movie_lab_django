from django.shortcuts import render ,redirect,reverse
from movie.views import getMoviesList
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .userForm import UserForm
# Create your views here.
def signup(request):
    form = UserForm(request.POST or None)
    if(form.is_valid()):
        form.save()
        return redirect(reverse('movie:getMoviesList'))

    return render(request, 'registration/signup.html', context={'form': form})
