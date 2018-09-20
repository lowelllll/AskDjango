from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(ip=self.request.META['REMOTE_ADDR'])
        # 저장할 때, validation 검사 후 기존 serializer 데이터(message)와 kwargs 딕셔너리(현재 아이피 주소)를 합쳐서 저><장