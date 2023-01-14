from django.db import models
from adminApp.models import UserInfo, Product
from datetime import datetime
# Create your models here.

class MyCart(models.Model):
    user = models.ForeignKey(to='adminApp.UserInfo', on_delete = models.CASCADE)
    cake = models.ForeignKey(to='adminApp.Product', on_delete = models.CASCADE )
    qty = models.IntegerField()
     
    class Meta:
        db_table = "MyCart"



class OrderMaster(models.Model):
    user = models.ForeignKey(to='adminApp.UserInfo', on_delete = models.CASCADE)
    amount = models.FloatField(default=1000)
    dateOfOrder = models.DateTimeField(default=datetime.now)
    details = models.CharField(max_length=200)
     
    class Meta:
        db_table = "OrderMaster"
