from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer, UserSerializer


class PostListAPIView(APIView):
    def get(self, request): # post list 반환
        qs = Post.objects.all()
        serializer = PostSerializer(qs,many=True)
        return Response(serializer.data)

    def post(self, request): # post 생성
        serializer = PostSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save() # modelform 처럼 작동
            return Response(serializer.data)
        return Response(serializer.errors)

# /post/10
class PostDetailAPIView(APIView): # APIView에선 이미 csrf_token 가 해제되어있음.
    def get_object(self, pk):
        return get_object_or_404(Post,pk=pk)


    def get(self, reqeust, pk):
        post = self.get_object(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


    def put(self, request, pk):
        post = get_object_or_404(Post,pk=pk)
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=204)


# 믹스인 클래스를 사용해서 더 쉽게 API뷰 만들기

#rest_framework/generics/ListCreateAPIView 와 동일
class PostListUseMixinView(mixins.ListModelMixin, mixins.CreateModelMixin,
                              generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

#rest_framework/generics/RetrieveUpdateDestoryAPIView 와 동일 (fetch)
class PostDetailUseMixinView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


# 위의 코드를 이미 만들어져있는 generics/ 안의 클래스를 상속받아 더 더 쉽게 구현하기
class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# 위 두 클래스의 코드가 같은데 ... 이걸 묶을 수 없을까?! ->viewset
# viewset 2개의 뷰를 만들어주는 헬퍼클래스

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# user_list = UserViewSet.as_view({
#     'get':'list', # 호출될 메소드와 호출할 함수를 지정.
# })
#
# user_detail = UserViewSet.as_view({
#     'get':'retrieve',
# })


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
