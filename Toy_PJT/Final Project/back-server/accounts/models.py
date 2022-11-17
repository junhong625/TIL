from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
class Membership(models.Model):
    payment_date    = models.DateTimeField(blank=True)
    price           = models.IntegerField(blank=True)
    expiration_date = models.DateField(blank=True)
    status          = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.payment_date and not self.expiration_date and self.status == 1:
            self.expiration_date = self.payment_date.date() + datetime.timedelta(days=364)
        super(Membership, self).save(*args, **kwargs)

class Survey_category(models.Model):
    category_name = models.CharField(max_length=20)

class User(AbstractUser):
    # 추가 필드
    style       = models.ManyToManyField(Survey_category, related_name="same_style_user", through='Survey')
    membership  = models.ForeignKey(Membership, on_delete=models.CASCADE, null=True)
    nickname    = models.CharField(max_length=10)
    def __str__(self):
        return self.nickname

# User와 Survey_category의 중계 필드
class Survey(models.Model):
    survey_category = models.ForeignKey(Survey_category, on_delete=models.CASCADE)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    
    like = 0
    normal = 1
    hate = 2
    choices = (
        (like, 'like'),
        (normal, 'normal'),
        (hate, 'hate'),
    )
    like_or_hate = models.IntegerField(default=1, choices=choices)