from django.contrib import admin
from .models import Order, Product_order
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Product_order)
class ProductOrderAdmin(admin.ModelAdmin):
    pass
