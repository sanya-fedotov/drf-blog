from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialiazers import PostSerialiazers
from .models import Post

# Create your views here.

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerialiazers

# class BlogAPIList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerialiazers

# class BlogAPIUpdate(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerialiazers

# class BlogAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerialiazers