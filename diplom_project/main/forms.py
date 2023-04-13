from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content', 'salary', 'photo', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form_input'}),
            'content': forms.Textarea(attrs={'class': 'form_content'}),

        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    email = forms.CharField(label='Почта')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'passs'}))
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UpDateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(label='Аватар')

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']


class MessageForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'send_msg', 'rows': 3}))

    class Meta:
        model = Message
        fields = ['message', ]
