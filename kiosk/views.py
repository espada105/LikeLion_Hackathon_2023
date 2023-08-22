from django.shortcuts import render
from .models import Burger

# Create your views here.

def main(request):
    return render(request, 'kiosk/kiosk.html')

def lotteria(request):
    if request.method == 'GET':
        burgers = Burger.objects.filter(type='Burger')
        drinks = Burger.objects.filter(type='Drink')
        desserts = Burger.objects.filter(type='Dessert')
        recommends = Burger.objects.filter(recommended=True)
        
        return render(request, 'kiosk/lotteria.html', {'burgers': burgers, 'drinks': drinks, 'desserts': desserts, 'recommends': recommends})

def confirmLotteria(request):
    return render(request, 'kiosk/confirm_lotteria.html')

def choice(request):
    return render(request, 'kiosk/choice_payment.html')