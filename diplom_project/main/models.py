from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Account(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.login

# class Message(models.Model):
#     message = models.CharField(max_length=1000)
#     # login_user_to = models.ForeignKey(Account, on_delete=models.CASCADE)
#
#     login_user_from = models.ManyToManyField(Account)
#     # date_time
#     # is_read
#     pass
#
#
# class Work(models.Model):
#     pass
