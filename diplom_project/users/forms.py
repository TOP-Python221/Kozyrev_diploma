from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    email = forms.CharField(label='Почта')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'passs'}))
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
