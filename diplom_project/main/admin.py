from django.contrib import admin
from .models import *


# Register your models here.


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_creat', 'photo', 'is_published')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Posts, PostsAdmin)
admin.site.register(Category, CategoryAdmin)
