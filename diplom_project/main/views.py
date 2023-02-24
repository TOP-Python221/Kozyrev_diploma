from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .models import *
from .forms import *

# Create your views here.


menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Добавить объявление', 'url_name': 'add_post'},
        {'title': 'Помощь', 'url_name': 'help'},
        {'tile': 'Поиск', 'url_name': 'search'},
        {'title': 'Регистрация', 'url_name': 'register'},
        {'title': 'Вход', 'url_name': 'sing_up'}
        ]


def index(request):
    posts = Posts.objects.all()
    context = {'posts': posts,
               'menu': menu,
               'title': 'Главная страница',
               'cat_selected': 0
               }

    return render(request, 'main/index/main.html', context=context)


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = AddPostForm()
    context = {'menu': menu,
               'title': '123обеление',
               'form': form}
    return render(request, 'main/index/addpage.html', context=context)


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


def show_post(request, post_slug):
    post = get_object_or_404(Posts, slug=post_slug)
    context = {'posts': post,
               'menu': menu,
               'title': post.title,
               'cat_selected': post.slug,
               }
    return render(request, 'main/index/post.html', context=context)


def show_category(request, cat_id):
    posts = Posts.objects.filter(cat_id=cat_id)
    context = {'posts': posts,
               'menu': menu,
               'title': '!!!!!!21212',
               'cat_selected': cat_id,
               }
    return render(request, 'main/index/main.html', context=context)
