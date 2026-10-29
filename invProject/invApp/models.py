from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    stock_keep_unit = models.CharField(max_length=50, unique=True)
    supplier = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.name
