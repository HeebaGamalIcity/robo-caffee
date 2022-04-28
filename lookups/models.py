from django.db import models


class ProductCat(models.Model):
    en_name = models.CharField(max_length=255)
    ar_name = models.CharField(max_length=255)
    parent_cat = models.ForeignKey("ProductCat", null=True, on_delete=models.SET_NULL)


class Product(models.Model):
    product_cat = models.ForeignKey(ProductCat, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='drinks/')
    en_name = models.CharField(max_length=255)
    ar_name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    is_topping = models.BooleanField()


class Topping(models.Model):
    en_name = models.CharField(max_length=255)
    ar_name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='toppings/')
    product_cat = models.ForeignKey(ProductCat, on_delete=models.CASCADE)
