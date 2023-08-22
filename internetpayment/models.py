from django.db import models
# Create your models here.

class Item(models.Model):
    user_name = models.CharField(max_length=128,verbose_name='수령인')
    item_phone = models.CharField(max_length=128,verbose_name='수령인 전화번호',default='')
    item_address = models.TextField(verbose_name='수령인 주소')
    item_require = models.CharField(max_length=128,verbose_name='요구사항')

    def __str__(self):
        return self.item_phone
    
    class Meta:
        db_table = 'item'
        verbose_name = '상품'
        verbose_name_plural = '상품'