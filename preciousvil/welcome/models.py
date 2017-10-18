from django import forms
from django.db import models
from django.forms import ValidationError
from django.core.validators import RegexValidator


def min_length_10_validators(value):
    if len(value) < 10:
        raise ValidationError('10글자 이상 입력해주세요.')


class HeroImage(models.Model):
    name = models.CharField(max_length=20, default='히어로이미지')
    photo = models.ImageField(upload_to='hero_image/%Y/%m/%d')
    title = models.CharField(max_length=50, default='PRECIOUS')
    content = models.CharField(max_length=100, default='서해안을 바라보는 명품 단독형 주거단지')

'''
    type = models.ForeignKey("dashboard.House", verbose_name="type", related_name="type1")
    address = models.ForeignKey("dashboard.House", verbose_name="address", related_name="address1")
    total_land = models.ForeignKey("dashboard.House", verbose_name="total_land", related_name="total_land1")
    your_land = models.ForeignKey("dashboard.House", verbose_name="your_land", related_name="your_land1")
    price = models.ForeignKey("dashboard.House", verbose_name="price", related_name="price1")
    house_tag_set = models.ForeignKey('dashboard.House', verbose_name="house_tag_set", related_name="house_tag_set1")

    def __str__(self):
        return self.address1
'''

class Reservation(models.Model):

    phone_regex = RegexValidator(regex=r'^\d{8,15}$', message="8자에서 15자의 숫자를 빈칸없이 입력하여 주세요.")

    STATUS_CHOICES = (
        ('r', '상담예약대기중'),
        ('v', '찾아가는상담예약중'),
        ('s', '현장방문상담예약중'),
        ('c', '상담완료'),
    )

    TYPE_CHOICES = (
        ('1', 'A 타입(192)'),
        ('2', 'B 타입(219)'),
        ('3', 'C 타입(238)'),
        ('4', 'D 타입(267)'),
    )

    name = models.CharField(max_length=10, verbose_name='예약자',help_text='실명 혹은 닉네임을 입력해주세요')
    corporate = models.CharField(max_length=30, verbose_name='법인명',help_text='(선택항목)법인 구매 상담을 위해 필요한 항목입니다,', blank=True)
    phone_number = models.CharField(validators=[phone_regex],max_length=15,verbose_name='연락처', help_text='연락처를 빈칸없는 형태로 입력해주세요. 글 작성 시 입력하신 번호가 비밀번호로 사용됩니다. ※분양 정보 제공 및 상담 이외의 목적으로 사용되지 않습니다.')
    email = models.EmailField(verbose_name='이메일주소', help_text='분양 정보 제공 및 상담 이외의 목적으로 사용되지 않습니다.')
    address = models.CharField(max_length=100, verbose_name='주소지', blank=True,
                               help_text='(선택항목)주소지를 적어주시면 찾아가는 분양상담 예약에 도움을 받으실 수 있습니다.')
    type_set = models.ManyToManyField('Type', verbose_name='관심타입', blank=True, help_text='(선택항목/다수선택가능)관심있는 타입을 작성해주세요')
    date = models.DateField(verbose_name='상담예약일', help_text='2018-01-03 와 같은 형식으로 입력해주세요. '
                                                                '더 많은 날짜는 하단의 추가사항에 입력해주세요.', default='1111-11-11')
    detail = models.TextField(verbose_name='추가사항', blank=True, help_text='(선택항목)문의사항 및 상담 가능 날짜를 적어주세요.')
    detail_admin = models.TextField(verbose_name='예약 손님에 대한 정보를 입력하는 란', blank='True')
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='r')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name