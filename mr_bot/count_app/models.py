from django.db import models

# Create your models here.


class Count(models.Model):
    count = models.IntegerField(verbose_name='counter', default=0)

    def __str__(self):
        return self.count
