from django.db import models
from lookups.models import Product


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through='Product_order')
    state = models.IntegerField(default=0)
    bar_code = models.CharField(max_length=100, default=None)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)


class Product_order(models.Model):
    state = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)