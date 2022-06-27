from django.db import models
from lookups.models import Product, Topping, Image
from machines.models import Unit


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through='Product_order')
    #unit_state = models.ManyToManyField(Unit)
    state = models.IntegerField(default=0)
    qr_code = models.CharField(max_length=100, default=None, blank=True, null=True)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)


class Product_order(models.Model):
    state = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True)
    topping = models.ManyToManyField(Topping, null=True, blank=True)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
