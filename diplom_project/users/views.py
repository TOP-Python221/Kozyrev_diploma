from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import *
# По другому не как не хотел импортироваться
from main.utils import DataMixin


# Create your views here.

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/register.html'
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
    template_name = 'registration/login.html'
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


class Profile_User(LoginRequiredMixin, DataMixin, CreateView):
    form_class = UpDateProfile
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        # user_profile = UserMain.objects.get(user='user3')
        context = super().get_context_data(**kwargs)
        c_def = self.get_using_context(title='Профиль')
        return context | c_def

# class UpDateProfileView(DataMixin, ListView):
#     model = UserMain
#     template_name = 'registration/'
