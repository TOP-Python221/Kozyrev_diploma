from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main/index/main.html')


def help_me(request):
    return render(request, 'main/index/help.html')
