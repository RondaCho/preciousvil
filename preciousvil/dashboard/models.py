from django.db import models
from django.contrib import admin
from django.forms import ValidationError
from django.core.urlresolvers import reverse


def min_length_10_validators(value):
    if len(value) < 10:
        raise ValidationError('10글자 이상 입력해주세요.')


class House(models.Model):
    TYPE_CHOICES = (
        ('Perfect(192)', '192'),
        ('Charming(219)', '219'),
        ('Elegant(238)', '238'),
        ('Luxury(267)', '267'),
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    address = models.CharField(max_length=3, unique=True, help_text='A-1과 같은 형식으로 입력해주세요')
    total_land = models.IntegerField()
    your_land = models.IntegerField()
    price = models.IntegerField()
    house_tag_set = models.ManyToManyField('House_Tag', blank=True)

    def __str__(self):
        return self.address


class House_Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Progress(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )

    title = models.CharField(max_length=100, verbose_name='제목',
                             validators=[min_length_10_validators],
                             help_text='본 포스팅의 제목을 입력해주세요.')
    content = models.TextField(verbose_name='상세 내용')
    photo = models.ImageField(upload_to='progress/%Y/%m/%d')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('welcome:progress_detail', args=[self.id])


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

