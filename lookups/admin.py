from django.contrib import admin
from .models import ProductCat, Product
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductCat)
class ProductCatAdmin(admin.ModelAdmin):
    pass
