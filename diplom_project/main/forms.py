from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'salary', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form_input'}),
            'content': forms.Textarea(attrs={'class': 'form_content'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Количество символом должно быть не больше 200')
        return title
