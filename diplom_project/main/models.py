from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    content = models.TextField(max_length=500)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    salary = models.IntegerField(max_length=300)
    time_creat = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Формирования динамических ссылок на посты"""
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        ordering = ['-time_creat', 'title']


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name

    #
    def get_absolute_url(self):
        """Формирования динамических ссылок на посты"""
        return reverse('category', kwargs={'cat_id': self.id})

#
#
# class Work(models.Model):
#     pass
