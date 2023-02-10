from django.db import models


# Create your models here.
class Account(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    # avatar


class Message(models.Model):
    # id
    # login_user_from
    # login_user_to
    # message
    # date_time
    # is_read
    pass


class Work(models.Model):
    pass
