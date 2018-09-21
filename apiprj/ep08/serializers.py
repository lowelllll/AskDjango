from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Post


class PostSerializer(ModelSerializer):
    author_username = ReadOnlyField(source='author.username') # custom field

    class Meta:
        model = Post
        fields = ('message','author_username')
