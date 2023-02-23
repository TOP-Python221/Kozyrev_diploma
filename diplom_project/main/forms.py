from django.contrib.auth.models import User
from django import forms
from .models import *


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=300, label='Заголовок',
                            widget=forms.TextInput(attrs={'class': 'form_input'}))
    slug = forms.SlugField(max_length=300, label='URL-адрес',
                           widget=forms.TextInput(attrs={'class': 'form_url'}))
    content = forms.CharField(max_length=600, label='Контент',
                              widget=forms.TextInput(attrs={'class': 'form_content'}))
    is_published = forms.BooleanField(label='Публикация')
    salary = forms.IntegerField(label='Зарплата')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),
                                 label='Категория',
                                 empty_label='Категория не выбрана')

    class Meta:
        model = Posts
        fields = ['title', 'content', 'photo']
        widgets = {
            'password': forms.PasswordInput(),
        }
