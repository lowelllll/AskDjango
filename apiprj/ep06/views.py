from rest_framework.viewsets import ModelViewSet
from ep04.models import Post
from ep04.serializer import PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self): # 필터링
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qs = qs.filter(user=self.request.user) # 현재 로그인 되어있는 유저와 동일한지
        else:
            qs = qs.none() # empty result
        return qs
