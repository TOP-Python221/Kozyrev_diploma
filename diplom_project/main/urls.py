from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPost.as_view(), name='home'),
    path('message', AllChat.as_view(), name='message'),
    path('new_msg', new_msg, name='new_msg'),
    path('post/<int:pk>/', ShowPost.as_view(), name='post'),
    path('/<int:pk>/', response, name='response'),
    path('category/<slug:cat_slug>/', CategoryPost.as_view(), name='category'),
    path('add_post', Addpage.as_view(), name='add_post'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('register', RegisterUser.as_view(), name='register'),
    path('profile_user/<slug:slug>/', Profile_User.as_view(), name='profile_user'),
    path('setings/<slug:slug>/', UpDateProfileView.as_view(), name='update_profile'),
    path('dialog/<slug:slug>/', Chat.as_view(), name='chat'),
    path('sent_msg/<slug:slug>/', send_message, name='sent_msg'),
    path('rec_msg/<slug:slug>/', received_message, name='rec_msg')

]
