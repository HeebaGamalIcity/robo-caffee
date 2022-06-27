from django.contrib import admin
from .models import Order, Product_order
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("created_at", "state", "qr_code")


@admin.register(Product_order)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ("order", "state")
