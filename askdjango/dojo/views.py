# dojo/views.py

from django.http import HttpResponse
from django.shortcuts import render

def mysum(request,x,y):
    return HttpResponse(int(x)+int(y))