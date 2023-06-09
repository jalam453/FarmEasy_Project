from django.db import models
from users.models import Profile
from django.contrib.auth.models import User

class Product(models.Model):
    owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(blank=True, null=True)
    quantity = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.product_name)
    
