from django.shortcuts import render
from django.http import HttpResponse

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
    print(product)
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


def _addUser(params={}):
    if USER:
        params['user'] = USER
    return params