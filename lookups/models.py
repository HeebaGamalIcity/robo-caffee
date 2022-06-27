from django.db import models
from machines.models import Unit


class ProductCat(models.Model):
    en_name = models.CharField(max_length=255)
    ar_name = models.CharField(max_length=255)
    parent_cat = models.ForeignKey("ProductCat", null=True, on_delete=models.SET_NULL, blank=True)
    image = models.ImageField(upload_to='cat/', null=True)
    max_product = models.PositiveIntegerField(default=4)
    name = ""

    def __str__(self):
        return f"{self.en_name}"


class Topping(models.Model):
    en_name = models.CharField(max_length=255)
    ar_name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='toppings/')
    unit_index = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.en_name}"


class Product(models.Model):
    product_cat = models.ForeignKey(ProductCat, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    unit_index = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='drinks/')
    en_name = models.CharField(max_length=255)
    ar_name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    is_topping = models.BooleanField()
    toppings = models.ManyToManyField(Topping, null=True, blank=True)
    is_image = models.BooleanField()
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.en_name}"


class Image(models.Model):
    image = models.ImageField(upload_to='images_toppings/')
    tag = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.tag}"







