from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    content = models.TextField(max_length=500)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    salary = models.IntegerField(null=True)
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
