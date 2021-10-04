from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import CheckOut, Gateway
checkout = CheckOut()
gateway = Gateway()
def index(request):
    item_list = []
    for item_info in checkout.get_item_list():
        item_list.append(item_info[0].get_name() + ', ' + str(item_info[0].get_price()) \
            + ', ' + str(item_info[1]))
    checkout_price = checkout.count_sum()
    return render(request, 'index.html', {'item_list': item_list, 'checkout_price': checkout_price, 'tax': checkout.get_tax()})

def additem(request):
    if request.method == "POST":
        if request.POST.get("additem"):
            name = request.POST.get("name")
            quantity = request.POST.get("quantity")
            checkout.add_item_to_list(name, int(quantity))
            return redirect('index')
        if request.POST.get("back"):
            return redirect('index')
    return render(request, 'additem.html')

def edittax(request):
    if request.method == "POST":
        if request.POST.get("edittax"):
            tax = request.POST.get("tax")
            checkout.change_tax(float(tax))
            return redirect('index')
        if request.POST.get("back"):
            return redirect('index')
    return render(request, 'edittax.html')

def removeitem(request):
    if request.method == "POST":
        if request.POST.get("removeitem"):
            name = request.POST.get("name")
            quantity = request.POST.get("quantity")
            checkout.remove_item_from_list(name, int(quantity))
            return redirect('index')
        if request.POST.get("back"):
            return redirect('index')
    return render(request, 'removeitem.html')

def database_opt(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        # form = database_opt(request.POST)
        if request.POST.get("edit"):
            checkout.edit_price(name, int(price))
        if request.POST.get("remove"):
            checkout.remove_item_from_list(name, None)
            gateway.remove_item_from_database(name)
        if request.POST.get("add"):
            gateway.add_item_to_database(name, int(price))
        if request.POST.get("back"):
            return redirect('index')
    return render(request, 'database_opt.html') 
