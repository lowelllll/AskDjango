# dojo/models.py
from django import forms
from django.db import models

def min_length_3_validator(value): # 유효값 검사 함수 생성.
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.')

class Post(models.Model):
    title = models.CharField(max_length=100,validators=[min_length_3_validator])
    content = models.TextField()
    ip = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
