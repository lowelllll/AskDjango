from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='ep08_post_set') # user.ep08_post_set
    message = models.CharField(max_length=128)
    ip = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

