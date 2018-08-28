# blog/models.py

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100,
        choices= (
            ('제목1','제목1 레이블'), # ('저장될 값', 'UI에 보여질 레이블')
            ('제목2','제목2 레이블'),
            ('제목3','제목3 레이블'),
        )
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add 해당 레코드가 최초 저장될 때 자동 저장.
    updated_at = models.DateTimeField(auto_now = True) # auto_now 해당 레코드가 저장될 때 마다 자동 저장