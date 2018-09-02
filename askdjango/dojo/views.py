# dojo/views.py

import os
from django.conf import settings
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def post_new(request):
    if request.method == 'POST': # django 스타일 구현
        form = PostForm(request.POST,request.FILES)
        if form.is_valid(): # 유효성 검사
            # 방법 1)
            """
            post = Post()
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            """

            # 방법 2)
            """
            post = Post(title = form.cleaned_data['title'],content = form.cleaned_data['content'])
            post.save()
            """

            # 방법 3)
            """
            post = Post.objects.create(title = form.cleaned_date['title'],content = form.cleaned_date['content'])
            """
            # 방법 4)
            """
            post = Post.objects.create(**form.cleaned_data) # 언팩킹으로 저장하는 방법
            """
            post = form.save()
            return redirect('/dojo/')
    else:
        form = PostForm()
    return render(request,'dojo/post_form.html',{
        'form':form
    })

def mysum(request,numbers):
    # numbers = "1/2/3/4/5.../10"
    # result = sum(map(int,numbers.splite("/"))
    result = sum(map(lambda s:int(s or 0),numbers.split("/"))) # s가 int 타입이 아닐 경우 false -> 0으로 치환 (빈문자 치환)
    return HttpResponse(result)


def hello(request,name,age):
    return HttpResponse("안녕하세요.{}.{}살이시네요.".format(name,age))


def post_list1(request):
    name = "예진";
    return HttpResponse('''
        <h1>Askdjango</h2>
        <p>{name}</p>
    '''.format(name=name))


def post_list2(request): # Json response
    return JsonResponse({
        'message':['파이썬','안녕'],
    },json_dumps_params={'ensure_ascii':False})


def excel_download(request): # Excel Download
    filepath = os.path.join(settings.BASE_DIR,'sample_excel_denmark.xlsx')
    # BASE_DIR 현재 최상위 디렉토리 + 파일 이름
    
    # filepath = r'C:\Users\lowel\OneDrive\문서\GitHub\AskDjango\askdjango\'
    filename = os.path.basename(filepath)

    with open(filepath,'rb') as f:
        response = HttpResponse(f,content_type='application/vnd.ms-excel') # excel download
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response

