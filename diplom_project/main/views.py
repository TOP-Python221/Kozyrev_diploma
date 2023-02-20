from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import *
from .forms import *

# Create your views here.


menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Помощь', 'url_name': 'help'},
        {'tile': 'Поиск', 'url_name': 'search'},
        {'title': 'Регистрация', 'url_name': 'register'},
        {'title': 'Вход', 'url_name': 'sing_up'},
        ]


def index(request):
    posts = Posts.objects.all()
    cats = Category.objects.all()
    context = {'posts': posts,
               'cats': cats,
               'menu': menu,
               'title': 'Главная страница',
               'cat_selected': 0
               }

    return render(request, 'main/index/main.html', context=context)


def help_me(request):
    context = {'menu': menu,
               'title': 'Помощь'}
    return render(request, 'main/index/help.html', context=context)


def sing_up(request):
    context = {'menu': menu,
               'title': 'Вход'}
    return render(request, 'main/index/help.html', context=context)


def register_users(request):
    context = {'menu': menu,
               'title': 'Регистрация'}
    return render(request, 'main/index/help.html', context=context)


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def show_category(request, cat_id):
    posts = Posts.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    context = {'posts': posts,
               'cats': cats,
               'menu': menu,
               'title': 'Главная страница',
               'cat_selected': cat_id,
               }
    return render(request, 'main/index/main.html', context=context)
