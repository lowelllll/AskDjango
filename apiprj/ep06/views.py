from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from ep04.models import Post
from ep04.serializer import PostSerializer
from .pagination import PostPageNumberPagination


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPageNumberPagination # pagination 커스텀

    filter_backends = [SearchFilter]
    search_fields = ['title']  # title 필드에서 검색 수행  ep06/post/?search=쿡



    def get_queryset(self): # 쿼리셋 필터링
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qs = qs.filter(user=self.request.user) # 현재 로그인 되어있는 유저와 동일한지
        else:
            qs = qs.none() # empty result
        return qs

