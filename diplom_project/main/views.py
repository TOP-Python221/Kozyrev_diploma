from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.


menu = ['Главная', 'Помощь', 'Регистрация', 'Войти']


def index(request):
    return render(request, 'main/index/main.html', {'menu': menu, 'title': 'Главная страница'})


def help_me(request):
    return render(request, 'main/index/help.html')


def sing_up(request):
    return render(request, 'main/index/sing_up.html')


def User_All(request):
    users = Account.objects.all()
    return render(request, 'main/index/users.html', {'users': users})


def register_users(request):
    if request.method == 'POST':
        reg_user = UserRegister(request.POST)
        if reg_user.is_valid():
            reg_user.save()
            return redirect('home')
    else:
        reg_user = UserRegister()

    return render(request, 'main/index/register.html', {'reg_user': reg_user})
