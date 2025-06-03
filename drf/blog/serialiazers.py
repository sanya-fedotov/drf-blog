from rest_framework import serializers

from .models import Post, Tag

class PostSerialiazers(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = "__all__"

    # def create(self, validated_data):
    #     tags = validated_data.pop("tags", [])
    #     post = Post.objects.create(**validated_data)   
    #     post.tags.set(tags)
    #     return post

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.content = validated_data.get("title", instance.content)
    #     instance.tags = validated_data.get("title", instance.tags)
    #     instance.save()
    #     return instance
    

class TagSerialiazers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']