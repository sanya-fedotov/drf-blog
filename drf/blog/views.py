from rest_framework import generics
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serialiazers import PostSerialiazers
from .models import Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostFilter

class BlogAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialiazers
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter

class BlogAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialiazers
    permission_classes = (IsOwnerOrReadOnly, )

class BlogAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialiazers
    permission_classes = (IsAdminOrReadOnly, )