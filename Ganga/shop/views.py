from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json

from .models import Product, User

USER = None

# Create your views here.
def index(requests):
    products = Product.objects.all()
    for product in products:
        product.desc = product.desc[0:100]
    params = {'products':products}
    params = _addUser(params)
    return render(requests,"shop/index.html",params)

def about(requests):
    return render(requests,"shop/about.html",_addUser())

def contact(requests):
    return render(requests,"shop/contact.html",_addUser())


def search(requests):
    return render(requests,"shop/search.html",_addUser())

def product(requests,id):
    product = Product.objects.filter(id=id)
    return render(requests,"shop/product.html",{'product':product[0],**_addUser()})

def signup(requests):
    name = requests.POST.get('full-name')
    email = requests.POST.get('email')
    password = requests.POST.get('password')
    if name and email and password:
        user = User.objects.filter(email=email)
        if len(user) == 0:
            user = User(name=name,email=email,password=password)
            user.save()
            return render(requests,"shop/login.html")

    return render(requests,"shop/signup.html")

def login(requests):
    email = requests.POST.get('email')
    password = requests.POST.get('password')

    if email and password:
        user = User.objects.filter(email=email,password=password)
        if len(user) > 0:
            global USER
            USER = user[0]
            return index(requests)

    return render(requests,"shop/login.html")

def cart(requests):
    cart = requests.GET.get('cart',None)
    if cart:
        user = User.objects.filter(id=USER.id)
        user[0].cart = cart
        user[0].save()
        print("Saved cart:",cart)
    else:
        if USER:
            cart = USER.cart
        else:
            cart = []
        return JsonResponse(cart,safe=False)

def item(requests,id):
    if id:
        product = Product.objects.filter(id=id)
        if len(product) > 0:
        
            data ={
                'id':product[0].id,
                'name':product[0].product_name,
                'price':product[0].price,
                'image':product[0].image.url,
                'desc':product[0].desc,
            }
            return JsonResponse(data,safe=False)
    return JsonResponse([],safe=False)

def account(requests):
    return render(requests,"shop/account.html",_addUser())


def _addUser(params={}):
    if USER:
        params['user'] = USER
    return params



