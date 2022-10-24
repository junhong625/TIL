from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    image = models.ImageField(blank=True)
    win_cnt = models.BigIntegerField()
    lose_cnt = models.BigIntegerField()
    kill_cnt = models.BigIntegerField()
    pass