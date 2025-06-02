from rest_framework import serializers

from .models import Post, Tag

class PostSerialiazers(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ['id', 'title', 'content', 'tags', 'created_at']

class TagSerialiazers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fielfs = ['id', 'name']