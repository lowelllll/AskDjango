# blog/views.py

from django.shortcuts import render
from .models import Post

def post_list(request): # render
    qs = Post.objects.all()

    q = request.GET.get('q','')
    
    if q:
        qs = qs.filter(title__icontains=q) # 검색기능 구현

    return render(request,'blog/post_list.html',{
        'post_list':qs,
        'q':q
    })