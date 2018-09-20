from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from .models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','content']


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['pk','username','email']