from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import user_signup,user_logout

urlpatterns = [
    path('login',obtain_auth_token, name='login'),
    path('signup',user_signup,name='signup'),
    path('logout',user_logout,name='logout')
]