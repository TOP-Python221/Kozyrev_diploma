from .models import *

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Добавить объявление', 'url_name': 'add_post'},
        {'title': 'Помощь', 'url_name': 'help'},
        {'tile': 'Поиск', 'url_name': 'search'},
        ]


class DataMixin:
    """Едино-образное представление контекстом"""

    paginate_by = 4  # переменная для отображения кол постов на одной странице

    def get_using_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
