from django.contrib import admin
from .models import Account


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('Login', 'Password', 'Email')


admin.site.register(Account)
