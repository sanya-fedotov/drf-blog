from django.shortcuts import render
from rest_framework import generics
from .serialiazers import PostSerialiazers
from .models import Post

# Create your views here.
class BlogAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialiazers