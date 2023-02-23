from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('help', help_me, name='help'),
    path('sing_up', sing_up, name='sing_up'),
    path('register', register_users, name='register'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('add_post', add_post, name='add_post')

]
