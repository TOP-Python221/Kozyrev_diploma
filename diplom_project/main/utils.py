from .models import *

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Добавить объявление', 'url_name': 'add_post'},
        {'title': 'Помощь', 'url_name': 'help'},
        {'tile': 'Поиск', 'url_name': 'search'},
        {'title': 'Регистрация', 'url_name': 'register'},
        {'title': 'Вход', 'url_name': 'sing_up'}
        ]


class DataMixin:
    def get_using_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
