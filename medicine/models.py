from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    inde=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    brand=models.CharField(max_length=300)
    price=models.CharField(max_length=300)
    weight=models.CharField(max_length=300)
    flavour=models.CharField(max_length=300)
    pr=models.CharField(max_length=300)
    pemail=models.CharField(max_length=300)
    pphone=models.CharField(max_length=300)
    def __str__(self):
        return self.pr
