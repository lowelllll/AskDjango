# dojo/views.py

import os
from django.conf import settings
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

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

