from rest_framework.serializers import ModelSerializer,ReadOnlyField
from api.models import Post


class PostSerializer(ModelSerializer):
    author_username = ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id','author_username','message','photo']
