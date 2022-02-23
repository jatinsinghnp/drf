import imp
from django.shortcuts import render
from .serilizer import BlogSerializers
from rest_framework import generics
from blog.models import Blog

# Create your views here.


class BlogApiView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers


class BlogDetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
