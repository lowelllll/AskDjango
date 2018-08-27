# dojo/views.py

from django.http import HttpResponse
from django.shortcuts import render

def mysum(request,numbers):
    # numbers = "1/2/3/4/5.../10"
    # result = sum(map(int,numbers.splite("/"))
    result = sum(map(lambda s:int(s or 0),numbers.split("/"))) # s가 int 타입이 아닐 경우 false -> 0으로 치환 (빈문자 치환)
    return HttpResponse(result)


def hello(request,name,age):
    return HttpResponse("안녕하세요.{}.{}살이시네요.".format(name,age))