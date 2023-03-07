from django.urls import path
from .views import *

urlpatterns = [
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('register', RegisterUser.as_view(), name='register'),
    path('profile_user/<slug:slug>/', Profile_User.as_view(), name='profile_user'),
]
