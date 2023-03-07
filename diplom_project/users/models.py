from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class UserMain(AbstractUser):
    bio = models.CharField(max_length=160, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.username)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Формирования динамических ссылок на посты"""
        return reverse('profile_user', kwargs={'slug': self.slug})
