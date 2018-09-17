# accounts/models.py

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)  # 좋은 방법
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
