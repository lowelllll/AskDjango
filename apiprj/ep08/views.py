from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorUpdateOrReaonly


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthorUpdateOrReaonly,
        # IsAuthenticated, # 인증된 요청에 한해서 뷰 호출을 허용함.
        # IsAuthenticatedOrReadOnly 비인증 요청에게는 읽기 권한만 허용.
    ]

    def perform_create(self, serializer):
        serializer.save(
            ip=self.request.META['REMOTE_ADDR'],
            author=self.request.user
        )
        # 저장할 때, validation 검사 후 기존 serializer 데이터(message)와 kwargs 딕셔너리(현재 아이피 주소)를 합쳐서 저><장