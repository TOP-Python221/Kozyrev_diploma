from django.contrib.auth.models import User
from django import forms
from .models import *


class UserRegister(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['login', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }
