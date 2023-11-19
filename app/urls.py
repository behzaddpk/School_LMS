from django.urls import path
from .views import *

urlpatterns = [
    path('', base, name='base'),
    path('login/', LOGIN, name='login'),
    path('dologin/', DOLOGIN, name='dologin'),
    path('profile/', profile, name='profile'),
    path('profile/update/', UpdateProfile, name='UpdateProfile'),

    path('logout/', LOGOUT, name='logout'),

]