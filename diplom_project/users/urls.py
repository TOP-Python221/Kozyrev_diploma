from django.urls import path
from .views import *

urlpatterns = [
    path('log', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('register', RegisterUser.as_view(), name='register'),
]
