# blog/admin.py

from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe

# admin.site.register(Post) admin 사이트 등록

@admin.register(Post) # 데코레이터로 등록.
class PostAdmin(admin.ModelAdmin): # Custom Admin
    list_display = ['id','title','created_at']
    
    # admin 페이지에서 보일 필드를 커스텀하는 함수 (content의 글자 수를 반영)
    def content_size(self,post): # 해당 모델의 인스턴스 받음
        return mark_safe('<strong>{}글자</strong>'.format(len(post.content))) # html 태그를 출력(tag escape : 허용치 않은 코드 실행 방지)이 아닌, 적용하기 위해 mark_safe(이 태그는 안전하다) 함수 추가
    content_size.short_description = '글자수' # 필드명 수정 


# admin.site.register(Post,PostAdmin) register 함수로 등록.