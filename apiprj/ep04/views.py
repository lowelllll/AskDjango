from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet,ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post
from .serializer import PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # viewset에 custom API구현

    # ep04/post/public_list => public_list()함수 호출 post-public-list
    @action(detail=False)
    def public_list(self,request):
        qs = self.queryset.filter(is_public=True)
        serializer = self.get_serializer(qs,many=True)
        return Response([])


    # ep04/post/10/set_public => set_public()함수 호출 post-set-public
    @action(methods=['update'],detail=True) # 수정해보자
    def set_public(self, request, pk):
        instance = self.get_object() # viewset에서 이미 만들어져있음.
        instance.is_public = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)





post_list = PostViewSet.as_view({ # /post/
    'get':'list', # get 메소드를 받으면 list함수를 호출하겠다.
    'post':'create',
})

post_detail = PostViewSet.as_view({ # /post/10/
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update', # 부분적 수정
    'delete':'destory', # 삭제
})

# 이 메소드-함수 연결을 라우터가 편리하게 해줌!!