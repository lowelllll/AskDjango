# dojo/views.py

import os
from django.conf import settings
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from .forms import PostForm
from .models import Post

# def post_detail(request,id):
#     post = get_object_or_404(Post,id=id)
#     return render(request,'dojo/post_detail.html',{
#         'post':post
#     })

# def generate_view_fn(model):
#     def view_fn(request,id):
#         instance = get_object_or_404(model,id=id)
#         instance_name = model._meta.model_name # 모델의 이름을 구함
#         template_name = '{}/{}_detail.html'.format(model._meta.app_label, instance_name) # dojo/post_detail.html
#         return render(request,template_name,{
#             instance_name:instance
#         })
#     return view_fn
#
# post_detail = generate_view_fn(Post) # post_detail 뷰 함수 구현.

# class DetailView(object):
#     """
#     이전 FBV를 CBV 버전으로 컨셉을 구현. 같은 동작을 수행함.
#     """
#     def __init__(self,model):
#         self.model = model
#
#     def get_object(self, *args, **kwargs):
#         return get_object_or_404(self.model, id=kwargs['id'])
#
#     def get_template_name(self):
#         return '{}/{}_detail.html'.format(self.model._meta.app_label, self.model._meta.model_name)
#
#     def dispatch(self, request, *args, **kwargs):
#         return render(request, self.get_template_name(), {
#             self.model._meta.model_name:self.get_object(*args, **kwargs),
#         })
#
#     @classmethod
#     def as_view(cls,model):
#         def view(request, *args, **kwargs):
#             self = cls(model)
#             return self.dispatch(request, *args, **kwargs)
#         return view
#
# post_detail = DetailView.as_view(Post)

post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id') # url에서 id->pk로 변경하면 pk_url_kwarg 설정 안해도 댐


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
            post = form.save(commit=False) # save를 연기
            post.ip  = request.META['REMOTE_ADDR'] # 현재 IP 추가
            post.save() # save

            return redirect('/dojo/')
    else:
        form = PostForm()
    return render(request,'dojo/post_form.html',{
        'form':form
    })


def post_edit(request,id): # 수정
    post = get_object_or_404(Post,id=id)

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip  = request.META['REMOTE_ADDR']
            post.save()

            return redirect('/dojo/')
    else:
        form = PostForm(instance=post)
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

