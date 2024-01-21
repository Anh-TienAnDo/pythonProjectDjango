from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(req):
    content = {}
    return render(req, 'app/home.html', content)

def Cart(req):
    content = {}
    return render(req, 'app/cart.html', content)

def Checkout(req):
    content = {}
    return render(req, 'app/checkout.html', content)

def Login(req):
    content = {}
    return render(req, 'app/login.html', content)

def Singup(req):
    content = {}
    return render(req, 'app/signup.html', content)


