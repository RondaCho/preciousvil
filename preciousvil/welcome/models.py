from django.db import models
from django.forms import ValidationError


def min_length_10_validators(value):
    if len(value) < 10:
        raise ValidationError('10글자 이상 입력해주세요.')


class HeroImage(models.Model):
    name = models.CharField(max_length=20, default='히어로이미지')
    photo = models.ImageField(upload_to='hero_image/%Y/%m/%d')
    title = models.CharField(max_length=50, default='PRECIOUS')
    content = models.CharField(max_length=100, default='서해안을 바라보는 명품 단독형 주거단지')