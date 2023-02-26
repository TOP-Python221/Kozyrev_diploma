from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import *
from .utils import *


# Create your views here.
class MainPost(DataMixin, ListView):
    """Представление главной страницы и всех постов"""
    model = Posts
    template_name = 'main/index/main.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))


class CategoryPost(DataMixin, ListView):
    """Представление постов по категориям"""
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
    """Представление выбранных постов"""
    model = Posts
    template_name = 'main/index/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class Addpage(LoginRequiredMixin, DataMixin, CreateView):
    """Представление добавления постов"""
    form_class = AddPostForm
    template_name = 'main/index/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('log')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(title='Добавить объявление')
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUsers(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/index/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'main/index/sing_up.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(title='Вход')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('log')


def help_me(request):
    context = {'menu': menu,
               'title': 'Помощь'}
    return render(request, 'main/index/help.html', context=context)
