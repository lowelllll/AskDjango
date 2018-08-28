# blog/admin.py

from django.contrib import admin
from .models import Post

admin.site.register(Post) # admin 사이트 등록
