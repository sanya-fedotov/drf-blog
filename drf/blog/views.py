from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serialiazers import PostSerialiazers
from .models import Post, Tag
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
# Create your views here.

# class BlogViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerialiazers

#     @action(methods=['get'], detail=False)
#     def tags(self, request):
#         tags = Tag.objects.all()
#         return Response({'tags': [t.name for t in tags]})
    
class BlogAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialiazers
    permission_classes = (IsAuthenticatedOrReadOnly, )

class BlogAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialiazers
    permission_classes = (IsOwnerOrReadOnly, )

class BlogAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialiazers
    permission_classes = (IsAdminOrReadOnly, )