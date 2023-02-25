from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import *
from .utils import *


# Create your views here.
class MainPost(DataMixin, ListView):
    paginate_by = 4
    model = Posts
    template_name = 'main/index/main.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))


class CategoryPost(DataMixin, ListView):
    paginate_by = 4
    model = Posts
    template_name = 'main/index/main.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(title='Категория - ' + str(context['posts'][0].cat),
                                       cat_selected=context['posts'][0].cat_id
                                       )
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Posts.objects.filter(cat__slug=self.kwargs['cat_slug'])


class ShowPost(DataMixin, DetailView):
    model = Posts
    template_name = 'main/index/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class Addpage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'main/index/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(title='Добавить объявление')
        return dict(list(context.items()) + list(c_def.items()))


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
