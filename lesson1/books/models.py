
from django.db import models

# Create your models here.


class Book(models.Model):
    title=models.CharField(max_length=200)
    uname=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    isbn=models.CharField(max_length=12)



