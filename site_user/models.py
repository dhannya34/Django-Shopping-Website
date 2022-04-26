from django.db import models
from site_seller.models import *
# Create your models here.
class register_tb(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class cart_tb(models.Model):
    productid=models.ForeignKey(product_tb,on_delete=models.CASCADE)
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    shippingaddress=models.CharField(max_length=20)
    contactno=models.CharField(max_length=20)
    quantity=models.IntegerField()
    totalprice=models.IntegerField()
class order_tb(models.Model):
    productid=models.ForeignKey('site_seller.product_tb',on_delete=models.CASCADE)
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    sellerid=models.ForeignKey('site_seller.sellerregister_tb',on_delete=models.CASCADE)
    shippingaddress=models.CharField(max_length=20)
    quantity=models.CharField(max_length=20)
    totalprice=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default="pending")
    


    
