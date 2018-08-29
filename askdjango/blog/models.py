# blog/models.py

import re
from django.db import models
from django.forms import ValidationError

def lnglat_validator(value): # 유효성 검사하는 validator
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$',value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    author = models.CharField(max_length=20) # blank,null이 False인 필수 필드
    title = models.CharField(max_length=100,
        # choices= (
        #   ('제목1','제목1 레이블'), # ('저장될 값', 'UI에 보여질 레이블')
        #   ('제목2','제목2 레이블'),
        #    ('제목3','제목3 레이블'),
        # )
    )
    content = models.TextField()
    lnglat = models.CharField(max_length=50, blank=True,validators=[lnglat_validator],help_text='경도/위도 포맷으로 입력')
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add 해당 레코드가 최초 저장될 때 자동 저장.
    updated_at = models.DateTimeField(auto_now = True) # auto_now 해당 레코드가 저장될 때 마다 자동 저장