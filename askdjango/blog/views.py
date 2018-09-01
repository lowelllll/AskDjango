# blog/views.py
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from .models import Post

def post_list(request): # Post 리스트 보기 구현.
    qs = Post.objects.all()

    q = request.GET.get('q','')
    
    if q:
        qs = qs.filter(title__icontains=q) # 검색기능 구현

    return render(request,'blog/post_list.html',{
        'post_list':qs,
        'q':q
    })

def post_detail(request, id): # Post 상세보기 구현
    # try:
    #     post = Post.objects.get(id=id) 해당 id의 포스트가 없을 시
    # except:
    #     raise Http404  404 error 발생
    
    post = get_object_or_404(Post,id=id) # 위의 코드와 동일 추천!

    return render(request, 'blog/post_detail.html', {
        'post':post
    })