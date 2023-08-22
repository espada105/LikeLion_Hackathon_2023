from django.contrib import admin
from . import models

# Register your models here.

class BurgerAdmin(admin.ModelAdmin):
    list_filter = ('type',)
    search_fields = ['name']

admin.site.register(models.Burger, BurgerAdmin)