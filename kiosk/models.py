from django.db import models

# Create your models here.
class Burger(models.Model):
    MENU_TYPE = (
        ('Burger', 'Burger'),
        ('Drink', 'Drink'),
        ('Dessert', 'Dessert')
    )
    
    name = models.CharField(max_length=50, null=False)
    price = models.IntegerField()
    setPrice = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=10, choices=MENU_TYPE)
    image = models.ImageField(blank=True, upload_to='menu')
    recommended = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name