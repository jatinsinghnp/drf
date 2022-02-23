from operator import mod
from statistics import mode
from django.db import models

# Create your models here.


class Blog(models.Model):
    author = models.CharField(max_length=200)
    titile = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author
