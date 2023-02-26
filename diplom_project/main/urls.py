from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPost.as_view(), name='home'),
    path('help', help_me, name='help'),
    path('log', LoginUser.as_view(), name='log'),
    path('logout', logout_user, name='logout'),
    path('register', RegisterUsers.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', CategoryPost.as_view(), name='category'),
    path('add_post', Addpage.as_view(), name='add_post')

]
