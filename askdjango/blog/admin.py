# blog/admin.py

from django.contrib import admin
from .models import Post

# admin.site.register(Post) admin 사이트 등록

@admin.register(Post) # 데코레이터로 등록.
class PostAdmin(admin.ModelAdmin): # Custom Admin
    list_display = ['id','title','created_at']

# admin.site.register(Post,PostAdmin) register 함수로 등록.