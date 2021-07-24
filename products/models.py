from django.db import models
from datetime import datetime,time
# Create your models here.
class Productinshop(models.Model):
    Product_name = models.CharField(max_length=255)
    image = models.CharField(max_length=2000)
class Product(models.Model):
    Product_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2000)
class BuyProducts(models.Model):
    Client_name = models.CharField(max_length=255)
    client_mobile = models.IntegerField()
    Products_name = models.CharField(max_length=255)
    Quantity = models.FloatField()
    price1 = models.FloatField()
    randid = models.IntegerField()
    Userdid = models.IntegerField()
class ClientDetailLog(models.Model):
    id = models.AutoField(primary_key=True)
    Client_name = models.CharField(max_length=255)
    client_mobile = models.IntegerField()
    randid = models.IntegerField()
class BillDetails(models.Model):
    Userid = models.IntegerField()
    Client_name = models.CharField(max_length=255)
    client_mobile = models.IntegerField()
    randId = models.IntegerField()
    BillDate = models.DateTimeField(auto_now_add=True,auto_now=False)
    BillConfirmDate = models.DateTimeField(auto_now_add=False,auto_now=True)
    TotalAmt = models.FloatField()
    BillCheck = models.CharField(max_length=100)
class PaymentDone(models.Model):
    Userid = models.IntegerField()
    Client_name = models.CharField(max_length=255)
    client_mobile = models.IntegerField()
    randId = models.IntegerField()
    BillConfirmDate = models.DateTimeField(auto_now_add=True,auto_now=False)
    paymentDate = models.DateTimeField(auto_now_add=False,auto_now=True)
    TotalAmt = models.FloatField()
    DonePayment = models.CharField(max_length=100)

class Client_details(models.Model):
    Userid = models.IntegerField()
    Client_name = models.CharField(max_length=255)
    client_mobile = models.IntegerField()
    Client_Add1 = models.CharField(max_length=255)
    Client_add2 = models.CharField(max_length=255)
    Client_add3 = models.CharField(max_length=255)
    Client_pin = models.IntegerField()
    randId = models.IntegerField()





