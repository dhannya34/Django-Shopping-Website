from django.db import models

# Create your models here.
class sellerregister_tb(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    file=models.FileField()
    status=models.CharField(max_length=20,default="pending")

class product_tb(models.Model):
    productname=models.CharField(max_length=20)
    price=models.IntegerField()
    details=models.CharField(max_length=20)
    stock=models.CharField(max_length=20)
    catagoryid=models.ForeignKey('site_admin.catagory_tb',on_delete=models.CASCADE)
    sellerid=models.ForeignKey(sellerregister_tb,on_delete=models.CASCADE)
    file=models.FileField()
class tracking_tb(models.Model):
    orderid=models.ForeignKey('site_user.order_tb',on_delete=models.CASCADE)
    details=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
