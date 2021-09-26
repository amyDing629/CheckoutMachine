from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import CheckOut
checkout = CheckOut()
def index(request):
    item_list = []
    for item_info in checkout.get_item_list():
        item_list.append(item_info[0].get_name() + ' ' + str(item_info[0].get_price()) \
            + ' ' + str(item_info[1]))
    checkout_price = checkout.count_sum()
    return render(request, 'index.html', {'item_list': item_list, 'checkout_price': checkout_price})

def additem(request):
    if request.method == "POST":
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        checkout.add_item_to_list(name, int(quantity))
        return redirect('index')
    return render(request, 'additem.html')
    
