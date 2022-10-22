from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requests):
    return render(requests,"shop/index.html")

def about(requests):
    return HttpResponse("We are at about")

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

