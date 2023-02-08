from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('help', views.help_me, name='help'),
    path('sing_up', views.sing_up, name='sing_up')
]
