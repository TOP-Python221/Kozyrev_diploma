from django.contrib import admin
from .models import *


# Register your models here.


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_creat', 'photo', 'is_published')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Posts, PostsAdmin)
admin.site.register(Category, CategoryAdmin)
