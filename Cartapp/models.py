from django.db import models
from Account.models import Account_details
from Category.models import Product
# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(Account_details, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
    
class Cart_Items(models.Model):
    user=models.ForeignKey(Account_details,on_delete=models.CASCADE)
    item=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)