from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # 추가 필드
    nickname = models.CharField(max_length=10)

    def __str__(self):
        return self.nickname
