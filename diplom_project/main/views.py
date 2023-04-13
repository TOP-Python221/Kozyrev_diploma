import json

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

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


class ShowPost(LoginRequiredMixin, DataMixin, DetailView):
    """Представление выбранных постов"""
    model = Posts
    template_name = 'main/index/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        post = Posts.objects.get(id=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(title=context['post'],
                                       profile=Profile.objects.get(id=post.user_id),
                                       response=post.response.all())
        return context | c_def


def response(request, pk):
    post = Posts.objects.get(pk=pk)
    profiles = Profile.objects.all()
    response_post = post.response.all()
    is_response = False
    for r in response_post:
        if r == request.user:
            is_response = True
            break
    if not is_response:
        post.response.add(request.user)
    return redirect('post', post.pk)


class Addpage(LoginRequiredMixin, DataMixin, CreateView):
    """Представление добавления постов"""
    form_class = AddPostForm
    template_name = 'main/index/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(title='Добавить объявление')
        return context | c_def

    def form_valid(self, form):
        posts = form.save(commit=False)
        posts.user = Profile.objects.get(id=self.request.user.id)
        posts.save()
        return redirect('home')


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
    """Представление профилей пользователей"""
    model = Profile
    template_name = 'main/index/profile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'profile'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(title='Профиль')
        return context | c_def


class UpDateProfileView(DataMixin, UpdateView):
    """Представление для редактирования профиля"""
    model = Profile
    form_class = UpDateProfileForm
    template_name = 'main/index/update_profile.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(title='Редактирование профиля')
        return context | c_def

    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     with transaction.atomic():
    #         if form.is_valid():
    #             form.save()
    #         else:
    #             return self.render_to_response(context)
    #     return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile_user', kwargs={'slug': self.object.slug})


class AllChat(DataMixin, ListView):
    model = Message
    template_name = 'main/index/message.html'
    context_object_name = 'Chats'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(title='Сообщения')
        return context | c_def

    def get_queryset(self):
        message = Message.objects.filter(recipient_id=self.request.user.id).order_by('-created')[:1]
        from_message = Message.objects.filter(sender_id=self.request.user.id).order_by('-created')[:1]
        return message | from_message


class Chat(DataMixin, CreateView, ListView):
    model = Message
    template_name = 'main/index/Chat.html'
    context_object_name = 'dialog'
    form_class = MessageForm

    def get_context_data(self, *, object_list=None, **kwargs):
        num_msg = Message.objects.filter(sender_id=Profile.objects.get(slug=self.kwargs['slug']),
                                         recipient_id=self.request.user.profile)
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(title='Сообщения',
                                       form=self.form_class,
                                       msg=self.get_queryset,
                                       profile=Profile.objects.get(slug=self.kwargs['slug']),
                                       num_msg=num_msg.count(),
                                       )
        return context | c_def

    def get_queryset(self):
        sender_msg = self.request.user.profile
        recipient_msg = Profile.objects.get(slug=self.kwargs['slug'])
        all_msg = Message.objects.all()
        from_to = []
        for m in all_msg:
            if m.sender == sender_msg and m.recipient == recipient_msg:
                from_to.append(m)
            elif m.sender == recipient_msg and m.recipient == sender_msg:
                from_to.append(m)
        return from_to

    def form_valid(self, form):
        form = MessageForm
        user = self.request.user.profile
        recipient = Profile.objects.get(slug=self.kwargs['slug'])

        if self.request.method == "POST":
            form = MessageForm(self.request.POST)
            if form.is_valid():
                chat_msg = form.save(commit=False)
                chat_msg.sender = user
                chat_msg.recipient = recipient
                chat_msg.save()
                return redirect('chat', recipient.slug)
        return form


def send_message(request, slug):
    data = json.loads(request.body)
    new_chat = data['msg']
    new_chat_message = Message.objects.create(message=new_chat,
                                              sender=request.user.profile,
                                              recipient=Profile.objects.get(slug=slug)
                                              )
    print(new_chat)
    return JsonResponse(new_chat_message.message, safe=False)


def received_message(request, slug):
    chats = Message.objects.filter(sender_id=Profile.objects.get(slug=slug),
                                   recipient_id=request.user.profile
                                   )
    arr = []
    for chat in chats:
        arr.append(chat.message)

    return JsonResponse(arr, safe=False)
