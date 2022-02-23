from django.shortcuts import render

from books.models import Book
from .seralizer import BookSeralizer
from rest_framework.generics import ListAPIView
 
# Create your views here.


class BookApiView(ListAPIView):
    queryset=Book.objects.all()
    serializer_class = BookSeralizer
    