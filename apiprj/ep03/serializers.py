from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from .models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','content']


    def validate_title(self, title): # 특정 필드 유효성 검사
        if 'django' not in title:
            raise ValidationError('제목에 django를 꼭 포함시켜주세요!!.')
        return title


    def validate(self, data): # 전체 필드 유효성검사
        if len(data['title']) % 2 == 0 or len(data['content']) % 2 == 0:
            raise  ValidationError('글자갯수는  홀수로만 해주세용')
        return data


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['pk','username','email']