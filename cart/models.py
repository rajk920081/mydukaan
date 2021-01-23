from django.db import models

# Create your models here.
from products.models import MasterProduct
from django.contrib.auth.models import User
class Cart(models.Model):
    product = models.ForeignKey(MasterProduct,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=0)
    datetime = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.product.name
