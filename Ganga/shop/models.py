from unicodedata import category
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=600)
    publish_date = models.DateField()
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class User(models.Model):
    user_id = models.AutoField
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    cart =models.CharField(max_length=5000,default="")
    
    def __str__(self):
        return self.name