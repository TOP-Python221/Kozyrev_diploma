from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

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
        c_def = self.get_using_context(title='Главная страница',

                                       )
        return context | c_def


class CategoryPost(DataMixin, ListView):
    """Представление постов по категориям"""
    model = Posts
    template_name = 'main/index/main.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(
            title='Категория - ' + str(context['posts'][0].cat),
            cat_selected=context['posts'][0].cat_id
        )
        return context | c_def

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
        return context | c_def


class Addpage(LoginRequiredMixin, DataMixin, CreateView):
    """Представление добавления постов"""
    form_class = AddPostForm
    template_name = 'main/index/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(title='Добавить объявление',
                                       )
        return context | c_def

    def form_valid(self, form):
        posts = form.save(commit=False)
        posts.user = Profile.objects.get(id=self.request.user.id)
        posts.save()
        return redirect('home')


def help_me(request):
    context = {'menu': menu,
               'title': 'Помощь'
               }
    return render(request, 'main/index/help.html', context=context)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/index/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(title='Регистрация')
        return context | c_def

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'main/index/login.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(title='Вход')
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class Profile_User(DataMixin, DetailView):
    model = Profile
    template_name = 'main/index//profile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'profile'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(title='Профиль'
                                       )
        return context | c_def
