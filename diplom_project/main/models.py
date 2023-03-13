from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.views import LoginView
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone

from django.views.generic import CreateView
from pytils.translit import slugify


# Create your models here.
# class UserMain(AbstractUser):
#     bio = models.CharField(max_length=160, null=True, blank=True)
#     birthday = models.DateField(null=True, blank=True)
#     slug = models.SlugField(unique=True)
#
#     def __str__(self):
#         return self.username
#
#     def save(self, *args, **kwargs):
#         self.slug = self.slug or slugify(self.username)
#         super().save(*args, **kwargs)
#
#     def get_absolute_url(self):
#         """Формирования динамических ссылок на посты"""
#         return reverse('profile_user', kwargs={'slug': self.slug})

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    avatar = models.ImageField(default='2.jpeg', upload_to='profile_images')
    email = models.EmailField(blank=True)
    birthday = models.DateField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def get_absolute_url(self):
        """Формирования динамических ссылок на посты"""
        return reverse('user', kwargs={'slug': self.slug})

    def __str__(self):
        return self.user.username


class Posts(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    content = models.TextField(max_length=500)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    salary = models.IntegerField(null=True)
    time_creat = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Формирования динамических ссылок на посты"""
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        ordering = ['-time_creat', 'title']
        # КОММЕНТАРИЙ: не будет транслироваться в SQL код
        # managed = False


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Формирования динамических ссылок на посты"""
        return reverse('category', kwargs={'cat_slug': self.slug})

# ИСПОЛЬЗОВАТЬ: пример привязки сообщений к пользователям

# class User(models.Model):
#     name = models.CharField(max_length=15)

# class Message(models.Model):
#     text = models.TextField()
#     user_from = models.ForeignKey(User, models.CASCADE)
#     user_to = models.ForeignKey(User, models.CASCADE)

# u1 = User()

# все сообщения пользователя: отправленные и полученные
# u1.message_set_all()

# отправленные сообщения пользователя
# u1.message_set.filter(user_from_id=u1.id)

# полученные сообщения пользователя
# u1.message_set.filter(user_to_id=u1.id)
