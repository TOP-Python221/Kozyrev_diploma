from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main/index/base.html')


def help_me(request):
    return render(request, 'main/index/help.html')


def sing_up(request):
    return render(request, 'main/index/sing_up.html')
