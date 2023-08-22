from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.internetpayment,name='internetpayment'),
    path('paymentcreate',views.paymentcreate,name='paymentcreate'),
    path('complete',views.complete,name='complete')
]