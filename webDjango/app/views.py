from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def Home(req):
    products = Product.objects.all()
    content = {'products': products}
    return render(req, 'app/home.html', content)

def Cart(req):
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        item=[]
    content = {'items': items, 'order': order}
    return render(req, 'app/cart.html', content)

def Checkout(req):
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        item = []
    content = {'items': items, 'order': order}
    return render(req, 'app/checkout.html', content)

def Login(req):
    content = {}
    return render(req, 'app/login.html', content)

def Singup(req):
    content = {}
    return render(req, 'app/signup.html', content)


