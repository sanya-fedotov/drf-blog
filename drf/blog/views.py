from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialiazers import PostSerialiazers
from .models import Post

# Create your views here.
class BlogAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialiazers

class BlogAPIView(APIView):
    def get(self, request):
        p = Post.objects.all()
        return Response({'posts': PostSerialiazers(p, many=True).data})
    
    def post(self, request):
        serializer = PostSerialiazers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        
        try:
            instance = Post.objects.get(pk=pk)
        except:
            return Response({"error": "Method PUT not allowed"})
        
        serializer = PostSerialiazers(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response({"message":f"Post{pk} deleted"})
        
        except:
            return Response({"error": "Post not found"})