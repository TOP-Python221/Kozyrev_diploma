from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content', 'photo', 'cat']
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


class UpDateProfile(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput())
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    email = forms.EmailField(label='Почта')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', ]
