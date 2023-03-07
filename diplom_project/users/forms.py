from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserMain


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    email = forms.CharField(label='Почта')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'passs'}))
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput())

    class Meta:
        model = UserMain
        fields = ['username', 'password1', 'password2']


class UpDateProfile(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput())
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    email = forms.EmailField(label='Почта')

    class Meta:
        model = UserMain
        fields = ['username', 'first_name', 'last_name', 'email', ]
