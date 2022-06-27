from django.contrib import admin
from .models import ProductCat, Product, Topping, Image
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductCat)
class ProductCatAdmin(admin.ModelAdmin):
    pass


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
