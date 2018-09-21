from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField()
    photo = models.ImageField()

