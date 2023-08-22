from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='kiosk'),
    path('choice/lotteria', views.lotteria, name='lotteria'),
    path('lotteria/confirm', views.confirmLotteria, name="confirmLotteria"),
    path('choice/',views.choice,name='choice'),
]