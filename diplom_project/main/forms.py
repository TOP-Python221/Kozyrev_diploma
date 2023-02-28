
from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'salary', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form_input'}),
            'content': forms.Textarea(attrs={'class': 'form_content'}),
        }
