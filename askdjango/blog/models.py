# blog/models.py

import re
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.forms import ValidationError

def lnglat_validator(value): # 유효성 검사하는 validator
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$',value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    STATUS_CHOICES = (
        ('d','Draft'),
        ('p','Published'),
        ('w','Withdrawn')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100,
        # choices= (
        #   ('제목1','제목1 레이블'), # ('저장될 값', 'UI에 보여질 레이블')
        #   ('제목2','제목2 레이블'),
        #    ('제목3','제목3 레이블'),
        # )
    )
    content = models.TextField()
    photo = models.ImageField(blank=True)
    tags = models.CharField(max_length=100,blank=True)
    lnglat = models.CharField(max_length=50, blank=True,validators=[lnglat_validator],help_text='경도/위도 포맷으로 입력')
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag',blank=True) # 모델이 뒤에 있기 때문에 문자열로 정의.
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add 해당 레코드가 최초 저장될 때 자동 저장.
    updated_at = models.DateTimeField(auto_now = True) # auto_now 해당 레코드가 저장될 때 마다 자동 저장

    class Meta: # 기본 정렬 옵션 추가
        ordering = ['-id']
        
    def __str__(self):
        return self.title

    def get_absolute_url(self): # reverse를 위한 함수! 강추 기능
        return reverse('blog:post_detail',args=[self.id])


class Comment(models.Model):
    post = models.ForeignKey(Post) # 1:N 관계 실제 필드 이름 post_id
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50,unique=True) # N:N 관계

    def __str__(self):
        return self.name