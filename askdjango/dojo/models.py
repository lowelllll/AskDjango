# dojo/models.py

from django import forms
from django.core.validators import MinLengthValidator
from django.db import models

def min_length_3_validator(value): # 유효값 검사 함수 생성.
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.')

class Post(models.Model):
    title = models.CharField(max_length=100,validators=[min_length_3_validator])
    content = models.TextField()
    user_agent = models.CharField(max_length=200) # 브라우저 정보
    ip = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class GameUser(models.Model): # form 유효성 검사를 위한 model
    server_name = models.CharField(max_length=10, choices=(
        ('A','A 서버'),
        ('B', 'B 서버'),
        ('C', 'C 서버'),
    ))
    username = models.CharField(max_length=20, validators=[MinLengthValidator(3)]) # 유저네임은 최소 3글자 이상이여야하는 validator를 설정.

    class  Meta:
        unique_together = [
            ('server_name','username') # 두 필드가 합해 unique여야함. ex) A 서버 , 이예진 B 서버 , 이예진은 가능하나 A 서버에 동일한 유저네임이 있으면 unique하지 않다.
        ]