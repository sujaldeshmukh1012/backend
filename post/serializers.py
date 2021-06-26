from rest_framework import serializers
from .models import IpModel, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'posted', 'tags',
                  'categories', 'author', 'picture', 'likes', 'views', 'isvisible')


class IpModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpModel
        fields = ('id', 'ip', 'time')
