from django.db import models

# Create your models here.
class User(models.Model):
    GENDER_CHOICES = (
        ('M', '남성'),
        ('F', '여성'),
        ('O', '기타'),
    )
    user_id = models.CharField(max_length=32, unique=True,verbose_name='유저 아이디')
    user_pw = models.CharField(max_length=128,verbose_name='유저 비밀번호')
    user_name = models.CharField(max_length=16,unique=True,verbose_name='유저 이름')
    user_email = models.EmailField(max_length=128, unique=True, verbose_name='유저 이메일')
    user_phone = models.CharField(max_length=128,verbose_name='유저 전화번호',default='')
    user_gender = models.CharField(max_length=1,choices=GENDER_CHOICES, null=True, blank=True,verbose_name='유저 성별')

    def __str__(self):
        return self.user_name
    
    class Meta:
        db_table = 'user'
        verbose_name = '유저'
        verbose_name_plural = '유저'
    
