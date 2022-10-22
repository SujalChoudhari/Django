from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

# Create your views here.
def index(requests):
    products = Product.objects.all()
    params = {'products':products}
    return render(requests,"shop/index.html",params)

def about(requests):
    return render(requests,"shop/about.html")

def contact(requests):
    return HttpResponse("We are at contact")

def tracker(requests):
    return HttpResponse("We are at tracker")

def search(requests):
    return HttpResponse("We are at search")

def product(requests):
    return HttpResponse("We are at product")

def checkout(requests):
    return HttpResponse("We are at checkout")

