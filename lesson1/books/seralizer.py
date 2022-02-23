
from .models import Book
from rest_framework import serializers


class BookSeralizer(serializers.ModelSerializer):
  class Meta:
    model=Book
    fields=['title','uname','author','isbn']
