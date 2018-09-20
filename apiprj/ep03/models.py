from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100) # ,validators=[] 모델에다 정의하는 것이 좋음.
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)