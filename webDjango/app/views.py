from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(req):
    return render(req, 'app/home.html')
