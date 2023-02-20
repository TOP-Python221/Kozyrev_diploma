from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=500)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    time_creat = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Формирования динамических ссылок на посты"""
        return reverse('post', kwargs={'post_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name

    #
    def get_absolute_url(self):
        """Формирования динамических ссылок на посты"""
        return reverse('category', kwargs={'cat_id': self.pk})

#
#
# class Work(models.Model):
#     pass
