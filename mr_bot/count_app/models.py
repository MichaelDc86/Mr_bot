from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class BotUser(User):

    def __str__(self):
        return self.username


class Count(models.Model):
    count = models.IntegerField(verbose_name='counter', default=0)
    usr = models.OneToOneField(BotUser, verbose_name='user name', on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return str(self.count)
