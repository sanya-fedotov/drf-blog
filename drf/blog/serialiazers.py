from rest_framework import serializers

from .models import Post, Tag

class PostSerialiazers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post 
        fields = "__all__"



class TagSerialiazers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']