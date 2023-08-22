from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
# Create your views here.
def internetpayment(request):
    return render(request, 'internetpayment/intpay.html')

def paymentcreate(request):
    if request.method == 'GET':
        form = ItemForm()
        return render(request, 'internetpayment/intpay.html',{'form':form})

    elif request.method=='POST':
        item = Item()
        item.user_name=request.POST['user_name']
        item.item_phone=request.POST['item_phone']
        item.item_address=request.POST['item_address']
        item.item_require=request.POST['item_require']
        item.save()

    return redirect('complete')

def complete(request):
    item = Item.objects.last()
    return render(request,'internetpayment/intpaycomplete.html',{'item':item})

